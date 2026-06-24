---
keyword: StepBits
summary: 设置步进电机每电气周期的步数，控制全步、半步或微步运行。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 256
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 2
  - 16
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StepBits

设置步进电机每电气周期的步数，控制全步、半步或微步运行。

## 概述

`StepBits` 定义步进电机每电气周期的步数，即设定每个全步励磁序列被细分的精细程度。较高的值带来更精细的微步与更平滑的运动，但代价是每步的力矩更小。

此关键字仅在 [MotorType](MotorType.md) 为 6（开环步进）或 7（闭环步进）时适用。它参与 [MotorType](MotorType.md) 下所述的分辨率与每转计数公式，并与 [PolePrs](PolePrs.md) 配合用于闭环步进电机。由于其作用域为轴且保存至闪存，因此在电机使能或运动中时无法更改。

## 工作原理

每电气周期的步数为

$$
Steps\ per\ electrical\ cycle = 2^{\text{StepBits}}\ \lbrack step\ count\rbrack
$$

`StepBits = 2` 与 `StepBits = 3` 分别对应全步（每电气周期 4 步）与半步（每电气周期 8 步）。通过将 `StepBits` 增加到 2 以上（最大为 16）实现微步。

在内部，`StepBits` 驱动三个预先计算的常量（每当 `StepBits`、[EncRes](../03-encoder/01-general-settings/EncRes.md) 或 [PolePrs](PolePrs.md) 更改时重新计算）：

- **电气周期大小** $2^{\text{StepBits}}$ — 相位位置的数量；正弦/余弦相电流查找表的一个完整电气周期跨越这么多步。
- **电气周期掩码** $2^{\text{StepBits}} - 1$ — 在相电流查找之前，周期内的位置先用此掩码进行掩码处理，使得指令位置在一个周期内干净地环绕。
- **每计数步数**（仅闭环）$\text{PolePrs} \cdot 2^{\text{StepBits}} / \text{EncRes}$ — 将以编码器计数表示的速度参考转换为步进增量。

每个控制周期，周期内的位置被转换为电角度 $\theta = \text{position} \cdot 2\pi / 2^{\text{StepBits}}$，两个相电流参考由正弦/余弦表设定，并按当前的步进电流（运动中为 [StepInMotCurr](StepInMotCurr.md)，静止时为 [StepInPosCurr](StepInPosCurr.md)）缩放：$\text{IaRef} = I\sin\theta$，$\text{IbRef} = I\cos\theta$。因此，较高的 `StepBits` 将同一 90° 电气全步跨度细分为更精细的电流矢量——运动更平滑，但每步的力矩增量更小。

## 示例

```text
AStepBits=2          ; full-stepping (4 steps per electrical cycle)
AStepBits=3          ; half-stepping (8 steps per electrical cycle)
AStepBits=8          ; microstepping (256 steps per electrical cycle)
AStepBits           ; query the current setting
```

## 另见

- [MotorType](MotorType.md) — 必须为 6 或 7（步进）此关键字才适用
- [PolePrs](PolePrs.md) — 闭环步进电机每转电气周期数
- [StepInMotCurr](StepInMotCurr.md) / [StepInPosCurr](StepInPosCurr.md) — 运动中 / 静止时的步进相电流
