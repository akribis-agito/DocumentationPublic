---
keyword: StepInPosCurr
summary: 步进电机相电流指令，单位 mA，在电机静止时保持。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 254
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 32000
  default: 50
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StepInPosCurr

步进电机相电流指令，单位 mA，在电机静止时保持。

## 概述

`StepInPosCurr` 是在步进电机**静止时**施加的相电流指令（单位毫安），即保持电流。通常将其设置得低于运动电流，以在仍保持位置的同时减少发热与功耗。配套关键字 [StepInMotCurr](StepInMotCurr.md) 设定运动期间使用的较高电流。

此关键字仅在 [MotorType](MotorType.md) 为 6（开环步进）或 7（闭环步进）时适用。其作用域为轴且保存至闪存，但可在电机使能且运动中时更改。值为 0 时不施加保持电流。其最大值为产品最大电流指令的一半（运动电流 [StepInMotCurr](StepInMotCurr.md) 可使用完整的最大值）。

## 工作原理

每个控制周期，固件根据运动状态选择步进电流：当轴**未**运动（[MotionStat](../10-motion/05-motion-status/MotionStat.md) 为零，或仅在等待输入以启动）时，使用 `StepInPosCurr`；运动中则使用 [StepInMotCurr](StepInMotCurr.md)。所选的值缩放相对于当前电角度 θ 保持的相电流矢量：

$$\text{IaRef} = \text{StepInPosCurr} \cdot \sin\theta \qquad \text{IbRef} = \text{StepInPosCurr} \cdot \cos\theta$$

从而使电机以较小的发热保持其位置。由 2 相电流环将 Ia/Ib 驱动至这些参考值；当 `StepInPosCurr = 0` 时不流过保持电流，电机可被反向驱动。

## 示例

```text
AStepInPosCurr=500       ; 500 mA holding current at standstill
AStepInPosCurr=0         ; no holding current
AStepInPosCurr          ; query the current value
```

## 版本间变更

在 **v5（central-i）** 中，此参数为 32 位浮点值（`float32`），而非 v4 的整数；它仍以 mA 表示。v5 仅适用于 central-i。

## 另请参阅

- [StepInMotCurr](StepInMotCurr.md) — 运动中的步进相电流（步进电流）
- [MotorType](MotorType.md) — 必须为 6 或 7（步进）此关键字才适用
- [StepBits](StepBits.md) — 每电气周期的步数
- [MotionStat](../10-motion/05-motion-status/MotionStat.md) — 选择此电流还是运动电流的运动状态
