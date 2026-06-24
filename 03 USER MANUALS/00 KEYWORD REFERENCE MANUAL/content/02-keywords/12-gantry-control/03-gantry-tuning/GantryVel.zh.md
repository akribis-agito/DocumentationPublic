---
summary: 只读龙门速度反馈——主轴为共模（线性），偏摆轴为差模（偏摆）。
keyword: GantryVel
availability:
  standalone: []
  central-i:
  - v5
can_code: 676
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryVel

只读龙门速度反馈——主轴为共模（线性），偏摆轴为差模（偏摆）。

## 概述

`GantryVel` 是一个只读变量，在 [GantryOn](../01-general-variables/GantryOn.md) 为 `1` 时报告龙门速度环所使用的龙门速度反馈。在每个轴上，它是该轴龙门反馈（[GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md)）的每周期时间导数：**主轴**上为共模（线性）反馈的导数，**偏摆轴**上为差模（偏摆）反馈的导数。由于主轴反馈是两端的共模组合，其导数仅在解耦分配对称时等于成员轴速度的均值；使用位置相关解耦映射（[GantryMapType](../01-general-variables/GantryMapType.md) = 1）时，主轴反馈经过映射混合，`GantryVel` 跟随该混合组合而非简单均值。它是一个轴相关状态变量，在运动中和电机使能时有效，不保存至闪存。

## 工作原理

每个控制周期内，在龙门开启时，控制器逐轴推导 `GantryVel`，并将其用作匹配速度 PI 环中的速度项：

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

- **主轴（线性环）** — `VelRef` 由线性位置环（[GantryPosGain](GantryPosGain.md) / [GantryPosKi](GantryPosKi.md)）生成；龙门模式激活时，误差由龙门增益 [GantryVelGain](GantryVelGain.md) 和 [GantryVelKi](GantryVelKi.md) 处理，取代该轴的单轴 [VelGain](../../11-control-tuning/04-velocity-control/VelGain.md) / [VelKi](../../11-control-tuning/04-velocity-control/VelKi.md)。在双环模式下，该值为辅助（电机侧）速度经双环系数缩放后的值——参见 [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md)。
- **偏摆轴（偏摆环）** — `VelRef` 由偏摆位置环（[GantryPosGain](GantryPosGain.md) / [GantryPosKi](GantryPosKi.md)）生成；误差由 [GantryVelGain](GantryVelGain.md) 和 [GantryVelKi](GantryVelKi.md) 处理。

`GantryVel` 以用户单位报告。[双环龙门控制概述](../04-dual-loop-gantry-control/00-overview.md)描述了在各控制结构下（包括 `DualLoopFact` 缩放）`GantryVel` 相对于 [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) 的计算方式。

## 示例

```text
AGantryVel          ; on the master axis: common (linear) gantry velocity
BGantryVel          ; on the yaw axis:    differential (yaw) gantry velocity
```

### 边界情况

- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）— 不更新；保持龙门开启时的最后值。
- **龙门开启瞬间** — 在速度历史预热的一个周期内，两轴均强制置为 `0`。
- **电机关闭** — 若龙门配对中的某一成员（`A` 或 `B`）在配对启用时电机关闭，固件将禁用仍处于开启状态的成员，并在其上记录 [ConFlt](../../07-status-and-faults/ConFlt.md) 故障 `1061`（"另一龙门成员轴电机关闭"）；配对随即退出龙门模式，`GantryVel` 停止更新。
- **非龙门轴** — 在既不是主轴也不是偏摆轴的轴上读取返回 `0`。
- **平台** — 仅限 v5 Central-i。

## 另请参阅

- [GantryVelGain](GantryVelGain.md) — 偏摆速度环比例增益
- [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — 辅助编码器速度
- [双环龙门控制](../04-dual-loop-gantry-control/00-overview.md) — 各模式下 GantryVel 的推导方式
