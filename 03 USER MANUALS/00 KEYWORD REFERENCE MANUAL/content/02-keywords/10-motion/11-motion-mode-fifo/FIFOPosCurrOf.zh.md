---
keyword: FIFOPosCurrOf
summary: 叠加到每个 FIFO 位置段上的电流（力矩）前馈偏置。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 664
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# FIFOPosCurrOf

叠加到每个 FIFO 位置段上的电流（力矩）前馈偏置。

## 概述

`FIFOPosCurrOf` 是一个恒定的电流（力矩）前馈偏置，在轴以位置跟踪模式运行期间叠加到电流参考值上。它允许上位机注入额外的力矩项——例如用于补偿已知的恒定负载或重力——而无需修改已排队的目标。它是三个位置跟踪偏置中的电流分量，另外两个分别是位置偏置 [FIFOPosPosOf](FIFOPosPosOf.md) 和速度偏置 [FIFOPosVelOf](FIFOPosVelOf.md)。该参数不保存至闪存，可在任何时刻修改，包括运动中。

## 工作原理

在位置跟踪模式下，轴运动期间的每个采样，`FIFOPosCurrOf` 的值均被叠加到电流参考值上：

```text
current reference = current from control + FIFOPosCurrOf
```

该偏置在位置和速度运行模式下有效（在纯电流/力控制模式下，电流参考值直接设定，此偏置不适用）。它仅在位置跟踪模式下且轴处于运动中时有效；在其他条件下无效。它对力矩前馈施加偏置，不改变位置目标。

当轴进入位置跟踪模式时，`FIFOPosCurrOf` 将重置为 0（与 [FIFOPosPosOf](FIFOPosPosOf.md) 和 [FIFOPosVelOf](FIFOPosVelOf.md) 一同重置），因此每次运行均以无电流偏置的状态开始。若需非零偏置，请在模式进入后重新设置。

## 版本间变化

在 v5 中央控制器版本中，`FIFOPosCurrOf` 为浮点值，允许小数电流偏置。在 v4（及独立驱动器）上，它为整数值，范围为 -64000 至 64000。

## 示例

```text
AFIFOPosCurrOf=2000  ; 添加均匀的电流前馈偏置
AFIFOPosCurrOf=0     ; 移除偏置
```

## 另请参阅

- [FIFOPosPosOf](FIFOPosPosOf.md) — 位置偏置
- [FIFOPosVelOf](FIFOPosVelOf.md) — 速度前馈偏置
- [FIFOPosTrgt](FIFOPosTrgt.md) — 工作目标位置
