---
keyword: FIFOPushCycle
summary: 将周期时间（段持续时间）条目压入 FIFO 运动队列。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 284
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 65536000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# FIFOPushCycle

将周期时间（段持续时间）条目压入 FIFO 运动队列。

## 概述

`FIFOPushCycle` 将一个**周期时间**条目（[FIFOType](FIFOType.md) 中的类型 5）追加到队列末尾。该值为以控制周期数表示的段持续时间。控制器在回放时到达此条目后，会将其消耗而不产生运动：它更新 [FIFOCycleTime](FIFOCycleTime.md)，此后该值将应用于其后所有已排队的段，直到遇到下一个周期时间条目。这使得流式序列中的段长度可以变化。

它是用于在运动前或运动过程中填充队列的 `FIFOPush*` 函数之一。条目将被添加到队列末尾。若队列已满（无空闲条目），则该压入操作会被拒绝并返回错误 105，且不会添加任何内容。

队列头部也必须有一个周期时间条目：除非队列中的第一个条目是周期时间条目，否则无法启动 FIFO 运动。若在最旧的已排队条目不是周期时间条目的情况下尝试开始 FIFO 运动，该操作将被拒绝并返回错误 108。在任何运动段之前先压入一个 `FIFOPushCycle` 值，以确保队列以已定义的段持续时间开始。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

一次压入操作将提供的值写入下一个空闲队列槽，将其标记为周期时间条目，并递减 [FIFOStatus](FIFOStatus.md)（索引 2）报告的空闲条目计数。由于周期时间条目占用一个队列槽，大量交替使用会减少可用于运动段的槽位数量（总计 128 个可用槽）。

## 范围

在所有固件版本中，所压入的周期时间被限制在 1 个控制周期到 1000 秒对应的控制周期数之间；超出该范围的值将被拒绝。上限随控制器的控制环采样率缩放——例如，在 65 536 采样/秒的控制器上为 65 536 000 个采样，在 16 384 采样/秒的控制器上为 16 384 000 个采样。可接受的范围不随版本不同而有差异。

独立控制器在 v4 上支持此关键字；Central-i 在 v4 和 v5 上均支持。

## 示例

```text
AFIFOPushCycle=16    ; queue a cycle-time entry of 16 control samples
```

## 另请参阅

- [FIFOCycleTime](FIFOCycleTime.md) — 当前段持续时间
- [FIFOPushLinP](FIFOPushLinP.md)、[FIFOPushLinV](FIFOPushLinV.md) — 压入线性段
- [FIFOPushParP](FIFOPushParP.md)、[FIFOPushParA](FIFOPushParA.md) — 压入抛物线段
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
