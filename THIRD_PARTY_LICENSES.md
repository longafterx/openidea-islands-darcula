# 第三方许可与修改声明

本项目原创映射、脚本、文档及移植后的主题配置使用 Apache License 2.0；完整许可证见 [LICENSE](LICENSE)，归属与修改概要见 [NOTICE](NOTICE)。以下原始参考文件保留不变。

| 上游 | 固定版本 | 内容及用途 | 许可 |
| --- | --- | --- | --- |
| JetBrains / intellij-community | `idea/262.10968.63` / `8062c061ff33e22041d9f1844db5b8b8a6b5e4d7` | `sources/jetbrains/` 中的主题与编辑器颜色资源；最终颜色基准 | Apache-2.0 源码资源；保留 JetBrains NOTICE |
| l0ng-ai / openidea | `v0.1.40` / `37c2a6048eea89d4f6db645622612358b643862b` | 官方示例结构、Token 分类和转换器映射表；JSON 数据提取自源码 | Apache-2.0 |
| Gerry / islands-darcula | `f15cd3c5a948a14e71ebcf6587dee9803f641cd3` | `sources/gerry-islandsDarcula.theme.json` 原始第三方参考；项目 LICENSE 为其原始完整 Apache-2.0 文本 | Apache-2.0 |

JetBrains 原始归属：

```text
This software includes code from IntelliJ IDEA
Copyright (C) JetBrains s.r.o.
https://www.jetbrains.com/idea/
```

项目 NOTICE 保留此归属，并明确本项目复用的是颜色资源。JetBrains 对该版本仓库的根 `LICENSE.txt` 使用 Open-Source Build Terms，文中说明开源软件受 Apache-2.0 许可；原文保留于 [licenses/JetBrains-OPEN-SOURCE-BUILD-TERMS.txt](licenses/JetBrains-OPEN-SOURCE-BUILD-TERMS.txt) 供检查。本插件没有分发 IDEA 应用构建产物。

**显著修改声明：** `themes/islands-darcula.*.json` 为本项目生成的修改版移植，已在文件头标注。将 JetBrains UI 键和 editor attributes 映射为 OpenIDEA CSS Token，增加宿主角色近似和派生表达式；未声称其为 JetBrains 官方导出文件。第三方 Gerry JSON 仅用于对照和转换初稿，最终颜色优先遵循已核验的 JetBrains 资源；不同边框覆盖并未照搬。

没有复制或分发 JetBrains 商标图形、字体、图标、JAR 或专有可执行代码。产品名称仅用于说明兼容性及原资源来源。第三方项目中未发现独立 NOTICE；未编造其版权年份或授权范围。
