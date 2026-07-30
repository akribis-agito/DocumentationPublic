---
keyword: FieldWeakKi
summary: 磁场削弱外环的积分增益，相对电流环带宽归一化。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 872
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

> **示例演算：** 在相电感为 4 mH 的电机上，以 `FieldWeakKi=2.0` 启用磁场削弱后，可达速度从 201.9 rad/s 提升至 277.3 rad/s——提高 37%——d 轴电流稳定在 −3 961 mA。该稳定过程约需 15 000 个控制周期。

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
