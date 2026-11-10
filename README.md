# Islands Darcula for OpenIDEA

<img src="icon.svg" width="80" height="80" alt="Islands Darcula logo">

将 IntelliJ IDEA 内置 **Islands Darcula** 的低对比度深色界面与 Darcula 编辑器配色带到 OpenIDEA。适用于 **OpenIDEA 0.1.40**（Plugin API 1.2+）。

## 主题特色

- 柔和的深灰界面，搭配 Darcula 橙色关键字、绿色字符串和紫色字段。
- 配套编辑器、弹窗、搜索、Diff、VCS 和终端 ANSI 配色。
- 保留 OpenIDEA 的 Islands 布局、间距与圆角；纯配置，无需 Rust/WASM 或额外权限。

## 安装

1. 从 [Releases](https://github.com/longafterx/openidea-islands-darcula/releases/latest) 下载 `.oiplugin` 安装包。
2. 在 **Settings → Plugins → ⚙ → Install Plugin from Package File…** 中选择该文件并安装。
3. 在 **Settings → Appearance → Theme** 选择 **Islands Darcula**，编辑器配色使用 **Theme default**。

社区插件市场收录后，也可在 **Settings → Plugins → Available** 搜索 **Islands Darcula** 安装。

## 必要说明

- 部分语法分类与控件颜色为近似移植，不承诺像素级一致。已在 macOS 验证，Windows/Linux 尚未实测。
- **禁用或卸载前，先切回内置 Islands Dark**，以规避 OpenIDEA 0.1.40 禁用当前主题时可能出现的“主题不可用”提示。
- Apache-2.0；原配色来自 JetBrains，另参考 Gerry 的主题。详见[颜色来源](docs/COLOR-SOURCES.md)、[第三方许可](THIRD_PARTY_LICENSES.md)和 [NOTICE](NOTICE)。本项目为社区移植。
