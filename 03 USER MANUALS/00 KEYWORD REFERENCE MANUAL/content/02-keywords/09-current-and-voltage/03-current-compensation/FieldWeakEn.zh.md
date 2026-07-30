---
keyword: FieldWeakEn
summary: 使能磁场削弱，允许电机在基速以上运行。
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
  data_type: int32
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

# FieldWeakEn

使能磁场削弱，允许电机在基速以上运行。

## 概述

每台电机都有一个*基速*：在该速度下其反电动势耗尽整个直流母线电压，没有余量再驱动电流。超过该速度后，无论如何指令，电机都不再加速。

磁场削弱通过指令**负 d 轴电流**来削弱磁钢磁场，从而降低反电动势，使同样的母线电压能达到更高转速。`FieldWeakEn` 是其总开关。

## 工作原理

当 `FieldWeakEn=0` 时整个外环被跳过，电流环输出与不具备该功能的驱动器逐位相同。当 `FieldWeakEn=1` 时，环路在以下三个区域之一工作：

| 区域 | 条件 | 行为 |
|---|---|---|
| 0 | 仍有电压余量 | 不工作，d 轴电流为 0 |
| 1 | 余量耗尽 | 根据电压误差调节 d 轴电流 |
| 2 | d 轴电流达到限值 | 保持在限值，并逐步降低 q 轴限值 |

> **注意：** 在基速以下该功能不产生任何代价。驱动器在该区间不受电压限制，因此外环指令零 d 轴电流，其行为与禁用时完全一致。

> **示例演算：** 当 `FieldWeakEn = 0` 时，整个外环被跳过，`Id` 保持为 0，因此电流环输出与未内置该功能的驱动器完全相同。
>
> 设置 `FieldWeakEn = 1` 后并不会立即产生变化：在基速以下电压矢量未饱和，环路停留在区域 0，仍然指令 `Id = 0`。一旦矢量饱和，`Id` 便向负方向推进，直至电压误差被消除（区域 1），或 `Id` 达到由 [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) 推导出的限值——此时 `Id` 被保持在该处，转而对 q 轴限值进行递减（区域 2）。

> **重要：** 本功能能带来多少额外转速取决于**您的电机**，而非固件。它由磁链、d/q 电感比以及磁钢在工作温度下可承受的去磁电流决定——凸极式内置磁钢电机的收益显著高于表贴式圆形磁路电机。不同磁路结构下的实测数值请参见《电流环补偿》应用笔记。请勿依据本手册中的数字进行选型。

### 前提条件

> **重要：** 若未完成电机特性配置，磁场削弱无法启动。对直线电机，驱动器由 [MotForceConst](../../02-motor-and-amplifier/MotForceConst.md) 与 [MagneticPitch](../../02-motor-and-amplifier/MagneticPitch.md) 推导磁链；对旋转电机则由 [MotTorqConst](../../02-motor-and-amplifier/MotTorqConst.md) 与 [PolePrs](../../02-motor-and-amplifier/PolePrs.md) 推导。若保持默认值，磁链将失去意义，无论本关键字如何设置，环路都保持不工作。

### 安全

> **重要：** d 轴电流与磁钢磁场方向相反。超过磁钢 B–H 曲线的拐点后，磁通损失是**永久性**的——电机会比原先更弱，且后续任何处理都无法恢复。该拐点还随温度下降，因此在冷态台架上安全的设置可能损坏热态电机。
>
> 启用本功能前，请依据电机在工作温度下的可逆限值设置 [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md)；若数据表未给出该数值，请咨询电机制造商。

### 边界情况

- **转矩下降：** d 轴电流占用部分电流预算，因此可用的 q 轴电流——以及转矩——会减少。这是该功能的取舍，并非故障。
- **无法削弱的电机：** 特征电流远超其电流额定值的电机几乎没有磁场削弱余量。低电感无铁芯电机属于此类。

## 示例

```text
AFieldWeakEn=1        ; 在完成电机特性配置并设置 CurrLimRev 后启用
```

## 另请参阅

- [FieldWeakKp](FieldWeakKp.md)、[FieldWeakKi](FieldWeakKi.md) — 环路增益
- [FieldWkAdapEn](FieldWkAdapEn.md) — 自适应增益缩放
- [CurrLimRev](../../06-protections/02-current-and-voltage/CurrLimRev.md) — 限制去磁电流
