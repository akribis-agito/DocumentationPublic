---
keyword: FieldWeakKi
summary: 磁场削弱外环的积分增益，相对电流环带宽归一化。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 874
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range: [0, 100]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# FieldWeakKi

磁场削弱外环的积分增益。

## 概述

`FieldWeakKi` 是磁场削弱调节器的积分项。它对电压误差进行累积，是真正将 d 轴电流推向负值并将其保持在工作点的环节。

与 [FieldWeakKp](FieldWeakKp.md) 一样，该值相对 [CurrBw](CurrBw.md) 归一化。

## 工作原理

在电压矢量饱和期间积分器持续累积，使 d 轴指令向更负的方向推进，直到电机能够达到指令速度。累积量一侧以零为界——磁场削弱绝不会指令*正向* d 轴电流——另一侧以由 [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) 推导出的去磁限值为界。

> **注意：** 积分器需要时间才能到达工作点。若测试或测量仅采样启用磁场削弱后的一小段窗口，将只捕捉到环路的瞬态过程，从而低估该功能的实际效果。

> **示例演算：** 无论 [FieldWeakEn](FieldWeakEn.md) 如何设置，`FieldWeakKi = 0` 都会直接禁用磁场削弱：没有积分项，环路永远不会累积出 d 轴指令，`Id` 保持为 0。任何非零取值都会使 `Id` 在电压矢量饱和期间向负方向累积，其下界为 [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) 所对应的限值，上界为零。
>
> 积分器需要**数千个控制周期**才能到达工作点。若测量仅采样启用后的一小段窗口，将只捕捉到累积过程而非稳定结果，从而低估该功能的实际效果。

### 边界情况

- **抗积分饱和：** d 轴积分在电压矢量饱和期间继续累积——而这正是环路必须发挥作用的时刻——其边界由专门的限制逻辑给出，而非电流环通常的钳位方式。
- **禁用时无效：** 除非 [FieldWeakEn](FieldWeakEn.md) 为 1，否则被忽略。
- **范围：** 超出 `0…100` 的写入将被钳位。

## 示例

```text
AFieldWeakKi=2.0
```

## 另请参阅

- [FieldWeakKp](FieldWeakKp.md) — 比例项
- [FieldWkAdapEn](FieldWkAdapEn.md) — 两个增益的自适应缩放
