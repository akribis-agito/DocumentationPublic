---
keyword: CurrDir
summary: 翻转电机励磁方向（0 = 正常，1 = 翻转）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 76
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CurrDir

翻转电机励磁方向（0 = 正常，1 = 翻转）。

## 概述

`CurrDir` 配置电机励磁方向。它通常与编码器方向设置 [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) 一起使用，以将轴翻转到所需的物理方向。由于它改变了电流施加于电机的方式，因此在轴运动中或电机使能时不能更改。

对于无刷电机，将 `CurrDir` 更改为新值会使现有换相失效：换相完成状态被清除，必须重新执行换相后电机才能再次使能。写回相同的值则不会产生此效果。

## 工作原理

`CurrDir` 在速度/电流环与换相之间的电流路径上充当一个符号。在电流参考被限制之后，控制器形成电流环所用的方向修正后的参考：

$$
\text{CurrRef}_{dir}\ = \begin{cases} +\text{CurrRef} & \text{CurrDir} = 0 \\ -\text{CurrRef} & \text{CurrDir} = 1 \end{cases}
$$

随后换相将这个方向修正后的参考解析为相参考 [IaRef](IaRef.md)/[IbRef](IbRef.md)（以及无刷电机的 [IqRef](IqRef.md)），因此翻转 `CurrDir` 会反转指令电流驱动电机的方向。所报告的总电流 [MotorCurr](MotorCurr.md) 也被同一标志取反，从而与指令方向保持一致。测量得到的各相电流 [Ia](Ia.md)/[Ib](Ib.md) 以及 dq 电流 [Iq](Iq.md)/[Id](Id.md) 本身**不**被 `CurrDir` 取反；当 `CurrDir` = 1 时，它们相对于其参考值呈现反号。

| CurrDir | 效果 |
|---------|--------|
| 0 | 电机方向不翻转；方向修正后的参考等于 `+CurrRef`。 |
| 1 | 电机方向翻转；方向修正后的参考等于 `−CurrRef`。 |

## 示例

```text
ACurrDir=0           ; normal excitation direction
ACurrDir=1           ; flipped excitation direction
ACurrDir              ; read the current excitation-direction setting
```

## 另请参阅

- [EncDir / AuxEncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) — 编码器方向，通常与 CurrDir 一起设置
- [MotorCurr](MotorCurr.md) — 总电流，被同一 CurrDir 标志取反
- [IaRef](IaRef.md)、[IbRef](IbRef.md) — 由方向修正后的电流参考导出的相参考
- [ControlMode](ControlMode.md) — 电流/电压控制选项
