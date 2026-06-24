---
keyword: PolePrs
summary: 电机磁极对数，按电机类型进行解释，用于正确的反馈与换相。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 54
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
  - 1
  - 50
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PolePrs

电机磁极对数，按电机类型进行解释，用于正确的反馈与换相。

## 概述

`PolePrs` 定义磁极对数（一个极对 = 一个 N 极加一个 S 极）。其确切含义取决于所配置的 [MotorType](MotorType.md)。设置正确的值对于反馈与换相正常工作以及防止可能的损坏至关重要。

此关键字仅在 [MotorType](MotorType.md) 为 3（直线直流无刷）、4（旋转直流无刷）或 7（闭环步进）时适用。对于直线无刷电机（类型 3），您必须始终自行设置 `PolePrs = 1`——控制器不会强制设定该值。由于其作用域为轴且保存至闪存，因此在电机使能或运动中时无法更改。在无刷电机上更改 `PolePrs` 会重新置位换相（[StatReg](../07-status-and-faults/StatReg.md) 换相位被清除，直到该轴重新定相）。

## 工作原理

对于无刷电机，`PolePrs` 与 [EncRes](../03-encoder/01-general-settings/EncRes.md) 一起定义用于换相的**电气周期**。控制器按下式预先计算每个电气周期的计数

$$Counts\ per\ electrical\ cycle = \frac{\text{EncRes}}{\text{PolePrs}}$$

并通过将反馈位置在周期内的位置乘以 $2\pi / (\text{EncRes}/\text{PolePrs})$，将反馈位置转换为电角度。该角度驱动逆 Park 变换，从而产生三相电压。因此，错误的 `PolePrs` 会错误地缩放电角度，导致换相失败，电机可能飞车——请在使能前正确设置。

对于闭环步进电机，`PolePrs`（每转电气周期数）与 [StepBits](StepBits.md) 定义用于将速度参考转换为步进增量的*每计数步数*因子：$\text{StepsPerCount} = \text{PolePrs} \cdot 2^{\text{StepBits}} / \text{EncRes}$。

`PolePrs` 按电机类型的不同解释如下：

| MotorType               | PolePrs 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3 (Linear DC brushless) | PolePrs 是每个磁周期的极对数。简而言之，对于直线无刷电机，用户必须始终设置 PolePrs = 1。                                                                                                                                                                                                                                                                                                                          |
| 4 (Rotary DC brushless) | PolePrs 是旋转电机每机械转的极对数。                                                                                                                                                                                                                                                                                                                                                                           |
| 7 (Stepper closed loop) | PolePrs 是 2 相步进电机每机械转的电气周期数（1 个电气周期 = 1 组完整的全步励磁序列）。在 1 个电气周期中，共有 4 个全步。通常，步进电机制造商以每个全步的物理角度来规定分辨率。这意味着在 1 转中，电气周期数为 $$\text{PolePrs} = \ \ \frac{360\lbrack physical\ deg\rbrack}{4 \cdot Manufacturer\ step\ angle\left\lbrack \frac{physical\ deg}{step\ count} \right\rbrack}$$ |

## 示例

```text
APolePrs=1           ; linear DC brushless motor (must be 1)
APolePrs=4           ; rotary brushless: 4 pole pairs per revolution
APolePrs            ; query the configured pole-pair count
```

## 另见

- [MotorType](MotorType.md) — 决定 PolePrs 的解释方式
- [EncRes](../03-encoder/01-general-settings/EncRes.md) — 编码器分辨率，与 PolePrs 一起构成电气周期
- [StepBits](StepBits.md) — 步进电机每电气周期的步数
- [StatReg](../07-status-and-faults/StatReg.md) — 换相状态位（在无刷电机上更改 PolePrs 时被清除）
