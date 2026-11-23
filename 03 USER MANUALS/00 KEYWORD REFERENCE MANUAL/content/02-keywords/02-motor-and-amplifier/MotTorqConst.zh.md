---
keyword: MotTorqConst
summary: 旋转电机与直流有刷电机的电机转矩常数，单位 N.m/A（有效值）；磁场削弱的前提条件。
availability:
- controller
- ci-master
can_code: 872
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
  default: 1.0
  scaling: 1.0
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.09'
overrides: {}
language: zh-CN
---

# MotTorqConst

旋转电机与直流有刷电机的电机转矩常数，单位为牛·米每安培有效值。

## 概述

`MotTorqConst` 是电机每安培有效值相电流产生的转矩，按电机数据表给出的值填写（N.m/Arms）。它是 [MotForceConst](MotForceConst.md) 的**旋转电机**对应项；对任一给定轴，两者中只有一个适用，由 [MotorType](MotorType.md) 选择。

以下三项功能使用该参数：

- **磁场削弱**由它推导磁链。
- **增强型 PTP 规划器**（Central-i 主站）用它限定旋转无刷电机所能提供的加速度。
- **负载估计器**（AGM800 / AGM800-EC）用它把电机惯量换算为电流。

## 工作原理

驱动器的相电流以峰值幅值表示，因此对三相无刷电机，驱动器先将有效值常数除以 √2 再使用。直流有刷电机通过直流电流，有效值等于峰值，常数按填写值直接使用：

```text
Kt_peak = MotTorqConst / sqrt(2)     ; 旋转无刷电机（MotorType 4）
Kt_peak = MotTorqConst               ; 直流有刷电机（MotorType 1）
psi_f   = (2/3) * Kt_peak / PolePairs
```

所有磁场削弱常数——特征电流、去磁限值、归一化增益——均由 `psi_f` 导出。

> **重要：** [PolePrs](PolePrs.md) 必须正确，该推导才成立。极对数错误会直接按比例影响磁链，并随之影响所有相关常数。

### 边界情况

- **单位：** 牛·米每安培**有效值**，即常见的数据表约定。请直接填写数据表数值。若曾按旧固件的每安培峰值换算（数据表数值除以 √2），该值在无刷电机上现在偏低 √2 倍：请重新填写数据表数值。
- **电机类型：** 除非 [MotorType](MotorType.md) 选择旋转电机或直流有刷电机，否则本参数被忽略。
- **两者均未设置：** 若电机类型与两个分支都不匹配，磁链为零，磁场削弱按构造保持不工作——无需任何特例处理。
- **零值：** 取值为 0 时，增强型 PTP 规划器不启用，磁场削弱不工作。默认值 1.0 并非电机的实际常数，请设置真实值。
- **取代 TorqueConst：** 增强型 PTP 规划器原有的独立参数 `TorqueConst`（CAN 864）已停用；对旋转电机，规划器改为读取本关键字。旧固件保存的 `TorqueConst` 值将被忽略。
- **运动中不可设置。**

## 示例

```text
AMotTorqConst=0.36    ; 每安培有效值 0.36 N.m，取自数据表
```

## 另请参阅

- [MotForceConst](MotForceConst.md) — 直线电机对应项
