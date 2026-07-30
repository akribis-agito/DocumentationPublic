---
keyword: MotForceConst
summary: 直线电机与音圈电机的电机力常数，单位 N/A；磁场削弱的前提条件。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 871
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
  range: [0, 1000]
  default: 10
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# MotForceConst

直线电机与音圈电机的电机力常数，单位 N/A。

## 概述

`MotForceConst` 是电机每安培电流产生的推力，取自电机数据表。它是 [MotTorqConst](MotTorqConst.md) 的**直线电机**对应项；对任一给定轴，两者中只有一个适用，由 [MotorType](MotorType.md) 选择。

驱动器将其与 [MagneticPitch](MagneticPitch.md) 一起用于推导磁链，而所有磁场削弱相关常数均依赖于该磁链。

## 工作原理

对直线电机或音圈电机，磁链推导如下：

```text
psi_f = 1.061032954e-4 * MotForceConst * MagneticPitch
```

驱动器由 `psi_f` 计算特征电流、去磁电流限值以及归一化的磁场削弱增益。

> **重要：** 因此对直线电机而言，`MotForceConst` 是磁场削弱的**前提条件**，而不是可选的优化项。若保持默认值，上述乘积将失去意义，特征电流塌缩为零，无论 [FieldWeakEn](../09-current-and-voltage/03-current-compensation/FieldWeakEn.md) 如何设置，磁场削弱外环都将保持不工作。

> **示例演算：** AKM100-B1 数据表的力常数为 76.5 N/A，电气周期为 42 mm。设置 `MotForceConst=76.5` 与 `MagneticPitch=42` 得到磁链 0.341 Wb、特征电流 11.8 A。与该电机 14.4 A 的峰值额定值相比，特征电流*低于*峰值额定值是判断一台电机是否值得进行磁场削弱的经典依据。

### 边界情况

- **单位：** 牛顿每安培**有效值**，与常见数据表约定一致。
- **电机类型：** 除非 [MotorType](MotorType.md) 选择直线电机或音圈电机，否则本参数被忽略。旋转电机使用 [MotTorqConst](MotTorqConst.md)。
- **运动中不可设置：** 修改它会重新推导所有相关常数，因此轴在运动时该写入被拒绝。

## 示例

```text
AMotForceConst=76.5   ; AKM100-B1
AMagneticPitch=42     ; 必须同时设置
```

## 另请参阅

- [MotTorqConst](MotTorqConst.md) — 旋转电机对应项
- [MagneticPitch](MagneticPitch.md) — 磁链推导的另一半
