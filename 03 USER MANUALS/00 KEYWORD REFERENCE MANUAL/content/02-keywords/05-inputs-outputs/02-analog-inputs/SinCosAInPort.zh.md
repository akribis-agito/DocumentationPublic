---
keyword: SinCosAInPort
summary: 已移除——曾用于为 sin/cos（旋变）编码器反馈选择模拟端口。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# SinCosAInPort

已移除——曾用于为 sin/cos（旋变）编码器反馈选择模拟端口。

> **已在早期固件中移除。** `SinCosAInPort` 不再是受支持的关键字，
> 无法使用。本页保留用于参考较旧的固件和文档。

## 概述（历史）

`SinCosAInPort` 曾用于选择使用哪个模拟量输入端口来读取
旋变或 sin/cos 编码器反馈的正弦/余弦编码器信号。

当增加对专用 `SinCosSignals[1-6]` 关键字的支持时，它被移除；
sin/cos 反馈不再通过通用模拟量输入端口路由。
在当前固件上它不再是受支持的关键字。

## 另请参阅

- [AInPort](AInPort.md) — 模拟量输入读数
- [AInMode](AInMode.md) — 模拟量输入功能分配
