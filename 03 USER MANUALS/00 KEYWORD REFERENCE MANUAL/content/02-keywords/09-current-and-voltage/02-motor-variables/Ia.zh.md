---
keyword: Ia
summary: 只读的实测 A 相电流，单位为毫安。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 9
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# Ia

只读的实测 A 相电流，单位为毫安。

## 概述

`Ia` 报告 A 相的实测电流，单位为毫安。A 相由硬件参考指南中的接线方案定义。它是 A 相参考 [IaRef](IaRef.md) 的反馈对应量；二者之差即为 A 相电流误差 [IaErr](IaErr.md)。

## 工作原理

每个控制环采样周期，固件读取 A 相电流检测 ADC，使用硬件电流检测系数将原始计数转换为毫安，并减去启动时测得的每轴零电流校准偏置：

$$
\text{Ia}\ \lbrack mA\rbrack\ = \ (ADC_{A}\ \cdot\ k_{sense})\ -\ I_{0,A}
$$

其中 $k_{sense}$ 为硬件电流检测系数，$I_{0,A}$ 为每轴零电流偏置。电流检测系数由电流量程硬件固定（因此给定的 ADC 计数映射到固定的 mA 值）。对于三相无刷电机，仅直接测量两相，第三相根据基尔霍夫定律导出为 $\text{Ic} = -(\text{Ia} + \text{Ib})$；`Ia` 本身始终是一个直接测量的相（被导出的相是第三相）。`Ia` 随后用于构成 dq 电流 [Iq](Iq.md)/[Id](Id.md) 以及幅值 [MotorCurr](MotorCurr.md)，并与每相过流保护 [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) 进行比较：如果 $|\text{Ia}|$ 连续多个采样周期保持高于 `MaxPhaseCurr`，则该轴以 A 相过流故障（故障码 1013）关断。

## 示例

```text
AIa                 ; read measured phase A current (mA)
```

## 参见

- [IaRef](IaRef.md) — A 相电流参考
- [IaErr](IaErr.md) — A 相电流误差 (IaRef − Ia)
- [Ib](Ib.md) — 实测 B 相电流
- [MotorCurr](MotorCurr.md) — 由 Ia/Ib/Ic 构成的反馈电流总幅值
- [MaxPhaseCurr](../../06-protections/02-current-and-voltage/MaxPhaseCurr.md) — 与 Ia 比较的每相过流限值
