---
keyword: AuxVel
summary: 辅助编码器速度反馈（AuxPos 的后向欧拉微分）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 6
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# AuxVel

辅助编码器速度反馈（AuxPos 的后向欧拉微分）。

## 概述

`AuxVel` 报告辅助编码器的速度，计算方式为辅助位置反馈 [AuxPos](AuxPos.md) 的后向欧拉微分。它以辅助用户单位每秒（通过 [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) 配置）表示。它是主速度反馈 [Vel](Vel.md) 在辅助环中的对应量。

## 工作原理

$$
\text{AuxVel} = \frac{\text{AuxPos}\left(1 - z^{-1}\right)}{T_{s}}
$$

其中 $T_{s}$ 是控制器采样时间。它实现为 [AuxPos](AuxPos.md) 的每周期变化量乘以采样频率，即 `ΔAuxPos × samples-per-second`，等于 `ΔAuxPos / Tₛ`。这与主 `Vel[2]` 所用的单差分方法相同；辅助编码器没有滑动平均或 1/T 变体。

在**双环**（[DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1）中，`AuxVel` 成为速度环反馈 [Vel](Vel.md)`[1]`。当 [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) ≥ 1 时，反馈按 $\frac{\text{DualLoopFact}}{65536}$ 缩放，因此 `Vel[1]` 以主编码器单位表示；当 `DualLoopFact` < 1 时，反馈增益为 1.0，因此 `Vel[1]` 保持辅助编码器单位，而速度环指令则改为按 $\frac{1}{\text{DualLoopFact}/65536}$ 缩放。

### 边界情况

- **电机失能：** `AuxVel` 持续反映辅助编码器的每周期变化；如果辅助轴被外部反向驱动，则即使电机失能 `AuxVel` 也会非零。
- **仿真模式（`MotorType` = 5）：** `AuxPos` 不由硬件更新，因此 `AuxVel` 为零。
- **ModRev 环绕：** [ModRev](../../03-encoder/04-modulo-mode/ModRev.md) 仅作用于 [Pos](Pos.md)——[AuxPos](AuxPos.md) 不会被环绕，因此 `AuxVel` 不会出现虚假的取模边沿尖峰。对于本身在硬件中环绕的旋转辅助编码器，单差分微分将在每次环绕时看到一个单采样跳变。
- **龙门：** `AuxVel` 为按轴配置（无龙门共模/差模组合）；每条腿的 `AuxVel` 相互独立。
- **激活故障：** `AuxVel` 在每个周期持续计算；在故障期间读取它可显示负载是否仍在运动。

## 示例

```text
AAuxVel             ; read the auxiliary velocity
```

## 版本间差异

在 **v5（central-i）** 中，`AuxVel` 是 64 位；单差分微分不变。数据类型/范围的差异显示在 frontmatter 中。**v5 仅适用于 central-i。**

## 另请参阅

- [AuxPos](AuxPos.md) — 辅助位置，此微分的来源
- [Vel](Vel.md) — 主速度反馈数组（双环下 `Vel[1]` 使用 `AuxVel`）
- [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — 辅助用户单位缩放
- [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — `AuxVel` 馈入速度环时所应用的缩放
