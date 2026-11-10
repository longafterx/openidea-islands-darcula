# Token 映射明细

由 `python3 scripts/generate.py` 离线生成。`mapped` 表示原始数值已核验、角色已映射，不代表跨宿主实机视觉完全一致。`approximation` 是明确的语义近似；`derived` 为别名/宿主表达；`host-fallback` 不写入插件，继承 Islands Dark。

| Token | 值 | 状态 | 文件 / 键 | 说明 |
| --- | --- | --- | --- | --- |
| `--bg-app` | `#2b2b2b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.background` |  |
| `--bg-elev` | `#2b2b2b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ToolWindow.background` |  |
| `--bg-popup` | `#333333` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Popup.background` |  |
| `--bg-floating-toolbar` | `#393b40` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Toolbar.Floating.background` |  |
| `--bg-hover` | `#393b40` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.hoverBackground` |  |
| `--bg-selected` | `#304c80` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.selectionBackground` |  |
| `--bg-selected-strong` | `#304c80` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.lightSelectionBackground` |  |
| `--bg-current-line` | `#323232` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/CARET_ROW_COLOR` |  |
| `--bg-debug-line` | `#2d6099` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/EXECUTIONPOINT_ATTRIBUTES/BACKGROUND` |  |
| `--bg-backdrop` | `#333333` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Popup.background` |  |
| `--bg-input` | `#2b2b2b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.TextField.background` |  |
| `--border` | `#404040` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Borders.color` |  |
| `--border-popup` | `#474747` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Popup.borderColor` |  |
| `--border-strong` | `#5c5c5c` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Component.borderColor` |  |
| `--border-window` | `#404040` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Borders.ContrastBorderColor` |  |
| `--control-off` | `#5c5c5c` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Component.borderColor` |  |
| `--fg-strong` | `#bbbbbb` | mapped | `sources/jetbrains/darcula.theme.json` · `ui.Label.selectedForeground` |  |
| `--fg-emphasis` | `#bbbbbb` | mapped | `sources/jetbrains/darcula.theme.json` · `ui.Label.foreground` |  |
| `--fg` | `#bbbbbb` | mapped | `sources/jetbrains/darcula.theme.json` · `ui.Label.foreground` |  |
| `--fg-secondary` | `#828282` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Label.infoForeground` |  |
| `--fg-muted` | `#828282` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Label.infoForeground` |  |
| `--fg-subtle` | `#777777` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.disabledText` |  |
| `--fg-faint` | `#777777` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.disabledText` |  |
| `--fg-gutter` | `#606366` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/LINE_NUMBERS_COLOR` |  |
| `--fg-icon` | `#bbbbbb` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.foreground` |  |
| `--accent` | `#365880` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.default.startBackground` |  |
| `--link` | `#589df6` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Link.activeForeground` |  |
| `--link-hover` | `#589df6` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Link.hoverForeground` |  |
| `--chart-series` | `#e07a7c` | host-fallback | `sources/openidea-token-groups.json` · `--chart-series` | Inherits Islands Dark; no verified equivalent mapped. |
| `--danger` | `#db5c5c` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.Label.errorForeground` |  |
| `--warning` | `#ba9752` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.Label.warningForeground` |  |
| `--success` | `#57965c` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.VersionControl.Merge.Status.NoConflicts.foreground` |  |
| `--db-connected` | `#2fe02f` | host-fallback | `sources/openidea-token-groups.json` · `--db-connected` | Inherits Islands Dark; no verified equivalent mapped. |
| `--db-connected-ring` | `#1d6b1d` | host-fallback | `sources/openidea-token-groups.json` · `--db-connected-ring` | Inherits Islands Dark; no verified equivalent mapped. |
| `--info` | `#548af7` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `colors.Blue8` | Reuses verified palette for a different host control/state. |
| `--vcs-modified` | `#6897bb` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/FILESTATUS_MODIFIED` |  |
| `--vcs-added` | `#629755` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/FILESTATUS_ADDED` |  |
| `--vcs-deleted` | `#6c6c6c` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/FILESTATUS_DELETED` |  |
| `--vcs-untracked` | `#d1675a` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/FILESTATUS_UNKNOWN` |  |
| `--vcs-ignored` | `#848504` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/FILESTATUS_IDEA_FILESTATUS_IGNORED` |  |
| `--vcs-conflict` | `#d5756c` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/FILESTATUS_IDEA_FILESTATUS_MERGED_WITH_CONFLICTS` |  |
| `--gutter-modified` | `#374752` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/MODIFIED_LINES_COLOR` |  |
| `--gutter-added` | `#384c38` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/ADDED_LINES_COLOR` |  |
| `--gutter-deleted` | `#656e76` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/DELETED_LINES_COLOR` |  |
| `--diff-modified` | `#385570` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_MODIFIED/BACKGROUND` |  |
| `--diff-inserted` | `#294436` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_INSERTED/BACKGROUND` |  |
| `--diff-deleted` | `#484a4a` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_DELETED/BACKGROUND` |  |
| `--diff-modified-stripe` | `#43698d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_MODIFIED/ERROR_STRIPE_COLOR` |  |
| `--diff-inserted-stripe` | `#447152` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_INSERTED/ERROR_STRIPE_COLOR` |  |
| `--diff-deleted-stripe` | `#656e76` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_DELETED/ERROR_STRIPE_COLOR` |  |
| `--diff-conflict-stripe` | `#8f5247` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DIFF_CONFLICT/ERROR_STRIPE_COLOR` |  |
| `--syn-keyword` | `#cc7832` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_KEYWORD/FOREGROUND` |  |
| `--syn-string` | `#6a8759` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_STRING/FOREGROUND` |  |
| `--syn-type` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-function` | `#ffc66d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_FUNCTION_DECLARATION/FOREGROUND` |  |
| `--syn-function-call` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-comment` | `#808080` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_LINE_COMMENT/FOREGROUND` |  |
| `--syn-comment-style` | `normal` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_LINE_COMMENT` | No italic FONT_TYPE; use normal. |
| `--syn-doc-comment` | `#629755` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_COMMENT/FOREGROUND` |  |
| `--syn-doc-comment-tag` | `#629755` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_COMMENT_TAG/FOREGROUND` |  |
| `--syn-doc-comment-tag-effect` | `underline` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_COMMENT_TAG/EFFECT_TYPE=1` |  |
| `--syn-doc-comment-tag-value` | `#8a653b` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_COMMENT_TAG_VALUE/FOREGROUND` |  |
| `--syn-doc-markup` | `#77b767` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_MARKUP/FOREGROUND` |  |
| `--syn-doc-markup-bg` | `transparent` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_MARKUP/BACKGROUND(empty)` | Explicitly cleared in source. |
| `--syn-docstring` | `#629755` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_DOC_COMMENT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-annotation` | `#bbb529` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_METADATA/FOREGROUND` |  |
| `--syn-decorator` | `#bbb529` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_METADATA/FOREGROUND` |  |
| `--syn-number` | `#6897bb` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_NUMBER/FOREGROUND` |  |
| `--syn-punct` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-variable` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-global` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-namespace` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-param` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-property` | `#9876aa` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_INSTANCE_FIELD/FOREGROUND` |  |
| `--syn-constant` | `#9876aa` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_CONSTANT/FOREGROUND` |  |
| `--syn-python-local-variable` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-global-variable` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-instance-attribute` | `#9876aa` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_INSTANCE_FIELD/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-class-attribute` | `#9876aa` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_STATIC_FIELD/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-constant` | `#9876aa` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_CONSTANT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-property` | `#9876aa` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_INSTANCE_FIELD/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-type-parameter` | `#507874` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TYPE_PARAMETER_NAME_ATTRIBUTES/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-builtin` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-predefined-definition` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-predefined-usage` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-fstring` | `#6a8759` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_STRING/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-python-bytes` | `#6a8759` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_STRING/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-php-variable` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-php-function-call` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-builtin` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-self` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-keyword-arg` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-predefined` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-escape` | `#cc7832` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_VALID_STRING_ESCAPE/FOREGROUND` |  |
| `--syn-regexp` | `#6a8759` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_STRING/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-tag` | `#e8bf6a` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/XML_TAG_NAME/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-attribute` | `#bababa` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/XML_ATTRIBUTE_NAME/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-todo` | `#a8c023` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TODO_DEFAULT_ATTRIBUTES/FOREGROUND` |  |
| `--syn-link` | `#589df6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CTRL_CLICKABLE/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-markup-heading` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-markup-code` | `#6a8759` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEFAULT_STRING/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-invalid` | `#ff0000` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/BAD_CHARACTER/EFFECT_COLOR` | Host invalid text foreground uses IDEA's box/effect color. |
| `--syn-inline-value` | `#666d75` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/DEBUGGER_INLINED_VALUES/FOREGROUND` |  |
| `--syn-rainbow-1` | `#529d52` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/RAINBOW_COLOR0/FOREGROUND` | Corrected zero-based source index; not bracket colors. |
| `--syn-rainbow-2` | `#be7070` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/RAINBOW_COLOR1/FOREGROUND` | Corrected zero-based source index; not bracket colors. |
| `--syn-rainbow-3` | `#3d7676` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/RAINBOW_COLOR2/FOREGROUND` | Corrected zero-based source index; not bracket colors. |
| `--syn-rainbow-4` | `#be9970` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/RAINBOW_COLOR3/FOREGROUND` | Corrected zero-based source index; not bracket colors. |
| `--syn-rainbow-5` | `#9d527c` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/RAINBOW_COLOR4/FOREGROUND` | Corrected zero-based source index; not bracket colors. |
| `--syn-bracket-1` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-bracket-2` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--syn-bracket-3` | `#a9b7c6` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` | Shared host syntax category; language fallback/semantic scopes need visual calibration. |
| `--fg-editor` | `#a9b7c6` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/FOREGROUND` |  |
| `--caret` | `#bbbbbb` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/CARET_COLOR` |  |
| `--fg-line-number` | `#606366` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/LINE_NUMBERS_COLOR` |  |
| `--fg-line-number-current` | `#a4a3a3` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/LINE_NUMBER_ON_CARET_ROW_COLOR` |  |
| `--border-gutter` | `#2b2b2b` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/BACKGROUND` | No separate gutter border in source; merge into editor surface. |
| `--border-indent-guide` | `#373737` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/INDENT_GUIDE` |  |
| `--border-indent-guide-active` | `#505050` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/SELECTED_INDENT_GUIDE` |  |
| `--border-right-margin` | `#4d4d4d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/RIGHT_MARGIN_COLOR` |  |
| `--bg-editor-selection` | `#214283` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/SELECTION_BACKGROUND` |  |
| `--bg-editor-selection-inactive` | `#4c4f56` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/SELECTION_BACKGROUND_INACTIVE` |  |
| `--bg-text-search-result` | `#32593d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT_SEARCH_RESULT_ATTRIBUTES/BACKGROUND` |  |
| `--bg-text-search-result-current` | `#32593d` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT_SEARCH_RESULT_ATTRIBUTES/BACKGROUND` | No separate active occurrence background available. |
| `--bg-matched-brace` | `#3b514d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/MATCHED_BRACE_ATTRIBUTES/BACKGROUND` |  |
| `--matched-brace-weight` | `700` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/MATCHED_BRACE_ATTRIBUTES/FONT_TYPE=1` |  |
| `--bg-matched-tag` | `#3b514d` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/MATCHED_BRACE_ATTRIBUTES/BACKGROUND` | Host shares brace and tag match surfaces. |
| `--bg-fold-placeholder` | `#3a3a3a` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/FOLDED_TEXT_ATTRIBUTES/BACKGROUND` |  |
| `--fg-fold-placeholder` | `#8c8c8c` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/FOLDED_TEXT_ATTRIBUTES/FOREGROUND` |  |
| `--fg-fold-marker` | `#555555` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/TEARLINE_COLOR` |  |
| `--fg-whitespace` | `#606060` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/WHITESPACES` |  |
| `--fg-unused` | `#72737a` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/NOT_USED_ELEMENT_ATTRIBUTES/FOREGROUND` |  |
| `--bg-identifier-under-caret` | `#344134` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/IDENTIFIER_UNDER_CARET_ATTRIBUTES/BACKGROUND` |  |
| `--bg-identifier-under-caret-write` | `#40332b` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/WRITE_IDENTIFIER_UNDER_CARET_ATTRIBUTES/BACKGROUND` |  |
| `--fg-inlay` | `#787878` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/INLINE_PARAMETER_HINT/FOREGROUND` |  |
| `--bg-inlay` | `#3b3b3b` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/INLINE_PARAMETER_HINT/BACKGROUND` |  |
| `--wave-error` | `#bc3f3c` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/ERRORS_ATTRIBUTES/EFFECT_COLOR` |  |
| `--wave-warning` | `#be9117` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/WARNING_ATTRIBUTES/ERROR_STRIPE_COLOR` | Source warning has background/stripe but no EFFECT_COLOR; use stripe for host wave. |
| `--editor-error-decoration` | `underline wavy var(--wave-error)` | derived | `derived` · `--wave-error` | Host renders IDEA diagnostic effects as CSS decorations. |
| `--editor-warning-decoration` | `underline wavy var(--wave-warning)` | derived | `derived` · `--wave-warning` | Host renders IDEA diagnostic effects as CSS decorations. |
| `--editor-warning-background` | `#52503a` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/WARNING_ATTRIBUTES/BACKGROUND` |  |
| `--bg-breakpoint-line` | `#3a2323` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/BREAKPOINT_ATTRIBUTES/BACKGROUND` |  |
| `--fg-completion-match` | `#548af7` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.CompletionPopup.matchForeground` |  |
| `--bg-editor-inline` | `var(--bg-editor)` | derived | `derived` · `--bg-editor` | Same host role / shared palette. |
| `--bg-editor-banner` | `#1d3857` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/NOTIFICATION_BACKGROUND` |  |
| `--fg-weak-warning` | `#72737a` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/NOT_USED_ELEMENT_ATTRIBUTES/FOREGROUND` | No equivalent weak-warning foreground mapped. |
| `--fg-bulb` | `#ba9752` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Label.warningForeground` | Host bulb uses warning UI foreground. |
| `--ansi-black` | `#000000` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_BLACK_OUTPUT/FOREGROUND` |  |
| `--ansi-red` | `#f0524f` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_RED_OUTPUT/FOREGROUND` |  |
| `--ansi-green` | `#5c962c` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_GREEN_OUTPUT/FOREGROUND` |  |
| `--ansi-yellow` | `#a68a0d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_YELLOW_OUTPUT/FOREGROUND` |  |
| `--ansi-blue` | `#3993d4` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_BLUE_OUTPUT/FOREGROUND` |  |
| `--ansi-magenta` | `#a771bf` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_MAGENTA_OUTPUT/FOREGROUND` |  |
| `--ansi-cyan` | `#00a3a3` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_CYAN_OUTPUT/FOREGROUND` |  |
| `--ansi-white` | `#808080` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_GRAY_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-black` | `#595959` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_DARKGRAY_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-red` | `#ff4050` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_RED_BRIGHT_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-green` | `#4fc414` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_GREEN_BRIGHT_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-yellow` | `#e5bf00` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_YELLOW_BRIGHT_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-blue` | `#1fb0ff` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_BLUE_BRIGHT_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-magenta` | `#ed7eed` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_MAGENTA_BRIGHT_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-cyan` | `#00e5e5` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_CYAN_BRIGHT_OUTPUT/FOREGROUND` |  |
| `--ansi-bright-white` | `#ffffff` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/CONSOLE_WHITE_OUTPUT/FOREGROUND` |  |
| `--terminal-ansi-black` | `var(--ansi-black)` | derived | `derived` · `--ansi-black` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-red` | `var(--ansi-red)` | derived | `derived` · `--ansi-red` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-green` | `var(--ansi-green)` | derived | `derived` · `--ansi-green` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-yellow` | `var(--ansi-yellow)` | derived | `derived` · `--ansi-yellow` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-blue` | `var(--ansi-blue)` | derived | `derived` · `--ansi-blue` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-magenta` | `var(--ansi-magenta)` | derived | `derived` · `--ansi-magenta` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-cyan` | `var(--ansi-cyan)` | derived | `derived` · `--ansi-cyan` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-white` | `var(--ansi-white)` | derived | `derived` · `--ansi-white` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-black` | `var(--ansi-bright-black)` | derived | `derived` · `--ansi-bright-black` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-red` | `var(--ansi-bright-red)` | derived | `derived` · `--ansi-bright-red` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-green` | `var(--ansi-bright-green)` | derived | `derived` · `--ansi-bright-green` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-yellow` | `var(--ansi-bright-yellow)` | derived | `derived` · `--ansi-bright-yellow` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-blue` | `var(--ansi-bright-blue)` | derived | `derived` · `--ansi-bright-blue` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-magenta` | `var(--ansi-bright-magenta)` | derived | `derived` · `--ansi-bright-magenta` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-cyan` | `var(--ansi-bright-cyan)` | derived | `derived` · `--ansi-bright-cyan` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--terminal-ansi-bright-white` | `var(--ansi-bright-white)` | derived | `derived` · `--ansi-bright-white` | Classic Darcula console palette; new block-terminal palette is intentionally separate upstream. |
| `--shadow-popup` | `0 6px 20px rgba(0, 0, 0, 0.45)` | host-fallback | `sources/openidea-token-groups.json` · `--shadow-popup` | Inherits Islands Dark; no verified equivalent mapped. |
| `--shadow-dialog` | `0 0 0 0.5px rgba(0, 0, 0, 0.6), 0 10px 24px rgba(0, 0, 0, 0.35), 0 24px 72px rgba(0, 0, 0, 0.45)` | host-fallback | `sources/openidea-token-groups.json` · `--shadow-dialog` | Inherits Islands Dark; no verified equivalent mapped. |
| `--traffic-close` | `#ff5f57` | host-fallback | `sources/openidea-token-groups.json` · `--traffic-close` | Inherits Islands Dark; no verified equivalent mapped. |
| `--traffic-close-border` | `#e0443e` | host-fallback | `sources/openidea-token-groups.json` · `--traffic-close-border` | Inherits Islands Dark; no verified equivalent mapped. |
| `--traffic-close-pressed` | `#bf4942` | host-fallback | `sources/openidea-token-groups.json` · `--traffic-close-pressed` | Inherits Islands Dark; no verified equivalent mapped. |
| `--traffic-glyph` | `#4d0000` | host-fallback | `sources/openidea-token-groups.json` · `--traffic-glyph` | Inherits Islands Dark; no verified equivalent mapped. |
| `--traffic-off` | `#4b4c4f` | host-fallback | `sources/openidea-token-groups.json` · `--traffic-off` | Inherits Islands Dark; no verified equivalent mapped. |
| `--traffic-off-border` | `#404144` | host-fallback | `sources/openidea-token-groups.json` · `--traffic-off-border` | Inherits Islands Dark; no verified equivalent mapped. |
| `--bg-stripe-tooltip` | `var(--bg-tooltip)` | derived | `derived` · `--bg-tooltip` | Same host role / shared palette. |
| `--fg-stripe-tooltip` | `var(--fg-tooltip)` | derived | `derived` · `--fg-tooltip` | Same host role / shared palette. |
| `--border-stripe-tooltip` | `var(--border-tooltip)` | derived | `derived` · `--border-tooltip` | Same host role / shared palette. |
| `--shadow-stripe-tooltip` | `var(--shadow-tooltip)` | derived | `derived` · `--shadow-tooltip` | Same host role / shared palette. |
| `--bg-tooltip` | `#4b4d4d` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ToolTip.background` |  |
| `--fg-tooltip` | `#bfbfbf` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ToolTip.foreground` |  |
| `--border-tooltip` | `#616161` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ToolTip.borderColor` |  |
| `--bg-control` | `#4c5052` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.startBackground` |  |
| `--bg-control-hover` | `#ffffff26` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.ActionButton.pressedBackground` |  |
| `--bg-active` | `#ffffff26` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.ActionButton.pressedBackground` |  |
| `--bg-scrim` | `rgba(0, 0, 0, 0.45)` | host-fallback | `sources/openidea-token-groups.json` · `--bg-scrim` | Inherits Islands Dark; no verified equivalent mapped. |
| `--fg-on-accent` | `#bbbbbb` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.default.foreground` |  |
| `--shadow-tooltip` | `0 4px 12px rgba(0, 0, 0, 0.4)` | host-fallback | `sources/openidea-token-groups.json` · `--shadow-tooltip` | Inherits Islands Dark; no verified equivalent mapped. |
| `--shadow-balloon` | `0 8px 24px rgba(0, 0, 0, 0.45)` | host-fallback | `sources/openidea-token-groups.json` · `--shadow-balloon` | Inherits Islands Dark; no verified equivalent mapped. |
| `--bg-frame` | `#3c3f41` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.MainWindow.background` |  |
| `--bg-island` | `#2b2b2b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ToolWindow.background` |  |
| `--bg-stripe-hover` | `#ffffff12` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.MainToolbar.Dropdown.transparentHoverBackground` |  |
| `--bg-stripe-selected` | `#3574f0` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.ToolWindow.Button.selectedBackground` |  |
| `--fg-stripe-selected-active` | `#ffffff` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.ToolWindow.Button.selectedForeground` |  |
| `--fg-stripe-label` | `#9da0a8` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ToolWindow.Button.foreground` |  |
| `--bg-tab-selected` | `#2b405a` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.EditorTabs.underlinedTabBackground` |  |
| `--border-tab-selected` | `#385475` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.EditorTabs.underlinedBorderColor` |  |
| `--bg-tab-selected-inactive` | `#35393b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.EditorTabs.inactiveUnderlinedTabBackground` |  |
| `--border-tab-selected-inactive` | `#454a4d` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.EditorTabs.inactiveUnderlinedTabBorderColor` |  |
| `--bg-tab-hover` | `#35393b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.EditorTabs.hoverBackground` |  |
| `--border-editor-tabs` | `#3c3f41` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.EditorTabs.underTabsBorderColor` |  |
| `--bg-tree-selected` | `#304c80` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.selectionBackground` |  |
| `--bg-tree-selected-inactive` | `#474a4d` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.selectionInactiveBackground` |  |
| `--bg-tree-hover` | `#393b40` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.*.hoverBackground` |  |
| `--bg-toolbar-hover` | `#ffffff12` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ActionButton.hoverBackground` |  |
| `--bg-toolbar-pressed` | `#ffffff26` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.ActionButton.pressedBackground` |  |
| `--bg-toolbar-selected` | `#304c80` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.SelectionActive` | Reuses verified palette for a different host control/state. |
| `--bg-toolbar-selected-hover` | `#304c80` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.SelectionActiveLight` | Reuses verified palette for a different host control/state. |
| `--bg-button-primary-hover` | `#366799` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.ComponentBorderFocus` | Reuses verified palette for a different host control/state. |
| `--fg-button-primary` | `#bbbbbb` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.default.foreground` |  |
| `--bg-button` | `#4c5052` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.startBackground` |  |
| `--border-button` | `#5e6060` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Button.startBorderColor` |  |
| `--bg-field` | `#2b2b2b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.TextField.background` |  |
| `--bg-checkbox` | `#363738` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `icons.ColorPalette.Checkbox.Background.Default` |  |
| `--border-checkbox` | `#6b6b6b` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `icons.ColorPalette.Checkbox.Border.Default` |  |
| `--bg-toggle-on` | `#304c80` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.SelectionActive` | Reuses verified palette for a different host control/state. |
| `--fg-toggle-on` | `#bbbbbb` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.ForegroundDefault` | Reuses verified palette for a different host control/state. |
| `--bg-toggle-off` | `#2b2b2b` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.InputBackground` | Reuses verified palette for a different host control/state. |
| `--fg-toggle-off` | `#bbbbbb` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.ForegroundDefault` | Reuses verified palette for a different host control/state. |
| `--border-toggle` | `#5c5c5c` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.ComponentBorder` | Reuses verified palette for a different host control/state. |
| `--bg-toggle-knob` | `#bbbbbb` | approximation | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `colors.ForegroundDefault` | Reuses verified palette for a different host control/state. |
| `--focus-ring-soft` | `#366799` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Component.focusColor` |  |
| `--scrollbar-thumb` | `#80808059` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ScrollBar.thumbColor` |  |
| `--scrollbar-thumb-hover` | `#8080808c` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.ScrollBar.hoverThumbColor` |  |
| `--bg-search-match` | `#155221` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/SEARCH_RESULT_ATTRIBUTES/BACKGROUND` |  |
| `--bg-search-match-current` | `var(--bg-search-match)` | derived | `derived` · `--bg-search-match` | Same host role / shared palette. |
| `--fg-search-match` | `var(--fg-editor)` | derived | `derived` · `--fg-editor` | Same host role / shared palette. |
| `--bg-dialog` | `var(--bg-app)` | derived | `derived` · `--bg-app` | Same host role / shared palette. |
| `--bg-popup-inline` | `var(--bg-popup)` | derived | `derived` · `--bg-popup` | Same host role / shared palette. |
| `--bg-popup-advertiser` | `#333333` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Popup.Advertiser.background` |  |
| `--bg-feedback-info` | `#25324d` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `colors.Blue1` | No one-to-one banner key; verified blue status palette. |
| `--border-feedback-info` | `#35538f` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `colors.Blue3` | No one-to-one banner key; verified blue status palette. |
| `--bg-feedback-error` | `#402929` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Editor.ToolTip.errorBackground` | Editor tooltip status palette projected onto host banners. |
| `--border-feedback-error` | `#472b2b` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Editor.ToolTip.errorBorder` | Editor tooltip status palette projected onto host banners. |
| `--bg-feedback-warning` | `#3d3223` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Editor.ToolTip.warningBackground` | Editor tooltip status palette projected onto host banners. |
| `--border-feedback-warning` | `#5e4d33` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Editor.ToolTip.warningBorder` | Editor tooltip status palette projected onto host banners. |
| `--bg-feedback-success` | `#253627` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Editor.ToolTip.successBackground` | Editor tooltip status palette projected onto host banners. |
| `--border-feedback-success` | `#273828` | approximation | `sources/jetbrains/expUI_dark.theme.json` · `ui.Editor.ToolTip.successBorder` | Editor tooltip status palette projected onto host banners. |
| `--bg-counter` | `#868a91` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Counter.background` |  |
| `--fg-counter` | `#000000` | mapped | `sources/jetbrains/ManyIslandsDarcula.theme.json` · `ui.Counter.foreground` |  |
| `--bg-progress-track` | `#43454a` | mapped | `sources/jetbrains/expUI_dark.theme.json` · `ui.ProgressBar.trackColor` |  |
| `--border-method-separator` | `#4d4d4d` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/colors/METHOD_SEPARATORS_COLOR` |  |
| `--bg-editor` | `#2b2b2b` | mapped | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/BACKGROUND` |  |
| `--bg-editor-gutter` | `#2b2b2b` | approximation | `sources/jetbrains/DefaultColorSchemesManager.xml` · `Darcula/attributes/TEXT/BACKGROUND` | Converter uses editor background in new UI when EDITOR_GUTTER_BACKGROUND is absent; classic GUTTER_BACKGROUND is not used. |
