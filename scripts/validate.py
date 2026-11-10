#!/usr/bin/env python3
"""Offline integrity/coverage checks; complement the official plugin CLI.

Copyright 2026 longafter. SPDX-License-Identifier: Apache-2.0
"""

import hashlib
import json
import re
import tomllib
from collections import Counter
from pathlib import Path

from generate import ROOT, render


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_jsonc(path):
    # Generated files use only full-line comments, never inline comments.
    text = "\n".join(line for line in path.read_text().splitlines() if not line.lstrip().startswith("//"))
    return json.loads(text)


def main():
    upstream = json.loads((ROOT / "sources/UPSTREAM.json").read_text())
    for path, info in upstream["files"].items():
        require(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == info["sha256"], f"Upstream hash mismatch: {path}")
    print(f"PASS: {len(upstream['files'])} pinned source hashes")
    for path, text in render().items():
        require((ROOT / path).read_text() == text, f"Generated file is stale: {path}; run scripts/generate.py")
    print("PASS: generated theme, scheme and provenance match source recipes")

    manifest = tomllib.loads((ROOT / "plugin.toml").read_text())
    require(manifest["id"] == "longafter.islands-darcula", "Unexpected plugin identity")
    require(not manifest["id"].startswith("openidea."), "Reserved plugin namespace")
    require(manifest["engines"]["openidea"] == "^1.0", "Unexpected API range")
    require(not any(k in manifest for k in ["wasm", "capabilities", "activation", "openidea-api"]), "Plugin must remain data-only")
    require(set(manifest["contributes"]) == {"themes"}, "Unexpected executable contribution")
    require(len(manifest["contributes"]["themes"]) == 1, "Expected one theme")
    decl = manifest["contributes"]["themes"][0]
    for field in ["path", "editor-scheme"]:
        path = Path(decl[field])
        require(not path.is_absolute() and (ROOT / path).resolve().is_relative_to(ROOT), f"Unsafe path: {path}")
    theme = load_jsonc(ROOT / decl["path"])
    scheme = load_jsonc(ROOT / decl["editor-scheme"])
    require(theme["id"] == "islands-darcula" and theme["kind"] == "dark", "Invalid theme identity/kind")
    require(theme["name"] == scheme["name"] == "Islands Darcula", "Inconsistent display names")
    tokens = {**theme["tokens"], **scheme["tokens"]}
    require(not (theme["tokens"].keys() & scheme["tokens"].keys()), "Accidental UI/editor override collision")
    require(len(tokens) <= 512, "Host token limit exceeded")
    inventory = json.loads((ROOT / "sources/openidea-token-groups.json").read_text())
    defaults = {t["name"]: t["dark"] for g in inventory for t in g["tokens"]}
    # These derived editor tokens are defined in tokens.css outside its Light block.
    allowed = set(defaults) | {"--bg-editor", "--bg-editor-gutter", "--border-method-separator"}
    required = {
        "--bg-app", "--bg-frame", "--bg-island", "--bg-editor", "--fg-editor",
        "--syn-keyword", "--syn-string", "--syn-comment", "--syn-type", "--syn-function",
        "--syn-number", "--caret", "--bg-current-line", "--bg-editor-selection",
        "--fg-line-number", "--wave-error", "--wave-warning", "--editor-error-decoration",
        "--editor-warning-decoration", "--bg-tab-selected", "--bg-tree-selected",
        "--bg-popup", "--bg-tooltip", "--bg-input",
    }
    require(required <= tokens.keys(), f"Missing P0 tokens: {required - tokens.keys()}")
    require(tokens.keys() <= allowed, f"Unknown host tokens: {tokens.keys() - allowed}")
    provenance = json.loads((ROOT / "sources/token-provenance.json").read_text())
    require(tokens.keys() <= provenance.keys(), "Tokens missing provenance")
    for key, value in tokens.items():
        require(not re.search(r"[;{}<>\\\n]|url\(|image\(", value, re.I), f"Unsupported CSS value: {key}")
        require(not re.match(r"--(?:fs|h|radius|font|space)-", key), f"Layout/font override: {key}")
        require(provenance[key]["value"] == value, f"Provenance mismatch: {key}")
    inherited = {k for k, e in provenance.items() if e["status"] == "host-fallback"}
    require(set(defaults) - tokens.keys() == inherited, "Unrecorded host fallbacks")

    values = {**defaults, **tokens}

    def resolve(key, stack=()):
        require(key in values, f"Unresolved token: {key}")
        require(key not in stack, f"Cyclic token alias: {key}")
        return re.sub(r"var\((--[a-z0-9-]+)\)", lambda m: resolve(m[1], (*stack, key)), values[key])

    for key in values:
        resolve(key)
    print(f"PASS: manifest, JSONC, P0 coverage, {len(tokens)} supported tokens, aliases and safe CSS")
    print("Provenance:", dict(Counter(e["status"] for e in provenance.values())))

    def luminance(value):
        require(bool(re.fullmatch(r"#[0-9a-f]{6}", value)), f"Expected opaque RGB for contrast: {value}")
        rgb = [int(value[i:i + 2], 16) / 255 for i in [1, 3, 5]]
        rgb = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
        return sum(a * b for a, b in zip(rgb, [0.2126, 0.7152, 0.0722]))

    for fg, bg, minimum in [
        ("--fg", "--bg-app", 4.5), ("--fg-editor", "--bg-editor", 4.5),
        ("--fg-editor", "--bg-editor-selection", 4.5), ("--fg", "--bg-tree-selected", 4.0),
        ("--fg-tooltip", "--bg-tooltip", 4.0), ("--syn-comment", "--bg-editor", 3.0),
        ("--syn-string", "--bg-editor", 3.0),
    ]:
        a, b = sorted([luminance(resolve(fg)), luminance(resolve(bg))])
        ratio = (b + 0.05) / (a + 0.05)
        require(ratio >= minimum, f"Contrast below palette sanity threshold: {fg}/{bg} = {ratio:.2f}")
        print(f"Contrast {fg}/{bg}: {ratio:.2f}:1 (minimum {minimum})")
    print("PASS: palette sanity checks (not a comprehensive accessibility audit)")


if __name__ == "__main__":
    main()
