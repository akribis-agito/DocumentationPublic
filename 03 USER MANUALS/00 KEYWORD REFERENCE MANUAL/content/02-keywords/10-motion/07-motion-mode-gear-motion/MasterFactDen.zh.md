---
summary: 应用于主变量增量的齿轮比分母。
keyword: MasterFactDen
availability:
- controller
- ci-master
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
last_updated: '2026-11-23'
doc_revision: '2026.11'
language: zh-CN
---
# MasterFactDen

应用于主变量增量的齿轮比分母。

## 概述

`MasterFactDen` 是电子齿轮运动中齿轮比的分母。与分子 [MasterFact](MasterFact.md) 共同构成精确有理比值 `MasterFact / MasterFactDen`，将主变量（由 [GearMaster](GearMaster.md) 选择）的变化量映射至 [MasterPos](MasterPos.md) 的变化量，从而驱动从动轴的位置参考 [PosRef](../01-kinematics-status/PosRef.md)（直接齿轮，[MotionMode](../02-motion-configuration/MotionMode.md) `= 5`）或目标 [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md)（间接齿轮，`MotionMode = 6`）。

旧版 v4 电子齿轮的分母固定为 65536。在 v5 上将 `MasterFactDen` 设为 65536 并沿用原分子，即可保留旧齿轮比。如果目标齿轮比为 1:3，请将分子设为 1、分母设为 3。

在含小数余量跟踪修复的多轴固件中，直接从轴模式也使用约分后的 `MasterFact / MasterFactDen`。轴 A 保留余量并跟随轴 B 的参考变化。参见 [MotionMode10](MotionMode10.md)。

## 工作原理

$$
\Delta_{\text{MasterPos}} = \frac{\text{MasterFact}}{\text{MasterFactDen}} \cdot \Delta_{\text{master variable}}
$$

### 精确无漂移比值

当该参数对被设置后，控制器会将 `MasterFact` 和 `MasterFactDen` 除以它们的最大公因数进行化简。分母始终保持为正值——比值的符号由 `MasterFact` 决定。

每个控制周期，控制器以**商与余数**方案在扩展精度浮点运算中应用该比值：将主变量变化量的小数部分延续至下一个周期，使累积的从动轴运动量等于 `MasterFact / MasterFactDen × 主变量变化量`，即使对于不是 1/65536 整数倍的比值，也不会产生长期舍入漂移。这是 v5 分子/分母形式相对于 v4 单因子形式的主要优势。

### 迁移已保存的齿轮比

在主机对比试验中，旧版将 2:5 向下舍入为 26214/65536。从轴正向行程约 15.1 亿个计数时，旧版从轴的终点比 v5 落后 23,040 个计数。该差值与主轴净位移成正比，净位移反向时差值也反向。在所测齿轮比下，v5 的位置与目标值相差不超过半个计数。另行比较的速度前馈相差最多一个计数。[电子齿轮迁移试验](https://github.com/akribis-agito/Firmware-Main/blob/b767c53b79d07e8b825c9889cfc4779867087f9c/docs/convergence/gearing_ffw_divergence_study.md)

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
