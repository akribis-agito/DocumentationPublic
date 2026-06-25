---
keyword: VelTrackFact
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 107
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
  - 0
  - 1228
  default: 1024
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 速度前馈（跟踪）系数——缩放叠加到位置控制器输出上的参考派生速度。
---
# VelTrackFact

速度前馈（跟踪）系数——缩放叠加到位置控制器输出上的参考派生速度。

## 概述

`VelTrackFact` 是位置环的速度前馈增益。它对位置参考的（滤波后）微分——参考速度 [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md)——进行缩放，并将结果叠加到位置控制器输出上，构建速度环参考 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)。该前馈使速度环能够直接跟踪指令速度，从而减少运动过程中位置比例增益原本需要产生的位置误差。

使用中的系数为 `VelTrackFact/1024`，因此值 `1024` 对应单位前馈（完整参考速度）。

## 工作原理

`VelTrackFact` 对 [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) 进行缩放，缩放值与位置控制器输出（[PosGain](../03-position-control/PosGain.md) 项）相加，构成 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)：

$$
\text{VelRef} = \text{PosErr} \cdot \text{PosGain} + \frac{\text{dPosRef} \cdot \text{VelTrackFact}}{1024}
$$

- **相乘对象：** 滤波后的参考速度 [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md)（位置参考的微分，经 [dPosRefFilt](dPosRefFilt.md) 低通滤波器后）。
- **求和位置：** 缩放项叠加到位置环输出上，构成 [VelRef](../../10-motion/01-kinematics-status/VelRef.md)，位于双环、运行模式和 `MaxVel` 处理之前。
- **缩放/单位：** 有效系数为 `VelTrackFact/1024`（`1024` = ×1.0 = 完整参考速度）。
- **范围/默认值：** `0` 到 `1228`，默认 `1024`（单位前馈）。最大值 `1228` 对应约 ×1.2。

## 示例

```text
AVelTrackFact=1024  ; unity velocity feed-forward (pass the full reference velocity)
AVelTrackFact=0     ; disable velocity feed-forward
AVelTrackFact       ; read the velocity feed-forward factor
```

### 计算示例：匀速运动时的贡献

当 `VelTrackFact = 1024`（单位）、`PosGain = 400`，在匀速运动阶段滤波后参考速度为 `dPosRef = 20000`（用户单位/s），假设位置误差稳定在 `PosErr = 5`。速度环参考为：

`VelRef = 5 x 400 + (20000 x 1024) / 1024 = 2000 + 20000 = 22000`（用户速度单位）

前馈项（`20000`）提供了 `VelRef` 的大部分，位置环只需补偿 `2000` 以覆盖残差。将 `VelTrackFact = 0` 将迫使位置环单独从误差产生全部 `22000`，从而增大稳态跟随误差。

## 另请参阅

- [dPosRef](../../10-motion/01-kinematics-status/dPosRef.md) — `VelTrackFact` 缩放的参考速度
- [dPosRefFilt](dPosRefFilt.md) — 缩放前对 `dPosRef` 应用的低通滤波器
- [VelRef](../../10-motion/01-kinematics-status/VelRef.md) — 缩放前馈加入的速度环参考
- [PosGain](../03-position-control/PosGain.md) — 前馈叠加到其输出上的位置增益
- [PosKi](../03-position-control/PosKi.md) — 输出加入同一求和点的位置积分（v5）
- [VelFFW](../05-feedforwards/VelFFW.md) — 进入电流指令的速度前馈（并行路径）
