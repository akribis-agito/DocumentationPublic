---
keyword: FIFOPosVelOf
summary: 叠加到每个 FIFO 位置段上的速度前馈偏置。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 663
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# FIFOPosVelOf

叠加到每个 FIFO 位置段上的速度前馈偏置。

## 概述

`FIFOPosVelOf` 是一个常量速度前馈偏置，在轴以位置跟踪模式运行时叠加到速度参考上。它在控制器从流式位置轨迹推导出的速度前馈基础上，允许上位机注入额外的速度项而无需改变已排队的目标。它是三个位置跟踪偏置中的速度分量，另外两个分别是位置偏置 [FIFOPosPosOf](FIFOPosPosOf.md) 和电流偏置 [FIFOPosCurrOf](FIFOPosCurrOf.md)。该参数不保存至闪存，可在任意时刻更改，包括运动过程中。

## 工作原理

在每个采样周期，当轴处于运动中且处于位置跟踪模式时，`FIFOPosVelOf` 的值被叠加到速度参考：

```text
velocity reference = velocity from trajectory + FIFOPosVelOf
```

该偏置仅在位置跟踪模式下且轴运动时生效；在其他条件下无效。它偏置前馈路径，不改变位置目标，因此不会单独驱使轴运动至新位置——它主要用于改善跟踪性能或施加有意的速度偏置。该值以控制器速度单位解释。

当轴进入位置跟踪模式时，`FIFOPosVelOf` 将被复位为 0（与 [FIFOPosPosOf](FIFOPosPosOf.md) 和 [FIFOPosCurrOf](FIFOPosCurrOf.md) 一同复位），因此每次运行均从无速度偏置开始。若需要非零偏置，请在模式进入后重新设置。

## 示例

```text
AFIFOPosVelOf=10000  ; add a uniform velocity feedforward bias
AFIFOPosVelOf=0      ; remove the bias
```

## 另请参阅

- [FIFOPosPosOf](FIFOPosPosOf.md) — 位置偏置
- [FIFOPosCurrOf](FIFOPosCurrOf.md) — 电流前馈偏置
- [FIFOPosTrgt](FIFOPosTrgt.md) — 工作目标位置
