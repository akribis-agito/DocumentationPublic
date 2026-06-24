---
summary: 报告 CNC 组 A（或 B）成员实际合路径速度的只读数组。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAVel/CNCBVel

报告 CNC 组 A（或 B）成员实际合路径速度的只读数组。

## 概述

`CNCAVel`（以及对应的 `CNCBVel`）是一个只读数组，报告参与 A 组（或 B 组）CNC 运动的各轴的**实际合速度**，由成员轴的实测速度计算得出。该参数为非轴只读数组，不保存至闪存。与 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md)（来自规划器的*指令*路径速度）不同，`CNCAVel` 由成员轴的实际运动状态计算。

## 工作原理

每个控制周期，控制器由各成员轴速度计算组的合速度（欧几里得速度）：对当前属于该组成员的每个轴的速度平方求和后取平方根。这是多轴速度矢量的幅值，即沿路径的实际进给速率。

该数组报告：

| 索引 | 含义 |
|----|----|
| 1 | 未使用。 |
| 2 | 瞬时合速度——各成员轴速度平方和的平方根。 |
| 3 | 平滑合速度——索引 2 的 32 周期移动平均值。 |

数组采用 1 索引，因此首个有效读取为 `CNCAVel[2]`。索引 2 用于实时合进给速率，索引 3 用于噪声较小的读取（例如显示用途）。只有被标记为该组成员的轴（[MotionStat](../05-motion-status/MotionStat.md) A 组为位 10，B 组为位 13）才计入求和。

该数组测量的合速度由指令路径速度 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) 经动态缩放因子 [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) 和 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 作用后驱动。

### CNCB 说明

`CNCBVel` 报告独立第二 CNC 组的等效合速度。

## 示例

```text
ACNCAVel[2]         ; instantaneous resultant velocity (arrays are 1-indexed)
ACNCAVel[3]         ; 32-cycle moving-average resultant velocity
```

## 另请参阅

- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — 来自规划器的指令路径速度
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 当前活动段的指令路径速度
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — 速度百分比覆盖
- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — 活动段加速度
