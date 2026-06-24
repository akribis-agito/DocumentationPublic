---
summary: 当前活动段沿 CNC 路径的期望矢量速度。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCASpeed/CNCBSpeed

当前活动段沿 CNC 路径的期望矢量速度。

## 概述

`CNCASpeed`（以及第二 CNC 组对应的 `CNCBSpeed`）是当前活动段沿 CNC 路径的期望（巡航）速度，单位为用户单位/秒。该值是路径速度曲线所趋近的上限，始终视为正幅值——运动方向由路径几何形状决定，而非由符号决定。

控制器实际所瞄准的速度是 `CNCASpeed` 乘以两个动态缩放因子：段定义中编码的逐段速度因子，以及通过 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 和 [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) 施加的用户覆盖值。

## 工作原理

CNC 模式沿路径运行一条速度曲线。每个控制周期，控制器按以下公式计算巡航目标：

```text
target path speed = CNCASpeed × (CNCAPercents/100) × (CNCASpeedPer/100) × (segment speed factor/100)
```

并将路径速度 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 向该目标斜坡变化：

- 当路径速度低于目标时，每个周期以当前加速度（[CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md)）提升，钳位至目标值。
- 达到目标后以该速度巡航。
- 根据剩余距离与段长度 [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) 的减速距离前瞻计算，以当前减速度（[CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)）强制降速，使路径速度在段端点恰好到达段末速度 [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md)。

若段过短而无法达到目标速度，则速度曲线呈三角形，`CNCASpeed` 永远不会被实际达到。若收到暂停或停止请求，目标将被强制设为零，路径随之减速。

控制器每个周期重新计算上述因子，因此在路径运行过程中修改 `CNCAPercents` 或 `CNCASpeedPer` 将在下一周期重新设定路径速度目标。合成巡航速度由几何关系分配给各成员轴，因此任何单个成员轴的速度不一定等于路径速度——只有几何合速度才等于路径速度（由 [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) 索引 2 报告）。

### CNCB 说明

`CNCBSpeed` 是独立第二 CNC 组的等效机制。

## 示例

```text
ACNCASpeed          ; 读取 A 组当前活动段的期望路径速度
ACNCBSpeed          ; 读取 B 组的期望路径速度
```

## 另请参阅

- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — 动态速度及加减速缩放
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — 仅速度百分比覆盖
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — 向此速度斜坡变化的指令路径速度
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — 段末速度
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — 实际合速度
