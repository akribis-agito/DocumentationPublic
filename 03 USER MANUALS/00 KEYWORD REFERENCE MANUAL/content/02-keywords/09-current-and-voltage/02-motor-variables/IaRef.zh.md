---
keyword: IaRef
summary: 只读的 A 相电流参考，单位为毫安（定义随电机类型而异）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 27
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
language: zh-CN
---
# IaRef

只读的 A 相电流参考，单位为毫安（定义随电机类型而异）。

## 概述

`IaRef` 是 A 相的参考电流，单位为毫安。其确切的推导方式取决于 [MotorType](../../02-motor-and-amplifier/MotorType.md)。它是实测 A 相电流 [Ia](Ia.md) 的参考对应量；二者之差即为 [IaErr](IaErr.md)。

## 工作原理

三种推导方式均从经方向修正的标量电流参考 $\text{CurrRef}_{dir}$ 出发，它是应用 [CurrDir](CurrDir.md) 符号之后的受限电流参考。换相随后将其投影到 A 相：

| 电机组 (MotorType) | A 相参考 |
|----|----|
| 单相 / 有刷电机 (MotorType = 1, 2) | $\text{IaRef}\ = \ \text{CurrRef}_{dir}$（整个电流参考都流向 A 相）。 |
| 三相无刷电机 (MotorType = 3, 4) | $\text{IaRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta)$，其中 $\theta$ 为换相角。这是在 $\text{IqRef} = \text{CurrRef}_{dir}$ 且 [IdRef](IdRef.md) = 0 时 dq 参考的逆变换。当电流控制在 abc 域中运行（[ControlMode](ControlMode.md) 位 1 置位）时，它是有效参考。 |
| 两相步进电机 (MotorType = 6, 7) | $\text{IaRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta_{step})$，其中 $\theta_{step}$ 为步进电机电角度（开环时来自位置参考，闭环时来自积分后的速度参考）。 |

`IaRef` 被限定在 ±64000 mA。它与实测 [Ia](Ia.md) 之差给出 [IaErr](IaErr.md)，即 A 相电流环的输入。

## 示例

```text
AIaRef              ; read phase A current reference (mA)
```

## 另请参阅

- [Ia](Ia.md) — 实测 A 相电流
- [IaErr](IaErr.md) — A 相电流误差
- [IbRef](IbRef.md) — B 相电流参考
- [IqRef](IqRef.md)、[IdRef](IdRef.md) — 该相参考所对应的 dq 参考的逆变换（无刷）
- [CurrDir](CurrDir.md) — 在投影到相之前应用的方向修正
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 决定推导方式的电机类型
