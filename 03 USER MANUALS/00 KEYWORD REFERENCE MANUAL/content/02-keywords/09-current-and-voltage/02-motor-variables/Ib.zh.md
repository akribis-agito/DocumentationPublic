---
keyword: Ib
summary: 只读的测得 B 相电流，单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 10
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# Ib

只读的测得 B 相电流，单位为毫安。

## 概述

`Ib` 报告 B 相的测得电流，单位为毫安。B 相由硬件参考指南中的接线方案定义。它是 B 相参考 [IbRef](IbRef.md) 的反馈对应量；二者之差即为 B 相电流误差 [IbErr](IbErr.md)。

## 工作原理

每个控制环采样周期，固件读取 B 相电流采样 ADC，使用硬件电流采样系数将原始计数转换为毫安，并减去启动时测得的每轴零电流校准偏置：

$$
\text{Ib}\ \lbrack mA\rbrack\ = \ (ADC_{B}\ \cdot\ k_{sense})\ -\ I_{0,B}
$$

其中 $k_{sense}$ 为硬件电流采样系数，$I_{0,B}$ 为每轴零电流偏置。对于三相无刷电机，三相中仅有两相被直接采样；剩余一相由 $\text{Ia} + \text{Ib} + \text{Ic} = 0$ 推导得出（例如 $\text{Ic} = -(\text{Ia} + \text{Ib})$），因此在某些硬件型号上 `Ib` 是推导相而非测得相。对于单相（有刷/音圈）电机，仅 A 相有电流，`Ib` 保持为 0。随后 `Ib` 用于构成 dq 电流 [Iq](Iq.md)/[Id](Id.md) 以及幅值 [MotorCurr](MotorCurr.md)，并与每相过流保护 [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) 进行比对。

## 示例

```text
AIb                 ; read measured phase B current (mA)
```

## 另请参阅

- [IbRef](IbRef.md) — B 相电流参考
- [IbErr](IbErr.md) — B 相电流误差（IbRef − Ib）
- [Ia](Ia.md) — 测得 A 相电流
- [MotorCurr](MotorCurr.md) — 由 Ia/Ib/Ic 构成的总反馈电流幅值
- [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) — 与 Ib 比对的每相过流限值
