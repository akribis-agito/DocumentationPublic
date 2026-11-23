---
keyword: MotForceConst
summary: 直线电机与音圈电机的电机力常数，单位 N/A（有效值）；磁场削弱的前提条件。
availability:
- controller
- ci-master
can_code: 871
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 1000.0
  default: 10.0
  scaling: 1.0
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.09'
overrides: {}
language: zh-CN
---

# MotForceConst

直线电机与音圈电机的电机力常数，单位为牛顿每安培有效值。

## 概述

`MotForceConst` 是电机每安培有效值相电流产生的推力，按电机数据表给出的值填写（N/Arms）。它是 [MotTorqConst](MotTorqConst.md) 的**直线电机**对应项；对任一给定轴，两者中只有一个适用，由 [MotorType](MotorType.md) 选择。

驱动器将其与 [MagneticPitch](MagneticPitch.md) 一起用于推导磁链，而所有磁场削弱相关常数均依赖于该磁链。增强型 PTP 规划器（Central-i 主站）用它限定直线无刷电机所能提供的加速度，负载估计器（AGM800 / AGM800-EC）用它把运动质量换算为电流。

## 工作原理

驱动器的相电流以峰值幅值表示，因此对三相直线无刷电机，驱动器先将有效值常数除以 √2 再使用。音圈电机通过直流电流，有效值等于峰值，常数按填写值直接使用：

```text
Kf_peak = MotForceConst / sqrt(2)    ; 直线无刷电机（MotorType 3）
Kf_peak = MotForceConst              ; 音圈电机（MotorType 2）
psi_f   = 1.061032954e-4 * Kf_peak * MagneticPitch
```

驱动器由 `psi_f` 计算特征电流、去磁电流限值以及归一化的磁场削弱增益。

> **重要：** 因此对直线电机而言，`MotForceConst` 是磁场削弱的**前提条件**，而不是可选的优化项。若保持默认值，上述乘积将失去意义，特征电流塌缩为零，无论 [FieldWeakEn](../09-current-and-voltage/03-current-compensation/FieldWeakEn.md) 如何设置，磁场削弱外环都将保持不工作。

> **示例演算：** AKM100-B1 数据表的力常数为 76.5 N/Arms，电气周期为 42 mm。设置 `MotForceConst=76.5` 与 `MagneticPitch=42` 得到磁链 0.241 Wb，与数据表的反电动势常数 62.5 Vpeak/(m/s) 一致。相电感为 29 mH 时，特征电流为 8.3 A（峰值）。特征电流*低于*该电机 14.4 Arms 的峰值额定值（20.4 A 峰值），是判断一台电机是否值得进行磁场削弱的经典依据。

### 边界情况

- **单位：** 牛顿每安培**有效值**，即常见的数据表约定。请直接填写数据表数值。若曾按旧固件的每安培峰值换算（数据表数值除以 √2），该值在直线无刷电机上现在偏低 √2 倍：请重新填写数据表数值。
- **电机类型：** 除非 [MotorType](MotorType.md) 选择直线电机或音圈电机，否则本参数被忽略。旋转电机使用 [MotTorqConst](MotTorqConst.md)。
- **零值：** 取值为 0 时，增强型 PTP 规划器不启用，磁场削弱不工作。默认值 10.0 并非电机的实际常数，请设置真实值。
- **取代 TorqueConst：** 增强型 PTP 规划器原有的独立参数 `TorqueConst`（CAN 864）已停用；对直线电机，规划器改为读取本关键字。旧固件保存的 `TorqueConst` 值将被忽略。
- **运动中不可设置：** 修改它会重新推导所有相关常数，因此轴在运动时该写入被拒绝。

## 示例

```text
AMotForceConst=76.5   ; AKM100-B1，取自数据表的每安培有效值推力
AMagneticPitch=42     ; 必须同时设置
```

## 另请参阅

- [MotTorqConst](MotTorqConst.md) — 旋转电机对应项
- [MagneticPitch](MagneticPitch.md) — 磁链推导的另一半
