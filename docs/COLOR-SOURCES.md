# 颜色来源与还原边界

取证日期：2026-11-10。**目标为 IDEA 内置 Islands Darcula UI + 当前实际搭配的 Darcula Editor Scheme。** UI Theme 与 Editor Scheme 分别处理，不使用 OpenIDEA Islands Dark 或第三方 Dracula 作为目标调色板。

## 已核验的基准

本机 IntelliJ IDEA **2026.2.3 / IU-262.10968.63**：`options/laf.xml` 为 `themeId="Islands Darcula"`，`options/colors.scheme.xml` 为 `_@user_Darcula`。用户 `.icls` 的父方案是 `Darcula`，只清空了 `INJECTED_LANGUAGE_FRAGMENT`；它没有完整颜色。未将该文件误称为完整官方导出，也未将用户路径和个人配置打包。

从安装包 `Contents/lib/intellij.platform.ide.impl.jar` 只读检查以下资源，并从公开 IntelliJ Community tag `idea/262.10968.63` 取得同名文件；**四个文件逐字节一致**。本仓库保存的是这些公开源文件，不是伪造的 `.icls` 导出。

| 资源 | 作用 |
| --- | --- |
| `themes/islands/ManyIslandsDarcula.theme.json` | 目标 UI，`parentTheme=ExperimentalDark`、`editorScheme=Darcula` |
| `themes/expUI/expUI_dark.theme.json` | UI 父主题，`parentTheme=Darcula`，补齐命名色与控件状态 |
| `themes/darcula.theme.json` | UI 祖先主题，普通文本、链接及基础控件参考 |
| `DefaultColorSchemesManager.xml` | 完整内置 `Darcula → Default` 编辑器方案；解析具体颜色及属性 |

公开源码锁定 commit **`8062c061ff33e22041d9f1844db5b8b8a6b5e4d7`**，文件链接与 SHA-256 见 [UPSTREAM.json](../sources/UPSTREAM.json)。核心 UI 文件 SHA-256 为 `ffb56c08de03c434cacffeaaa0ac3a634d4b744c95bb3265a0bea5bc0fb5c9fd`。

