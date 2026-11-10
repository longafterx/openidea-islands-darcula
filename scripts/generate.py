#!/usr/bin/env python3
"""Build data-only themes and their provenance from pinned, offline resources.

Copyright 2026 longafter. SPDX-License-Identifier: Apache-2.0
The generated themes are modified ports of JetBrains color resources.
"""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path):
    return json.loads((ROOT / path).read_text())


def flatten(value, prefix=""):
    result = {}
    for key, item in value.items():
        name = f"{prefix}.{key}" if prefix else key
        if isinstance(item, dict) and not any(k.startswith("os.") for k in item):
            result.update(flatten(item, name))
        else:
            result[name] = item
    return result


def build():
    groups = read("sources/openidea-token-groups.json")
    mapping = read("sources/openidea-mapping.json")
    entries = {}
    for group in groups:
        for token in group["tokens"]:
            entries[token["name"]] = {
                "value": token["dark"], "status": "host-fallback",
                "source": "sources/openidea-token-groups.json",
                "key": token["name"], "file": "scheme" if group["scheme"] else "theme",
                "note": "Inherits Islands Dark; no verified equivalent mapped.",
            }

    # Parent resources provide named colors; explicit mappings below choose
    # semantic roles deliberately rather than pretending to render Swing defaults.
    ui, named = {}, {}
    for filename in ["darcula.theme.json", "expUI_dark.theme.json", "ManyIslandsDarcula.theme.json"]:
        source = f"sources/jetbrains/{filename}"
        data = read(source)
        ui.update({k: (v, source) for k, v in flatten(data["ui"]).items()})
        named.update({k: (v, source) for k, v in data.get("colors", {}).items()})

    def resolve(value):
        seen = set()
        while value in named:
            if value in seen:
                raise ValueError(f"Cyclic named color: {value}")
            seen.add(value)
            value = named[value][0]
        if not re.fullmatch(r"#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?", value):
            raise ValueError(f"Not a color: {value}")
        return value.lower()

    def set_token(token, value, source, key, status="mapped", note=""):
        file = entries.get(token, {}).get("file", "scheme")
        entries[token] = dict(value=value, source=source, key=key, status=status, note=note, file=file)

    def from_ui(token, key, status="mapped", note=""):
        value, source = ui[key]
        if isinstance(value, dict):
            value = value.get("os.mac", value.get("os.default"))
        set_token(token, resolve(value), source, f"ui.{key}", status, note)

    def from_named(token, key, status="mapped", note=""):
        value, source = named[key]
        set_token(token, resolve(value), source, f"colors.{key}", status, note)

    def alias(token, target, note="Same host role / shared palette."):
        set_token(token, f"var({target})", "derived", target, "derived", note)

    # Start with OpenIDEA's official mapping, resolving named colors in the
    # verified parent chain. Review critical roles explicitly below.
    for token, keys in mapping["UI_KEYS"].items():
        for key in keys:
            candidates = [key, "*." + key.rsplit(".", 1)[-1]]
            found = next((k for k in candidates if k in ui), None)
            if found:
                try:
                    from_ui(token, found)
                except (ValueError, TypeError):
                    continue
                break

    ui_roles = {
        "--bg-app": "*.background", "--bg-frame": "MainWindow.background",
        "--bg-island": "ToolWindow.background", "--bg-elev": "ToolWindow.background",
        "--bg-hover": "*.hoverBackground", "--bg-selected": "*.selectionBackground",
        "--bg-selected-strong": "*.lightSelectionBackground",
        "--bg-tree-selected": "*.selectionBackground",
        "--bg-tree-selected-inactive": "*.selectionInactiveBackground",
        "--bg-tree-hover": "*.hoverBackground", "--fg-icon": "*.foreground",
        "--fg-muted": "Label.infoForeground", "--fg-secondary": "Label.infoForeground",
        "--fg-subtle": "Button.disabledText", "--fg-faint": "Button.disabledText",
        "--bg-tab-selected-inactive": "EditorTabs.inactiveUnderlinedTabBackground",
        "--border-tab-selected-inactive": "EditorTabs.inactiveUnderlinedTabBorderColor",
        "--border-editor-tabs": "EditorTabs.underTabsBorderColor",
        "--bg-stripe-hover": "MainToolbar.Dropdown.transparentHoverBackground",
        "--fg-stripe-selected-active": "ToolWindow.Button.selectedForeground",
        "--fg-stripe-label": "ToolWindow.Button.foreground",
        "--bg-toolbar-hover": "ActionButton.hoverBackground",
        "--bg-popup-advertiser": "Popup.Advertiser.background",
        "--danger": "Label.errorForeground", "--warning": "Label.warningForeground",
        "--success": "VersionControl.Merge.Status.NoConflicts.foreground",
        "--bg-button": "Button.startBackground", "--border-button": "Button.startBorderColor",
        "--bg-control": "Button.startBackground", "--control-off": "Component.borderColor",
        "--bg-control-hover": "ActionButton.pressedBackground",
        "--bg-active": "ActionButton.pressedBackground",
        "--fg-completion-match": "CompletionPopup.matchForeground",
    }
    for token, key in ui_roles.items():
        from_ui(token, key)
    for token, key in {
        "--info": "Blue8", "--bg-toolbar-selected": "SelectionActive",
        "--bg-toolbar-selected-hover": "SelectionActiveLight",
        "--bg-button-primary-hover": "ComponentBorderFocus",
        "--bg-toggle-on": "SelectionActive", "--bg-toggle-off": "InputBackground",
        "--border-toggle": "ComponentBorder", "--bg-toggle-knob": "ForegroundDefault",
        "--fg-toggle-on": "ForegroundDefault", "--fg-toggle-off": "ForegroundDefault",
        "--bg-checkbox": "InputBackground", "--border-checkbox": "ComponentBorder",
    }.items():
        from_named(token, key, "approximation", "Reuses verified palette for a different host control/state.")
    # Prefer the actual icon color palette for checkbox surfaces (no icons copied).
    icon_palette = read("sources/jetbrains/ManyIslandsDarcula.theme.json")["icons"]["ColorPalette"]
    for token, key in [("--bg-checkbox", "Checkbox.Background.Default"), ("--border-checkbox", "Checkbox.Border.Default")]:
        set_token(token, resolve(icon_palette[key]), "sources/jetbrains/ManyIslandsDarcula.theme.json", f"icons.ColorPalette.{key}")
    for kind in ["info", "error", "warning", "success"]:
        for part, prefix in [("Background", "--bg-feedback-"), ("Border", "--border-feedback-")]:
            from_ui(prefix + kind, f"Editor.ToolTip.{kind}{part}", "approximation", "Editor tooltip status palette projected onto host banners.") if kind != "info" else from_named(prefix + kind, "Blue1" if part == "Background" else "Blue3", "approximation", "No one-to-one banner key; verified blue status palette.")
    for token, target in {
        "--bg-popup-inline": "--bg-popup", "--bg-dialog": "--bg-app",
        "--bg-stripe-tooltip": "--bg-tooltip", "--fg-stripe-tooltip": "--fg-tooltip",
        "--border-stripe-tooltip": "--border-tooltip", "--shadow-stripe-tooltip": "--shadow-tooltip",
    }.items():
        alias(token, target)

    # Read both schemes. A Darcula <value/> is a deliberate reset, never a
    # reason to copy the Default scheme's bright colors into a dark theme.
    scheme_source = "sources/jetbrains/DefaultColorSchemesManager.xml"
    tree = ET.parse(ROOT / scheme_source)
    schemes = {s.get("name"): s for s in tree.getroot().findall("scheme")}
    colors = {o.get("name"): o.get("value") for o in schemes["Darcula"].findall("./colors/option")}
    attrs = {o.get("name"): {p.get("name"): p.get("value") for p in o.findall("./value/option")} for o in schemes["Darcula"].findall("./attributes/option")}

    def icls(token, key, part=None, status="mapped", note=""):
        if part:
            value = attrs[key].get(part)
        else:
            value = colors[key]
        if not value:
            raise ValueError(f"Missing Darcula value: {key}.{part}")
        value = "#" + value.lower().zfill(6 if len(value) <= 6 else 8)
        path = f"Darcula/{'attributes' if part else 'colors'}/{key}" + (f"/{part}" if part else "")
        set_token(token, value, scheme_source, path, status, note)

    for key, tokens in mapping["ICLS_COLORS"].items():
        if colors.get(key):
            for token in tokens:
                icls(token, key)
    for key, pairs in mapping["ICLS_ATTRIBUTES"].items():
        for part, token in pairs:
            if attrs.get(key, {}).get(part):
                icls(token, key, part)

    # The converter cannot infer these missing/default attribute fallbacks.
    # Project generic host syntax categories onto explicit Darcula values;
    # language-specific categories are approximations, not exact IDEA scopes.
    syntax_roles = {
        "--syn-type": "TEXT", "--syn-variable": "TEXT", "--syn-global": "TEXT",
        "--syn-param": "TEXT", "--syn-punct": "TEXT", "--syn-namespace": "TEXT",
        "--syn-function-call": "TEXT", "--syn-docstring": "DEFAULT_DOC_COMMENT",
        "--syn-builtin": "TEXT", "--syn-self": "TEXT", "--syn-keyword-arg": "TEXT",
        "--syn-predefined": "TEXT", "--syn-regexp": "DEFAULT_STRING",
        "--syn-tag": "XML_TAG_NAME", "--syn-attribute": "XML_ATTRIBUTE_NAME",
        "--syn-link": "CTRL_CLICKABLE", "--syn-markup-heading": "TEXT",
        "--syn-markup-code": "DEFAULT_STRING", "--syn-python-local-variable": "TEXT",
        "--syn-python-global-variable": "TEXT", "--syn-python-instance-attribute": "DEFAULT_INSTANCE_FIELD",
        "--syn-python-class-attribute": "DEFAULT_STATIC_FIELD", "--syn-python-constant": "DEFAULT_CONSTANT",
        "--syn-python-property": "DEFAULT_INSTANCE_FIELD", "--syn-python-type-parameter": "TYPE_PARAMETER_NAME_ATTRIBUTES",
        "--syn-python-builtin": "TEXT", "--syn-python-predefined-definition": "TEXT",
        "--syn-python-predefined-usage": "TEXT", "--syn-python-fstring": "DEFAULT_STRING",
        "--syn-python-bytes": "DEFAULT_STRING", "--syn-php-variable": "TEXT",
        "--syn-php-function-call": "TEXT", "--syn-bracket-1": "TEXT",
        "--syn-bracket-2": "TEXT", "--syn-bracket-3": "TEXT",
    }
    for token, key in syntax_roles.items():
        icls(token, key, "FOREGROUND", "approximation", "Shared host syntax category; language fallback/semantic scopes need visual calibration.")
    # The source has RAINBOW_COLOR0..4, while OpenIDEA names its five tokens 1..5.
    for index in range(5):
        icls(f"--syn-rainbow-{index + 1}", f"RAINBOW_COLOR{index}", "FOREGROUND", "mapped", "Corrected zero-based source index; not bracket colors.")
    icls("--syn-invalid", "BAD_CHARACTER", "EFFECT_COLOR", "approximation", "Host invalid text foreground uses IDEA's box/effect color.")
    set_token("--syn-comment-style", "normal", scheme_source, "Darcula/attributes/DEFAULT_LINE_COMMENT", "mapped", "No italic FONT_TYPE; use normal.")
    set_token("--syn-doc-comment-tag-effect", "underline", scheme_source, "Darcula/attributes/DEFAULT_DOC_COMMENT_TAG/EFFECT_TYPE=1", "mapped")
    set_token("--syn-doc-markup-bg", "transparent", scheme_source, "Darcula/attributes/DEFAULT_DOC_MARKUP/BACKGROUND(empty)", "mapped", "Explicitly cleared in source.")

    editor_colors = {
        "--bg-editor-selection-inactive": "SELECTION_BACKGROUND_INACTIVE",
        "--border-method-separator": "METHOD_SEPARATORS_COLOR",
        "--fg-gutter": "LINE_NUMBERS_COLOR", "--fg-fold-marker": "TEARLINE_COLOR",
    }
    for token, key in editor_colors.items():
        icls(token, key)
    icls("--bg-debug-line", "EXECUTIONPOINT_ATTRIBUTES", "BACKGROUND")
    icls("--bg-editor-banner", "NOTIFICATION_BACKGROUND")
    icls("--bg-editor-gutter", "TEXT", "BACKGROUND", "approximation", "Converter uses editor background in new UI when EDITOR_GUTTER_BACKGROUND is absent; classic GUTTER_BACKGROUND is not used.")
    icls("--border-gutter", "TEXT", "BACKGROUND", "approximation", "No separate gutter border in source; merge into editor surface.")
    icls("--bg-matched-tag", "MATCHED_BRACE_ATTRIBUTES", "BACKGROUND", "approximation", "Host shares brace and tag match surfaces.")
    icls("--bg-text-search-result-current", "TEXT_SEARCH_RESULT_ATTRIBUTES", "BACKGROUND", "approximation", "No separate active occurrence background available.")
    icls("--wave-warning", "WARNING_ATTRIBUTES", "ERROR_STRIPE_COLOR", "approximation", "Source warning has background/stripe but no EFFECT_COLOR; use stripe for host wave.")
    icls("--editor-warning-background", "WARNING_ATTRIBUTES", "BACKGROUND")
    icls("--fg-weak-warning", "NOT_USED_ELEMENT_ATTRIBUTES", "FOREGROUND", "approximation", "No equivalent weak-warning foreground mapped.")
    from_ui("--fg-bulb", "Label.warningForeground", "approximation", "Host bulb uses warning UI foreground.")
    for token, target in {
        "--bg-editor-inline": "--bg-editor", "--bg-search-match-current": "--bg-search-match",
        "--fg-search-match": "--fg-editor",
    }.items():
        alias(token, target)
    # IDEA search editor backgrounds are green, so the text must retain the
    # editor foreground instead of the host's black-on-yellow default.
    set_token("--matched-brace-weight", "700", scheme_source, "Darcula/attributes/MATCHED_BRACE_ATTRIBUTES/FONT_TYPE=1", "mapped")
    for kind in ["error", "warning"]:
        token = "--editor-" + kind + "-decoration"
        set_token(token, f"underline wavy var(--wave-{kind})", "derived", f"--wave-{kind}", "derived", "Host renders IDEA diagnostic effects as CSS decorations.")

    # Console gray/white have non-obvious names; bright white is
    # CONSOLE_WHITE_OUTPUT, not CONSOLE_GRAY_OUTPUT.
    ansi_keys = {
        "black": "BLACK", "red": "RED", "green": "GREEN", "yellow": "YELLOW",
        "blue": "BLUE", "magenta": "MAGENTA", "cyan": "CYAN", "white": "GRAY",
        "bright-black": "DARKGRAY", "bright-red": "RED_BRIGHT", "bright-green": "GREEN_BRIGHT",
        "bright-yellow": "YELLOW_BRIGHT", "bright-blue": "BLUE_BRIGHT", "bright-magenta": "MAGENTA_BRIGHT",
        "bright-cyan": "CYAN_BRIGHT", "bright-white": "WHITE",
    }
    for color, key in ansi_keys.items():
        icls("--ansi-" + color, f"CONSOLE_{key}_OUTPUT", "FOREGROUND")
        alias("--terminal-ansi-" + color, "--ansi-" + color, "Classic Darcula console palette; new block-terminal palette is intentionally separate upstream.")

    # Freeze only themeable overrides; omit unsupported/unmapped host values.
    theme = {"id": "islands-darcula", "name": "Islands Darcula", "kind": "dark", "tokens": {}}
    scheme = {"name": "Islands Darcula", "tokens": {}}
    for token, item in entries.items():
        if item["status"] != "host-fallback":
            (scheme if item["file"] == "scheme" else theme)["tokens"][token] = item["value"]
    return theme, scheme, entries


