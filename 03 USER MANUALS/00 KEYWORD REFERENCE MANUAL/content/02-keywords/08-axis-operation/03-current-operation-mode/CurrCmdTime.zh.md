---
summary: 每条电流指令的指令时间，单位为毫秒。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CurrCmdTime

每条电流指令的指令时间，单位为毫秒。

## 概述

`CurrCmdTime` 是每条电流指令的指令时间，单位为毫秒。

> **已废弃 / 已被取代：** 本条目从 2021 版 PDF 参考手册导入。`CurrCmdTime` 在当前固件中不是受支持的关键字（无论是独立式/v4 还是 central-i v5）。电流运行模式中每个条目保持时间所对应的关键字是 [CurrCmdHTime](CurrCmdHTime.md)。请改用 [CurrCmdHTime](CurrCmdHTime.md)；保留本页仅为将遇到旧名称的用户重定向至该关键字。

## 另请参阅

- [CurrCmdHTime](CurrCmdHTime.md) — 每条电流指令条目所对应的、有文档记载的保持时间
- [Current operation mode](00-overview.md) — 电流模式关键字概述
