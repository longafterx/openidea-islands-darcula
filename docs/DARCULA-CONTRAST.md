# Darcula Contrast color sources

Research date: **2026-11-25**. The target is JetBrains **Darcula Contrast** editor colors with the **Islands Darcula** interface and original **PhpStorm PHP syntax colors**. Original source RGB values take priority over third-party ports and OpenIDEA defaults.

## Original JetBrains resources

Resources are pinned to IntelliJ Community tag `idea/262.10968.63`, commit `8062c061ff33e22041d9f1844db5b8b8a6b5e4d7`. Public links and SHA-256 hashes are recorded in [UPSTREAM.json](../sources/UPSTREAM.json).

| Resource in `sources/jetbrains/` | Purpose |
| --- | --- |
| `expUI_darculaContrastScheme.xml` | Original Darcula Contrast editor overlay; `parent_scheme="Darcula"` |
| `DefaultColorSchemesManager.xml` | Base Darcula editor values inherited by the contrast scheme |
| `ManyIslandsDarcula.theme.json` | Islands Darcula UI; parent `ExperimentalDark` |
| `expUI_dark.theme.json` | UI parent; parent `Darcula` |
| `darcula.theme.json` | UI ancestor providing text, links, and basic controls |

The [original Darcula Contrast definition](https://github.com/JetBrains/intellij-community/blob/8062c061ff33e22041d9f1844db5b8b8a6b5e4d7/platform/platform-resources/src/themes/expUI/expUI_darculaContrastScheme.xml) supplies the darker editor background and revised current line, gutter, indent guides, warnings, and matched braces. Syntax colors absent from that overlay inherit Darcula. The generator tracks the actual defining file and scheme for every mapped value. An explicit attribute replaces its parent's entire attribute, including empty resets, so missing parts do not leak in from a parent.

JetBrains' [PhpStorm documentation](https://www.jetbrains.com/help/phpstorm/configuring-colors-and-fonts.html) lists Darcula Contrast separately from Darcula and distinguishes editor schemes from [interface themes](https://www.jetbrains.com/help/phpstorm/user-interface-themes.html). Documentation confirms scheme identity; XML resources provide the actual colors.

## Key editor mappings

| OpenIDEA token | Value | Defining scheme / key |
| --- | --- | --- |
| `--bg-editor` | `#1e1f22` | Darcula Contrast / `TEXT.BACKGROUND` |
| `--fg-editor` | `#a9b7c6` | Darcula Contrast / `TEXT.FOREGROUND` |
| `--bg-current-line` | `#2b2d30` | Darcula Contrast / `CARET_ROW_COLOR` |
| `--fg-line-number` / current | `#4e5157` / `#9da0a8` | Darcula Contrast / `LINE_NUMBERS_COLOR`, `LINE_NUMBER_ON_CARET_ROW_COLOR` |
| Indent guide / active | `#313438` / `#6f737a` | Darcula Contrast / `INDENT_GUIDE`, `SELECTED_INDENT_GUIDE` |
| Right margin / method separator | `#393b40` / `#43454a` | Darcula Contrast / `RIGHT_MARGIN_COLOR`, `METHOD_SEPARATORS_COLOR` |
| Matched brace background | `#326146` | Darcula Contrast / `MATCHED_BRACE_ATTRIBUTES.BACKGROUND` |
| Warning background | `#3d3322` | Darcula Contrast / `WARNING_ATTRIBUTES.BACKGROUND` |
| Keywords / strings / numbers | `#cc7832` / `#6a8759` / `#6897bb` | Darcula / `DEFAULT_KEYWORD`, `DEFAULT_STRING`, `DEFAULT_NUMBER` |
| Comments / documentation | `#808080` / `#629755` | Darcula / `DEFAULT_LINE_COMMENT`, `DEFAULT_DOC_COMMENT` |
| Function declarations / fields | `#ffc66d` / `#9876aa` | Darcula / `DEFAULT_FUNCTION_DECLARATION`, `DEFAULT_INSTANCE_FIELD` |
| PHP variables | `#9876aa` | Official PHP plugin / `PHP_VAR` |
| PHP function calls | `#ffc66d` | `PHP_FUNCTION_CALL → PHP_INSTANCE_METHOD → DEFAULT_INSTANCE_METHOD → DEFAULT_FUNCTION_DECLARATION` |
| Editor selection / inactive | `#214283` / `#4c4f56` | Inherited Darcula selection colors |
| Caret | `#bbbbbb` | Darcula / `CARET_COLOR` |

## PHP variables

The official JetBrains [PHP plugin](https://plugins.jetbrains.com/plugin/6610-php), version **252.28539.167**, was downloaded from JetBrains Marketplace and inspected read-only. In `php-impl/lib/php.jar!/colorScheme/PhpDarcula.xml`, both `PHP_VAR` and `PHP_PARAMETER` explicitly use **`#9876aa`**. That resource is registered for Darcula, the parent of Darcula Contrast. Archive and resource hashes, download URL, and observed color values are recorded in UPSTREAM.json. The plugin archive and proprietary XML are not distributed with this project.

The generator applies the observed stock `PHP_VAR` value to OpenIDEA's dedicated `--syn-php-variable` role. Function calls use **`#ffc66d`**: inspection of `php-frontback.jar!/com/jetbrains/php/lang/highlighter/PhpHighlightingData.class` confirms `PHP_FUNCTION_CALL → PHP_INSTANCE_METHOD → DEFAULT_INSTANCE_METHOD`; the platform's [DefaultLanguageHighlighterColors.java](https://github.com/JetBrains/intellij-community/blob/8062c061ff33e22041d9f1844db5b8b8a6b5e4d7/platform/core-api/src/com/intellij/openapi/editor/DefaultLanguageHighlighterColors.java) connects `DEFAULT_INSTANCE_METHOD` to `DEFAULT_FUNCTION_DECLARATION`. Resource hashes and the observed fallback chain are recorded in UPSTREAM.json. Generic variables and parameters in other languages retain their Darcula colors. PHP categories without a dedicated host token cannot be customized independently by this data-only plugin.

## Interface and shared controls

The interface retains the original Islands Darcula palette: application/tool windows `#2b2b2b`, frame `#3c3f41`, popups `#333333`, tooltips `#4b4d4d`, normal text `#bbbbbb`, borders `#404040`, and active tree selection `#304c80`. These are UI values, independent of the darker Darcula Contrast editor background.

The complete [token ledger](DARCULA-CONTRAST-TOKEN-MAPPING.md) and [machine-readable provenance](../sources/darcula-contrast-token-provenance.json) document each output and host fallback. `mapped` means a source RGB value and role were verified; it does not imply identical rendering across applications.

## Approximations and host behavior

- OpenIDEA has fewer syntax roles than PhpStorm. Types, calls, Python categories, Markdown, regex, and brackets use documented projections of the base palette where an exact language-specific source role is unavailable.
- Unspecified generic syntax roles use explicit Darcula text or related attributes. Bright colors from the light Default scheme are not substituted for missing dark attributes.
- Warning waves use `WARNING_ATTRIBUTES.ERROR_STRIPE_COLOR` because the source has no effect color. Invalid text uses the source's bad-character effect color as foreground.
- UI and editor searches share a host token. Editor search-result green takes priority over the UI's golden search highlight.
- Source rainbow identifiers `RAINBOW_COLOR0…4` map to host `1…5`. Brackets use ordinary text colors rather than identifier colors.
- The editor gutter and its border use the editor background, following the host converter when `EDITOR_GUTTER_BACKGROUND` is absent. The classic Darcula gutter background is not forced onto the new UI.
- Terminal ANSI colors use the classic Darcula console palette inherited by Darcula Contrast. The newer block-terminal palette is separate upstream.
- Derived aliases retain shared host roles. Unsupported shadows, traffic-light controls, chart series, database status, and scrim values inherit OpenIDEA Islands Dark; the ledger identifies all such fallbacks.
- Layout, fonts, spacing, rendering, and unsupported font effects remain host-controlled. A side-by-side PhpStorm/OpenIDEA comparison has not been performed for this revision.

## Host reference

OpenIDEA's API and token inventory are pinned to [v0.1.40](https://github.com/l0ng-ai/openidea/tree/v0.1.40), commit `37c2a6048eea89d4f6db645622612358b643862b`. `intellijTheme.ts` provides the original conversion mappings; `tokens.css` identifies supported tokens. Host colors are used only for documented fallbacks.
