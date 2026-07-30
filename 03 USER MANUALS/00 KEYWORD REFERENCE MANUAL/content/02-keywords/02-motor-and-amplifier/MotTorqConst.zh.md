---
keyword: MotTorqConst
summary: 旋转电机与直流有刷电机的电机转矩常数；磁场削弱的前提条件。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 870
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
  default: 1
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# MotTorqConst

旋转电机与直流有刷电机的电机转矩常数。

## 概述

`MotTorqConst` 是电机每安培电流产生的转矩，取自电机数据表。它是 [MotForceConst](MotForceConst.md) 的**旋转电机**对应项；对任一给定轴，两者中只有一个适用，由 [MotorType](MotorType.md) 选择。

## 工作原理

对旋转电机或直流有刷电机，磁链推导如下：

```text
psi_f = (2/3) * MotTorqConst / PolePairs
```

所有磁场削弱常数——特征电流、去磁限值、归一化增益——均由 `psi_f` 导出。

> **重要：** [PolePrs](PolePrs.md) 必须正确，该推导才成立。极对数错误会直接按比例影响磁链，并随之影响所有相关常数。

### 边界情况

- **电机类型：** 除非 [MotorType](MotorType.md) 选择旋转电机或直流有刷电机，否则本参数被忽略。
- **两者均未设置：** 若电机类型与两个分支都不匹配，磁链为零，磁场削弱按构造保持不工作——无需任何特例处理。
- **运动中不可设置。**

## 示例

```text
AMotTorqConst=0.36    ; 每安培 0.36 N.m
```

## 另请参阅

- [MotForceConst](MotForceConst.md) — 直线电机对应项