官方产品说明：[User interface themes](https://www.jetbrains.com/help/idea/user-interface-themes.html)。它用于确认主题定位；不作为具体颜色数值来源。

**核验层级：源码资源和本机配置已核验；Swing 最终 UI 默认值、插件覆盖、操作系统渲染及屏幕取色没有因此自动获得验证。** 尚未完成 IDEA 与 OpenIDEA 在同工作区、同缩放下的实机截图对照。

## 关键映射

以下键均可在随仓库固定的公开资源中复核。`mapped` 表示保留源数值并映射角色，不能读作“所有平台精确视觉相同”。

| OpenIDEA Token | 值 | 来源键 / 说明 |
| --- | --- | --- |
| `--bg-app` / `--bg-island` / `--bg-elev` | `#2b2b2b` | 目标 UI `*.background → PanelBackground`、`ToolWindow.background → ToolWindowBackground` |
| `--bg-frame` | `#3c3f41` | `MainWindow.background`；MainToolbar、Stripe、StatusBar 同层次 |
| `--bg-popup` | `#333333` | `Popup.background → PopupBackground` |
| `--bg-tooltip` / `--border-tooltip` | `#4b4d4d` / `#616161` | `ToolTip.background` / `ToolTip.borderColor` |
| `--fg` / `--fg-secondary` | `#bbbbbb` / `#828282` | `Label.foreground` / `Label.infoForeground` |
| `--border` / `--border-strong` | `#404040` / `#5c5c5c` | `Borders.color → BorderDark` / `Component.borderColor → ComponentBorder` |
| `--bg-tree-selected` / inactive | `#304c80` / `#474a4d` | 目标 UI `*.selectionBackground` / `*.selectionInactiveBackground` |
| `--bg-tab-selected` / border | `#2b405a` / `#385475` | `EditorTabs.underlinedTabBackground` / `underlinedBorderColor` |
| inactive tab / border | `#35393b` / `#454a4d` | `EditorTabs.inactiveUnderlinedTabBackground` / `inactiveUnderlinedTabBorderColor` |
| `--bg-input` / `--bg-field` | `#2b2b2b` | `TextField.background → InputBackground` |
| `--bg-editor` / `--fg-editor` | `#2b2b2b` / `#a9b7c6` | Darcula `TEXT.BACKGROUND` / `TEXT.FOREGROUND` |
| `--syn-keyword` / string / number | `#cc7832` / `#6a8759` / `#6897bb` | `DEFAULT_KEYWORD` / `DEFAULT_STRING` / `DEFAULT_NUMBER` foreground |
| `--syn-comment` / doc comment | `#808080` / `#629755` | `DEFAULT_LINE_COMMENT` / `DEFAULT_DOC_COMMENT` foreground |
| `--syn-function` / property | `#ffc66d` / `#9876aa` | `DEFAULT_FUNCTION_DECLARATION` / `DEFAULT_INSTANCE_FIELD` foreground |
| `--caret` / `--bg-current-line` | `#bbbbbb` / `#323232` | `CARET_COLOR` / `CARET_ROW_COLOR` |
| editor selection / inactive | `#214283` / `#4c4f56` | `SELECTION_BACKGROUND` / `SELECTION_BACKGROUND_INACTIVE` |
| line number / current | `#606366` / `#a4a3a3` | `LINE_NUMBERS_COLOR` / `LINE_NUMBER_ON_CARET_ROW_COLOR` |
| error / warning wave | `#bc3f3c` / `#be9117` | `ERRORS_ATTRIBUTES.EFFECT_COLOR`；warning 借用 `WARNING_ATTRIBUTES.ERROR_STRIPE_COLOR`，**approximation** |
| warning background | `#52503a` | `WARNING_ATTRIBUTES.BACKGROUND` |
| Diff modified / added / deleted | `#385570` / `#294436` / `#484a4a` | `DIFF_MODIFIED` / `DIFF_INSERTED` / `DIFF_DELETED` background |
| VCS modified / added | `#6897bb` / `#629755` | `FILESTATUS_MODIFIED` / `FILESTATUS_ADDED` |
| terminal normal / bright white | `#808080` / `#ffffff` | `CONSOLE_GRAY_OUTPUT` / `CONSOLE_WHITE_OUTPUT`；16 色来自 Darcula classic console |

完整 **255 项账本**见 [TOKEN-MAPPING.md](TOKEN-MAPPING.md)，包含 241 个输出 Token 与 14 个宿主继承项。机器可读记录逐项保存数值、状态、来源文件、键和近似理由；验证脚本检查生成结果与账本一致。

## 近似与继承

- 61 项 `approximation`：源码原值用于另一个宿主角色，并非随机虚构。主要是类型/普通变量/函数调用语义分类、Python/PHP、Markdown、正则、共享括号、Toggle 状态、反馈 Banner、弱警告、当前搜索项和 gutter 分隔。
- `DEFAULT_CLASS_NAME` 等在原始 Darcula 方案缺失，不能仅依据稀疏用户导出或 Default 的亮色属性推断。使用明确的 Darcula `TEXT` 或同类属性作保守映射，并标近似；未声称已复原所有 TextAttributesKey fallback 链或语言插件叠加。
- warning 没有 `EFFECT_COLOR`，保留原背景并将条纹色投射为波浪线。`BAD_CHARACTER` 同样将效果色投射到宿主的 invalid foreground。
- 宿主 UI/编辑器共用 `--bg-search-match`，本版优先 Darcula 编辑器 `SEARCH_RESULT_ATTRIBUTES` 的绿色；IDEA UI 的 `SearchMatch` 金黄色无法同时独立呈现。匹配括号的源 foreground/effect 与各语法属性的粗斜体也没有全部独立宿主 Token。
- 彩虹标识符正确按源 `RAINBOW_COLOR0…4` 映射到宿主 `1…5`；宿主彩虹括号单独使用普通文本色，避免误用标识符调色板。
- 27 项 `derived`：CSS 别名、同色面板及波浪线表达式。终端采用 classic console ANSI；IDEA 的新 block terminal 有另一套 palette，本版不宣称复刻它。
- 新 UI `EDITOR_GUTTER_BACKGROUND` 缺失时遵循官方转换器采用编辑区背景，未将 classic `GUTTER_BACKGROUND=#313335` 强行套入。标记为需要实机校准的近似。
- 14 项 `host-fallback`：`--chart-series`、`--db-connected`、`--db-connected-ring`、`--shadow-popup`、`--shadow-dialog`、`--traffic-close`、`--traffic-close-border`、`--traffic-close-pressed`、`--traffic-glyph`、`--traffic-off`、`--traffic-off-border`、`--bg-scrim`、`--shadow-tooltip`、`--shadow-balloon`。这些值没有写入插件，继续继承 Islands Dark。
- 未覆盖的 metrics、字体、布局、渲染实现和其他派生 Token 均沿用宿主。派生的 editor surfaces、coverage 等会引用本插件设置的基础颜色；没有宣称逐一复刻其 Swing 对应物。

## 第三方参考与优先级

Gerry 的 [islands-darcula](https://github.com/gerry-themes/islands-darcula/tree/f15cd3c5a948a14e71ebcf6587dee9803f641cd3) 是 Apache-2.0 **第三方少量 UI 覆盖**。已读取其 `islandsDarcula.theme.json` 与 `license`，保存原始参考并保留归属。`ToolWindow.background=#2b2b2b`、`ToolWindow.Stripe.background=#3c3f41` 与官方资源一致。

已运行 OpenIDEA 官方转换器，以该第三方文件及从完整内置资源提取的 Darcula 节点生成临时初稿，得到 **2 UI + 81 editor** Token。最终实现以已核验的 JetBrains 内置资源为准；例如第三方边框覆盖 `#3c3f41` 不替代官方 `BorderDark=#404040`。第三方文件不被描述为官方内置主题导出。

宿主 API 与格式锁定 [OpenIDEA v0.1.40](https://github.com/l0ng-ai/openidea/tree/v0.1.40)，commit `37c2a6048eea89d4f6db645622612358b643862b`。官方 `harbor-night` 用于结构和覆盖分类；`intellijTheme.ts` 的映射表用于生成初稿；`tokens.css` 用于识别有效 Token。宿主色彩仅用于已记录的 fallback。
