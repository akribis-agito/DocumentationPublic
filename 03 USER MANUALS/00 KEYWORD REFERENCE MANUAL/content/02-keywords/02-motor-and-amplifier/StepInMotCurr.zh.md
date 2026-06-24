---
keyword: StepInMotCurr
summary: 步进电机相电流指令，单位 mA，在电机运动中施加。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 255
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
  - 50
  - 64000
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
# StepInMotCurr

步进电机相电流指令，单位 mA，在电机运动中施加。

## 概述

`StepInMotCurr` 是在步进电机**运动中**施加的相电流指令（单位毫安），即步进电流。它设定移动时可用的力矩；配套关键字 [StepInPosCurr](StepInPosCurr.md) 设定静止时保持的较低电流。

此关键字仅在 [MotorType](MotorType.md) 为 6（开环步进）或 7（闭环步进）时适用。其作用域为轴且保存至闪存，但可在电机使能且运动中时更改。请将其设置在电机的额定电流范围内以避免过热。其最大值为产品的最大电流指令；[StepInPosCurr](StepInPosCurr.md) 被限制为其一半。

## 工作原理

每个控制周期，固件根据运动状态选取步进电流：若轴正在运动——[MotionStat](../10-motion/05-motion-status/MotionStat.md) 非零且**不**仅仅是在等待输入以启动——则使用 `StepInMotCurr`；否则使用 [StepInPosCurr](StepInPosCurr.md)。所选的值成为缩放相电流正弦/余弦矢量的电流参考幅值：

$$\text{IaRef} = \text{StepInMotCurr} \cdot \sin\theta \qquad \text{IbRef} = \text{StepInMotCurr} \cdot \cos\theta$$

其中电角度 θ 来自指令位置（参见 [StepBits](StepBits.md)）。然后由 2 相电流环将 Ia/Ib 驱动至这些参考值。因此，`StepInMotCurr` 直接设定移动期间产生力矩的电流包络。

## 示例

```text
AStepInMotCurr=2000      ; 2000 mA phase current while moving
AStepInMotCurr          ; query the current value
```

## 版本间变更

在 **v5（central-i）** 中，此参数为 32 位浮点值（`float32`），而非 v4 的整数；它仍以 mA 表示。v5 仅适用于 central-i。

## 另见

- [StepInPosCurr](StepInPosCurr.md) — 静止时的步进相电流（保持电流）
- [MotorType](MotorType.md) — 必须为 6 或 7（步进）此关键字才适用
- [StepBits](StepBits.md) — 每电气周期的步数
- [MotionStat](../10-motion/05-motion-status/MotionStat.md) — 选择此电流还是静止电流的运动状态
