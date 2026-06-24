---
summary: 对数字事件进行计数，并作为反馈记录历史数组的索引。
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# LockCntr/AuxLockCntr

对数字事件进行计数，并作为反馈记录历史数组的索引。

## 概述

`LockCntr` 跟踪自记录被武装以来捕获的触发事件数量，触发事件由 [LockSrc](LockSrc-AuxLockSrc.md) 定义。它同时充当历史数组 [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md)（及其 B 表）的运行索引。每次发生触发事件时，`LockCntr` 递增 1。`AuxLockCntr` 是其辅助编码器对应项。

当记录（[LockEn](LockEn-AuxLockEn.md)）从禁用状态被启用时，`LockCntr` 复位为 `0`。它是可写的，因此你可以预置它，使历史数组从所选索引处开始填充，或将其复位以从表的开头开始覆盖。

## 工作原理

每次触发事件发生时，固件首先递增 `LockCntr`，然后将捕获的位置（[LockVal](LockVal-AuxLockVal.md)）和已逝周期时间存入历史数组中索引为 `LockCntr` 的位置。由于计数器是预递增的，第一个事件落在索引 `1`（索引 `0` 未使用），这就是数组为 1 索引的原因。

### 表容量（取决于产品）

历史数组中可存储的事件数量取决于产品：

| 产品系列 | LockValTable / LockTimeTable | LockValTabB / LockTimeTabB | 可存储事件总数 |
|---|--:|--:|--:|
| Standalone | 50 | 50 | 100 |
| Central-i | 65000 | 65000 | 130000 |

当 `LockCntr` 处于第一个表的容量范围内时，事件存储在 [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) 中；一旦超出该范围，记录将继续存入 B 表（[LockValTabB](LockValTable-LockValTabB.md) / [LockTimeTabB](LockTimeTable-LockTimeTabB.md)）。一旦**两个**表都已存满，历史记录停止，但 `LockCntr` 和 [LockVal](LockVal-AuxLockVal.md) 在此后每个事件时仍继续更新——因此即使在缓冲区耗尽之后，计数器和最新捕获值仍保持实时有效。

`LockCntr` 本身是一个 32 位计数器，在任何实际运行中都不会回绕；受上述容量限制的是*表索引*。

### 每个控制周期记录一个事件

该计数器每个控制周期处理一次，且每个周期最多记录一个事件。如果在单个控制周期内发生多个触发边沿，硬件仅保留该周期中最近捕获的位置，且 `LockCntr` 恰好前进一个——同一周期内较早的边沿不会被单独计数或存储。要将每个边沿作为不同条目捕获，请使触发速率远低于每个控制周期一个事件（作为实用经验法则，低于每两个控制周期一个事件可为此时序限制留有余量）。超出该速率时，间隔很近的边沿会被合并为单个记录事件。

## 示例

```text
ALockCntr            ; read the number of events captured so far
ALockCntr=0          ; reset the history-array index (overwrite from the start)
```

## 另见

- [LockEn](LockEn-AuxLockEn.md) — 启用记录；将 `LockCntr` 复位为 0
- [LockSrc](LockSrc-AuxLockSrc.md) — 定义使 `LockCntr` 递增的触发事件
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — 以 `LockCntr` 为索引的历史数组
