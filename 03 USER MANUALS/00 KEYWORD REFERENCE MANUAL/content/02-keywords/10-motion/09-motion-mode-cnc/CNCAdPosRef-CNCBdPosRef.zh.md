---
summary: CNCAPosRef 的微分值——规划器当前的矢量速度。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAdPosRef/CNCBdPosRef

CNCAPosRef 的微分值——规划器当前的矢量速度。

## 概述

`CNCAdPosRef`（及其在第二 CNC 组上的对应关键字 `CNCBdPosRef`）报告 [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) 的每控制周期变化量，即**沿 CNC 路径的当前指令速度**（规划器的路径/矢量速度）。该值为只读，实时反映当前段的运动曲线。

## 工作原理

CNC 模式每个控制周期推进一个标量路径速度并将其累加到路径位置上。`CNCAdPosRef` 以速度形式表示该推进量：它是当前 `CNCAPosRef` 与上一周期 `CNCAPosRef` 之差（即路径坐标的变化率）。因此，它是路径速度曲线在各段端速之间加减速时的实时值。

- 在加速阶段，该值以当前加速度 [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) 向指令路径速度 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md)（应用速度缩放系数后）上升。
- 在巡航阶段，该值保持在缩放后的指令速度。
- 在制动阶段，该值以当前减速度 [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) 向段端速度 [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) 下降，并在路径到达段长度时达到该速度。

对于非运动段类型（延时、等待、设置位置、滤波器设置），路径不推进，因此在该段待处理期间 `CNCAdPosRef` 读数为零。为抑制端速度为零的段边界处的速度尖峰，控制器可能在该边界处保持该值稳定，而不报告瞬变值。

`CNCAdPosRef` 是规划器的*指令***路径**（合成）速度；它不是任何单个成员轴的速度。从成员轴测量的*实际*合成速度由 [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) 报告。

### CNCB 说明

`CNCBdPosRef` 是独立的第二 CNC 组的相同物理量。

## 示例

```text
ACNCAdPosRef        ; read the current path velocity on group A
ACNCBdPosRef        ; read the current path velocity on group B
```

## 另请参阅

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — 本关键字所报告变化率对应的路径位置
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 本值向其斜坡加速的指令路径速度
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — 本值在段末向其斜坡减速的段端速度
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — 从成员轴测量的实际合成速度
