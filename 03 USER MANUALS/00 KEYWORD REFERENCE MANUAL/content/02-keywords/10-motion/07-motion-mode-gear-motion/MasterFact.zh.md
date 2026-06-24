---
keyword: MasterFact
summary: 应用于主变量增量的齿轮比分子。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 120
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -16777215
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MasterFact

应用于主变量增量的齿轮比分子。

## 概述

`MasterFact` 是在电子齿轮运动中应用于主变量变化量的齿轮比分子。它将主变量（由 [GearMaster](GearMaster.md) 选定）的变化量映射为 [MasterPos](MasterPos.md) 的变化量，进而驱动从动件的位置参考 [PosRef](../01-kinematics-status/PosRef.md)（直接齿轮，[MotionMode](../02-motion-configuration/MotionMode.md) `= 5`）或其目标位置 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md)（间接齿轮，`MotionMode = 6`）。

## 工作原理

### 比值以 65536 为基准归一化

`MasterFact` 是相对于基数 65536 的分子，因此默认值 `65536` 对应 **1:1** 比值。在 v4 中，它直接应用，无独立分母项：

$$
\Delta_{\text{MasterPos}} = \frac{\text{MasterFact}}{65536} \cdot \Delta_{\text{主变量}}
$$

缩放后的变化量每周期累加到 `MasterPos` 中。

`MasterFact` 为负值时，从动件方向相对于主变量反向。若要设置非 1/65536 整数倍的比值，请使用分子/分母对（v5）——参见*版本间变化*。

### 关于独立直接从轴模式的说明

直接从轴运动模式（[MotionMode](../02-motion-configuration/MotionMode.md) `= 10`，参见 [MotionMode10](MotionMode10.md)）同样使用 `MasterFact` 作为缩放因子，但直接读取该值，无需经过 `MasterPos` 或 `MasterFilt`。它是与电子齿轮运动（`MotionMode = 5` 和 `= 6`）不同的独立机制——该模式的输入约定参见 [MotionMode10](MotionMode10.md)。

## 示例

```text
AMasterFact=65536    ; 1:1 比值（默认）
AMasterFact=131072   ; 从动件每单位主变量移动 2 个主变量单位
AMasterFact=-65536   ; 1:1，反向
AMasterFact          ; 读取当前值
```

## 版本间变化

在 **v4** 中，比值为 `MasterFact / 65536`（仅分子），累加中无分母。在 **v5（central-i）** 中，应用完整有理比值 `MasterFact / MasterFactDen`，并保留小数余量，使非整数比值精确且无长期漂移；参见 [MasterFactDen](MasterFactDen.md)。**v5 仅适用于 central-i。**

## 参见

- [MasterFactDen](MasterFactDen.md) — 齿轮比分母（v5）
- [MasterPos](MasterPos.md) — 经累加、缩放的主位置
- [GearMaster](GearMaster.md) — 选择主变量
- [MasterFilt](MasterFilt.md) — 齿轮参考的低通滤波器（直接模式）
- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择直接（`= 5`）或间接（`= 6`）电子齿轮运动
- [MotionMode10](MotionMode10.md) — 同样读取 `MasterFact` 的独立直接从轴模式
