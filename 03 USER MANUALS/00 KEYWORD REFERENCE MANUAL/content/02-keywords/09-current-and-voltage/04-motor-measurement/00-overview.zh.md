# 电机测量

本子组保存由 PCSuite 电阻与电感工具测得的电机电气参数——电机电阻与电感，以及用于选择这些测量结果是以相数据还是线间数据报告的设置——同时还包含将外部/远程模拟电流检测输入转换为电机电流反馈的电流反馈比例因子。

- [Rm](Rm.md) — 测得的电机电阻（mΩ）。
- [Lm](Lm.md) — 测得的电机电感（µH）。
- [RLType](RLType.md) — 相数据与线间数据测量类型。
- [CurrFBFact](CurrFBFact.md) / [ExtCurrFBSca](ExtCurrFBSca.md) — 将外部/远程模拟电流检测输入转换为电机电流反馈的比例因子；CurrFBFact 为 v4 整数形式，ExtCurrFBSca 为 v5 浮点形式。
