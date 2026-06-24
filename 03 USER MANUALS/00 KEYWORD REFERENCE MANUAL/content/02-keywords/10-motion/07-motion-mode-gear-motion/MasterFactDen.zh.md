---
summary: 应用于主变量增量的齿轮比分母。
keyword: MasterFactDen
availability:
  standalone: []
  central-i:
  - v5
can_code: 632
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
  - 1
  - 16777215
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MasterFactDen

应用于主变量增量的齿轮比分母。

## 概述

`MasterFactDen` 是电子齿轮运动中齿轮比的分母。与分子 [MasterFact](MasterFact.md) 共同构成精确有理比值 `MasterFact / MasterFactDen`，将主变量（由 [GearMaster](GearMaster.md) 选择）的变化量映射至 [MasterPos](MasterPos.md) 的变化量，从而驱动从动轴的位置参考 [PosRef](../01-kinematics-status/PosRef.md)（直接齿轮，[MotionMode](../02-motion-configuration/MotionMode.md) `= 5`）或目标 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md)（间接齿轮，`MotionMode = 6`）。

`MasterFactDen` **仅在 v5（central-i）上存在**。v4 没有分母：比值为 `MasterFact / 65536`（参见 [MasterFact](MasterFact.md)）。因此，默认值 `65536` 在 `MasterFact = 65536` 时可复现 v4 的 1:1 比值。

## 工作原理

$$
\Delta_{\text{MasterPos}} = \frac{\text{MasterFact}}{\text{MasterFactDen}} \cdot \Delta_{\text{master variable}}
$$

### 精确无漂移比值

当该参数对被设置后，控制器会将 `MasterFact` 和 `MasterFactDen` 除以它们的最大公因数进行化简。分母始终保持为正值——比值的符号由 `MasterFact` 决定。

每个控制周期，控制器以**商与余数**方案在扩展精度浮点运算中应用该比值：将主变量变化量的小数部分延续至下一个周期，使累积的从动轴运动量等于 `MasterFact / MasterFactDen × 主变量变化量`，即使对于不是 1/65536 整数倍的比值，也不会产生长期舍入漂移。这是 v5 分子/分母形式相对于 v4 单因子形式的主要优势。

### 示例计算

虚拟主编码器每转报告 360 000 计数；从动轴的齿轮比为每 11 个主单位对应 7 个从动轴单位。设置 `MasterFact = 7`，`MasterFactDen = 11`。若主轴以 360 000 计数/秒（1 转/秒）旋转，`MasterPos` 的累积速率为 `360000 × 7/11 ≈ 229 091` 个从动单位/秒。每个周期，控制器将主变量变化量乘以 `7/11` 并将余数小数部分延续至下一个周期，因此在任意 N 个周期的窗口内，累积的从动轴变化量精确等于 `7N/11`。

有效范围为 `1 … 16777215`；不得为零。

## 示例

```text
AMasterFactDen=65536 ; with MasterFact=65536 gives a 1:1 ratio (default)
AMasterFact=3        ; together with...
AMasterFactDen=7     ; ...gives an exact 3:7 ratio (follower moves 3 per 7 master units)
AMasterFactDen       ; read the gear-ratio denominator
```

## 另请参阅

- [MasterFact](MasterFact.md) — 齿轮比分子
- [MasterPos](MasterPos.md) — 经缩放后累积的主位置
- [GearMaster](GearMaster.md) — 选择主变量
- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择直接（`= 5`）或间接（`= 6`）齿轮运动
