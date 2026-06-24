---
keyword: FIFOPushParA
summary: 将抛物线（恒加速度）段压入 FIFO 运动队列。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 288
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
  - -2000000000
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# FIFOPushParA

将抛物线（恒加速度）段压入 FIFO 运动队列。

## 概述

`FIFOPushParA` 将一个**按加速度定义的抛物线**段（[FIFOType](FIFOType.md) 中的类型 4）追加到队列末尾。该值为加速度参考，在段的持续时间内保持恒定，从而产生抛物线位置曲线。该段从当前规划器速度开始。它是 [FIFOPushParP](FIFOPushParP.md) 的基于加速度的对应版本，后者通过位置增量来定义段。

它是用于在运动前或运动过程中填充队列的 `FIFOPush*` 函数之一。条目将被添加到队列末尾。若队列已满（无空闲条目），则该压入操作会被拒绝并返回错误 105，且不会添加任何内容。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

当控制器到达此段时，它在段的持续时间内每个控制周期按提供的加速度增加速度，并相应地推进位置参考。变化中的速度和加速度在 [FIFOStatus](FIFOStatus.md)（索引 4 和 5）中报告。

提供的幅值必须至少为一个*控制采样频率*（在标准 16 384 Hz 控制频率下为 16 384 counts/s²）。这是每采样速度步长所能分辨的最小加速度。压入时若 `|value| < 16 384`，将在压入阶段以错误 106 被拒绝。可接受的范围为 -2 000 000 000 至 2 000 000 000。

## 示例

```text
AFIFOPushParA=100000 ; queue a constant-acceleration (parabolic) segment
```

## 另请参阅

- [FIFOPushParP](FIFOPushParP.md) — 按位置定义的抛物线段
- [FIFOPushCycle](FIFOPushCycle.md) — 设置段持续时间
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
