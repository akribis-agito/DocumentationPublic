---
keyword: FIFOPushLinV
summary: 将恒速（线性）段压入 FIFO 运动队列。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 286
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# FIFOPushLinV

将恒速（线性）段压入 FIFO 运动队列。

## 概述

`FIFOPushLinV` 将一个**按速度定义的线性**段（[FIFOType](FIFOType.md) 中的类型 2）追加到队列末尾。该值为速度参考，在段的持续时间内保持恒定。该段从前一个位置参考出发，以该速度对应的固定每采样步长推进位置参考。

它是用于在运动前或运动过程中填充队列的 `FIFOPush*` 函数之一。条目将被添加到队列末尾。若队列已满（无空闲条目），则该压入操作会被拒绝并返回错误 105，且不会添加任何内容。

与 [FIFOPushLinP](FIFOPushLinP.md) 不同——后者指定行进距离并由周期时间推导速度——本函数直接指定速度。因此，所覆盖的距离取决于当前有效的 [FIFOCycleTime](FIFOCycleTime.md)。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

当控制器到达此段时，它在段的持续时间内每个控制周期按提供的速度推进位置参考。速度在 [FIFOStatus](FIFOStatus.md)（索引 4）中报告；加速度（索引 5）为 0。可接受的范围为 -1 300 000 000 至 1 300 000 000。

## 示例

```text
AFIFOPushLinV=500000 ; queue a constant-velocity segment at velocity 500000
```

## 另请参阅

- [FIFOPushLinP](FIFOPushLinP.md) — 按位置增量压入线性段
- [FIFOPushCycle](FIFOPushCycle.md) — 设置段持续时间
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
