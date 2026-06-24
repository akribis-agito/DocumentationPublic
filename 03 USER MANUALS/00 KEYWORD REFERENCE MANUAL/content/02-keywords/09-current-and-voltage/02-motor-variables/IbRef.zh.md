---
keyword: IbRef
summary: 只读的 B 相电流参考，单位为毫安（其定义因电机类型而异）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 28
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# IbRef

只读的 B 相电流参考，单位为毫安（其定义因电机类型而异）。

## 概述

`IbRef` 是 B 相的参考电流，单位为毫安。其确切的推导方式取决于 [MotorType](../../02-motor-and-amplifier/MotorType.md)。它是测得 B 相电流 [Ib](Ib.md) 的参考对应量；二者之差即为 [IbErr](IbErr.md)。

## 工作原理

与 [IaRef](IaRef.md) 类似，B 相参考是经方向修正的标量电流参考 $\text{CurrRef}_{dir}$ 的换相投影，而 $\text{CurrRef}_{dir}$ 是应用 [CurrDir](CurrDir.md) 符号后的受限电流参考：

| 电机分组（MotorType） | B 相参考 |
|----|----|
| 单相/有刷电机（MotorType = 1, 2） | $\text{IbRef}\ = \ 0$（仅驱动 A 相）。 |
| 三相无刷电机（MotorType = 3, 4） | $\text{IbRef}\ = \ \text{CurrRef}_{dir} \cdot \sin(\theta - 120^\circ)$，其中 $\theta$ 为换相角——即 $\text{IqRef} = \text{CurrRef}_{dir}$ 与 [IdRef](IdRef.md)（= 0）逆变换的 B 相结果。无论 [ControlMode](ControlMode.md) 如何，该换相参考每个采样周期均会计算；它产生的 B 相误差 [IbErr](IbErr.md) 仅在电流控制运行于 abc 域（[ControlMode](ControlMode.md) 位 1 置位）时才用作控制环输入。当电流控制被旁路时，它也会被直接用作 B 相电压指令。 |
| 两相步进电机（MotorType = 6, 7） | $\text{IbRef}\ = \ \text{CurrRef}_{dir} \cdot \cos(\theta_{step})$，其中 $\theta_{step}$ 为步进电气角。两个步进相以正交（sin/cos）方式驱动。 |

`IbRef` 受控制器峰值电流额定值的限制，该值因产品而异（在额定值最高的硬件上可达 ±64000 mA）。它与测得 [Ib](Ib.md) 之差给出 [IbErr](IbErr.md)，即 B 相电流环的输入。

## 示例

```text
AIbRef              ; read phase B current reference (mA)
```

## 另请参阅

- [Ib](Ib.md) — 测得 B 相电流
- [IbErr](IbErr.md) — B 相电流误差
- [IaRef](IaRef.md) — A 相电流参考
- [IqRef](IqRef.md)、[IdRef](IdRef.md) — 该相参考所对应逆变换的 dq 参考（无刷电机）
- [CurrDir](CurrDir.md) — 投影到该相之前应用的方向修正
- [MotorType](../../02-motor-and-amplifier/MotorType.md) — 决定推导方式的电机类型
