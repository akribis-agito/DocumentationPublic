---
keyword: FIFORemove
summary: 命令函数，用于移除最近压入 FIFO 运动队列的条目。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 289
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# FIFORemove

命令函数，用于移除最近压入 FIFO 运动队列的条目。

## 概述

`FIFORemove` 从 FIFO 运动队列的末尾移除最近压入的条目——即最后一次由 `FIFOPush*` 函数添加的条目。它用于在条目被回放前将其丢弃，而不影响队列中的其余条目。若要一次性清空整个队列，请使用 [FIFOClear](FIFOClear.md)。与 `FIFOClear` 不同，`FIFORemove` 可在 FIFO 运动过程中执行。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

一次移除操作释放队列末尾的一个条目，并递增 [FIFOStatus](FIFOStatus.md)（索引 2）报告的空闲条目计数。若队列已为空，则该操作无效。

在 FIFO 运动激活期间，当前正在回放的条目不可被移除：若队列中仅剩该一个段，则移除操作将被忽略。这是为了保护正在执行的段。当轴未在运行 FIFO 运动时，只要队列中至少有一个条目，末尾条目即可被移除。

## 示例

```text
AFIFORemove          ; discard the most recently pushed entry
```

## 另请参阅

- [FIFOClear](FIFOClear.md) — 清空整个 FIFO
- [FIFOStatus](FIFOStatus.md) — FIFO 队列状态
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