def render():
    theme, scheme, entries = build()
    header = "// Modified port, Copyright 2026 longafter. SPDX-License-Identifier: Apache-2.0\n// Original colors: JetBrains; format: OpenIDEA. See NOTICE and docs/COLOR-SOURCES.md.\n// Rebuild with python3 scripts/generate.py; approximations are recorded per token.\n"
    result = {}
    for name, data in [("theme", theme), ("scheme", scheme)]:
        result[f"themes/islands-darcula.{name}.json"] = header + json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    result["sources/token-provenance.json"] = json.dumps(entries, indent=2, ensure_ascii=False) + "\n"
    lines = ["# Token 映射明细", "", "由 `python3 scripts/generate.py` 离线生成。`mapped` 表示原始数值已核验、角色已映射，不代表跨宿主实机视觉完全一致。`approximation` 是明确的语义近似；`derived` 为别名/宿主表达；`host-fallback` 不写入插件，继承 Islands Dark。", "", "| Token | 值 | 状态 | 文件 / 键 | 说明 |", "| --- | --- | --- | --- | --- |"]
    for token, item in entries.items():
        lines.append(f"| `{token}` | `{item['value']}` | {item['status']} | `{item['source']}` · `{item['key']}` | {item['note']} |")
    result["docs/TOKEN-MAPPING.md"] = "\n".join(lines) + "\n"
    return result


if __name__ == "__main__":
    for path, content in render().items():
        (ROOT / path).write_text(content)
    theme, scheme, entries = build()
    print(f"Generated {len(theme['tokens'])} UI + {len(scheme['tokens'])} editor tokens; "
          f"{sum(e['status'] == 'host-fallback' for e in entries.values())} documented host fallbacks.")
