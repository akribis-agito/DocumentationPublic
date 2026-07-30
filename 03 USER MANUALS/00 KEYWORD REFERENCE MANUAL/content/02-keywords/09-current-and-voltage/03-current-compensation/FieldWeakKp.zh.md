---
keyword: FieldWeakKp
summary: 磁场削弱外环的比例增益，相对电流环带宽归一化。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 873
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
  range: [0, 1]
  default: 0
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# FieldWeakKp

磁场削弱外环的比例增益。

## 概述

磁场削弱根据*电压误差*——即指令电压矢量与驱动器限值之间剩余的电压余量——来调节负 d 轴电流。`FieldWeakKp` 是该调节器的比例项。

驱动器会将所设值相对电流环带宽 [CurrBw](CurrBw.md) 归一化，因此该增益在电气时间常数差异很大的不同电机之间具有可比性。

## 工作原理

一旦电压矢量饱和，外环便使用 `FieldWeakKp` 与 [FieldWeakKi](FieldWeakKi.md) 根据电压误差计算 d 轴电流指令。比例项决定环路对余量变化的响应速度；积分项则负责将 d 轴电流推进到工作点并保持在该处。

> **注意：** 实际上积分项承担了大部分作用。比例项主要影响电机首次进入饱和时环路的表现。

### 调试

在启用 [FieldWeakEn](FieldWeakEn.md) 的情况下加速穿越基速进行调试，并观察 d 轴电流的稳定过程。比例增益过大会使驱动器在进出饱和时 d 轴指令出现抖动。

> **重要：** 该环路指令的 d 轴电流与磁钢磁场方向相反。调试前，请依据电机在**工作温度下**的可逆去磁限值设置 [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md)。超过该限值磁钢将被永久削弱，电机无法恢复。

### 边界情况

- **禁用时无效：** 除非 [FieldWeakEn](FieldWeakEn.md) 为 1，否则被忽略。
- **范围：** 超出 `0…1` 的写入将被钳位。

## 示例

```text
AFieldWeakKp=0.10
```

## 另请参阅

- [FieldWeakKi](FieldWeakKi.md) — 积分项
- [FieldWeakEn](FieldWeakEn.md) — 总使能
- [CurrBw](CurrBw.md) — 这些增益所归一化的带宽
