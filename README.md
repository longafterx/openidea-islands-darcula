# OpenIDEA Islands Darcula

面向 **OpenIDEA v0.1.40 / Plugin API 1.4** 的纯配置深色主题插件，版本 `0.1.0`，插件 ID 为 `longafter.islands-darcula`。

目标是 IntelliJ IDEA **内置 Islands Darcula** 的低对比度界面，配套 **Darcula 编辑器方案**。已读取本机 IDEA 2026.2.3 的实际配置，并与 IntelliJ Community 同版本源码逐字节核对核心资源。UI 与编辑器方案是两个独立设置；这份插件同时提供两者。

当前包含 111 个 UI Token、130 个编辑器 Token：153 项使用已核验来源的映射、61 项明确标为近似、27 项为派生表达；另有 14 项沿用宿主默认值。保留 OpenIDEA 的 Islands 布局、间距、圆角和字体设置。没有 Rust、WASM、权限声明、网络访问或运行时依赖。

## 安装与启用

1. 在 OpenIDEA 0.1.40 打开 **Settings → Plugins → ⚙ → Install Plugin from Disk…**，选择本项目根目录（包含 `plugin.toml`）。也可用 **Install Plugin from Package File…** 选择本地生成的 `.oiplugin`；若该入口提供文件过滤，可先选择 `plugin.toml`。
2. 确认插件 **Islands Darcula** 已启用。
3. 打开 **Settings → Appearance → Theme**，选择 **Islands Darcula**。也可在插件详情页对主题点 **Apply**。
4. 将 **Accent Color** 恢复默认。在 **Settings → Editor → Color Scheme** 使用随当前主题提供的方案，清除会覆盖主题的显式 Scheme/Attribute Overrides；不要同时选用另一套独立编辑器方案。
5. 切换到其他主题，再切回，检查代码、选区和工具窗口。

**卸载/禁用：** 先在 Appearance 切回内置 Islands Dark，再到 Plugins 禁用或卸载本插件；主题不可用时宿主也会回退到其内置 dark 基础主题。安装后不需要编译，不依赖开发机器的任何绝对路径。

插件使用 `longafter` 命名空间。当前为可从源码目录本地安装的初版，尚未注册到社区 Marketplace，也未提供签名 Release。

## 校验与本地打包

基础校验只需 Python 3.11+（标准库）：

```sh
python3 scripts/validate.py
```

编辑 `scripts/generate.py` 中的映射并重新生成：

```sh
python3 scripts/generate.py
python3 scripts/validate.py
```

官方 CLI 应锁定宿主版本：

```sh
cargo install --locked --git https://github.com/l0ng-ai/openidea --tag v0.1.40 ide-host --bin openidea-plugin
openidea-plugin --version
openidea-plugin check .
mkdir -p dist
openidea-plugin pack . --out dist/longafter.islands-darcula-0.1.0.oiplugin
openidea-plugin check dist/longafter.islands-darcula-0.1.0.oiplugin
```

不传 `--key` / `--publisher` 即为本地未签名包。CLI 自带的打包规则只装入 manifest 引用文件及根目录 README / LICENSE / NOTICE；颜色来源、生成脚本和校验脚本保留在源码仓库。插件运行只需 `plugin.toml` 和 `themes/` 下两个 JSONC 文件，分发时同时保留 LICENSE 和 NOTICE。

## 颜色来源

- [颜色来源和还原边界](docs/COLOR-SOURCES.md)，[逐 Token 明细](docs/TOKEN-MAPPING.md)，[机器可读溯源](sources/token-provenance.json)。
- [固定的上游资源](sources/README.md)及其[版本、公开路径和 SHA-256](sources/UPSTREAM.json)。

## 验证与已知限制

已在 macOS aarch64 / OpenIDEA 0.1.40 上通过离线校验、官方 CLI 目录校验、打包和安装包校验；已实机验证磁盘安装、应用、内置主题切换、禁用回退和重新启用，以及 Go、JSON/XML、Markdown 预览和搜索弹窗。完整退出并重启 IDE 后，主题和配套编辑器配色自动恢复，原有项目窗口正常恢复。GUI 测试使用 MacBook 内置屏幕。

OpenIDEA 的语法分类及渲染器与 IDEA 不同。类型/函数调用、Python/PHP、Markdown、彩虹括号、警告波浪线及部分控件状态存在语义近似；源码颜色相同也不表示像素级一致。原生窗口效果、图表和数据库连接提示等 14 项继续继承 Islands Dark；派生覆盖、性能图表等会跟随它们引用的颜色 Token。

尚未完成卸载后重装、动态编辑器选区/光标、错误与警告、Completion、终端 ANSI 和 Git Diff 的完整验收。Windows/Linux 尚未实测；与运行中的 IDEA 在同工作区、同缩放下的截图对照也尚未完成。

**OpenIDEA 0.1.40 已知限制：** 禁用当前正在使用的主题时，宿主可能出现 `Could not apply theme / has no theme "islands-darcula"` 提示；本机补测的 10 轮快速 Disable/Enable 均复现，禁用后等待也可触发。重新启用后配色能恢复，但不能将此场景视为无错误通过。

**已验证的规避步骤：** 先点击 **Use Default Theme**（或在 Appearance 切回内置 Islands Dark），再禁用/启用插件；需要时重新 **Apply theme Islands Darcula**。按此步骤做的 5 轮快速切换均未出现主题错误。插件保持纯配置；该宿主生命周期问题未在本项目中修复。

Apache-2.0。原色彩资源归 JetBrains；另参考 Gerry 的第三方 Islands Darcula，并使用 OpenIDEA 官方主题示例和映射定义。详见 [第三方许可与修改声明](THIRD_PARTY_LICENSES.md) 和 [NOTICE](NOTICE)。本项目不隶属于 JetBrains 或 OpenIDEA。
