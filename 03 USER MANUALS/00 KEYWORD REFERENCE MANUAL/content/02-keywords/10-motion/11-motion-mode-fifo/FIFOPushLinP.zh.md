---
keyword: FIFOPushLinP
summary: 将由位置增量定义的线性段压入 FIFO 运动队列。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 285
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# FIFOPushLinP

将由位置增量定义的线性段压入 FIFO 运动队列。

## 概述

`FIFOPushLinP` 将一个**按位置增量定义的线性**段（[FIFOType](FIFOType.md) 中的类型 1）追加到队列末尾。该值为段内需行进的位置增量。该段从前一个位置参考出发，在段结束时到达该参考值加上增量的位置，以恒定速度运动。

它是用于在运动前或运动过程中填充队列的 `FIFOPush*` 函数之一。条目将被添加到队列末尾。若队列已满（无空闲条目），则该压入操作会被拒绝并返回错误 105，且不会添加任何内容。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

当控制器到达此段时，它将位置增量除以当前有效的 [FIFOCycleTime](FIFOCycleTime.md)，得到恒定的每采样步长，然后在段的持续时间内每个控制周期按该步长推进位置参考。请求的增量在最后一个采样时精确到达。由此得到的恒定速度在 [FIFOStatus](FIFOStatus.md)（索引 4）中报告；加速度（索引 5）为 0。

## 示例

```text
AFIFOPushLinP=10000  ; queue a constant-velocity segment that travels 10000 units
```

## 另请参阅

- [FIFOPushLinV](FIFOPushLinV.md) — 按速度压入线性段
- [FIFOPushCycle](FIFOPushCycle.md) — 设置段持续时间
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
