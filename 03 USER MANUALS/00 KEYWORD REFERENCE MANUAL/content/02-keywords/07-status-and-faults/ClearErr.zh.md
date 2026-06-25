---
keyword: ClearErr
summary: 清除控制器错误日志（ErrLog）的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 236
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-27'
doc_revision: '2026.06'
language: zh-CN
---
# ClearErr

清除控制器错误日志（ErrLog）的命令。

## 概述

`ClearErr` 清空 [ErrLog](ErrLog.md) 数组，丢弃所有已记录的错误条目及其时间戳，并将日志的写入位置回退到 `ErrLog[1]`，使新记录的错误从干净的状态开始。请在查看或导出日志后使用它。

`ClearErr` 是一个非轴命令（它作用于整个单元范围的日志），且不接受任何值——发出该关键字即运行该命令。它不保存至闪存，可在任何时刻发出，包括在电机使能或运动中时。

## 工作原理

`ClearErr` **仅**清除错误日志：

1. 内部环形缓冲区的写入索引被重置到起始位置，因此清除期间发生的任何错误都会写入数组的最前端（随后也会被清除）。
2. `ErrLog` 的每个元素被置为 `0`。
3. 中断被短暂禁用，以清除在批量清除运行期间控制中断可能压入的任何条目，随后写入索引被再次重置。

它**不会**清除 [ConFlt](ConFlt.md)、[ConFltSnapVal](ConFltSnapVal.md) 或 [MotorReason](MotorReason.md)——它们反映的是当前故障状态，需单独清除（通过重新使能轴，或向 `ConFlt` 写入 `0`）。

## 示例

```text
AClearErr            ; clear all entries from the error log
```

## 另请参阅

- [ErrLog](ErrLog.md) — 本命令所清除的错误日志
- [ConFlt](ConFlt.md) — 每轴的故障码；正值会被追加到 ErrLog
- [ConFltSnapVal](ConFltSnapVal.md) — 故障快照，不受 ClearErr 影响
