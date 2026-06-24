---
summary: 保留的每轴 CNC 分辨率比例关键字（当前固件未开放）。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAEncRatio/CNCBEncRatio

保留的每轴 CNC 分辨率比例关键字。当前固件未开放。

## 概述

`CNCAEncRatio` / `CNCBEncRatio` 原本用于描述某个 CNC 成员轴与其他轴之间的分辨率比例，以便在成员轴每单位计数不同的情况下保持 CNC 路径的几何精度。

> **当前固件不支持。** 现有固件（LTS v3.X.X 或 develop）均未将 `CNCAEncRatio` 或 `CNCBEncRatio` 作为关键字开放。请使用有理数对 [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) 实现等效的每轴 CNC 编码器缩放。

矢量运动的类似关键字 [VecEncRatio](../10-motion-mode-vector/VecEncRatio.md) 适用于 Vector 引擎；CNC 引擎则使用上述参数对。

## 另请参阅

- [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) / [CNCAEncFactDn/CNCBEncFactDn](CNCAEncFactDn-CNCBEncFactDn.md) — 实际应用于 CNC 路径的分子/分母形式
- [VecEncRatio](../10-motion-mode-vector/VecEncRatio.md) — Vector 引擎的类似关键字
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 队列段数据
