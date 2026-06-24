---
summary: 报告 A 组（或 B 组）当前活动 CNC 段的加速度。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAAccel/CNCBAccel

报告 A 组（或 B 组）当前活动 CNC 段的加速度。

## 概述

`CNCAAccel`（及其对应项 `CNCBAccel`）是只读参数，以用户单位每秒平方报告 A 组（或 B 组）当前活动 CNC 段路径速度曲线的加速度。它反映压入队列的段中编码的加速度。该参数为非轴只读参数，不保存至闪存。

## 工作原理

CNC 模式沿路径运行单一速度曲线。当路径速度 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 低于指令巡航速度 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) 时，控制器每个周期将其提高 `CNCAAccel × （控制周期时间）`，直到达到巡航速度。`CNCAAccel` 是该上升斜坡所用的速率；它作用于**路径**（合成）速度，而非任何单个成员轴——几何关系随后将合成加速度分配到各成员轴。

每个周期实际使用的有效加速度，是报告的段值乘以实时时间缩放因子 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 的平方：有效加速度 = `CNCAAccel × (CNCAPercents/100)²`。以速度因子的平方缩放斜坡，使得速度曲线形状（从而路径形状）保持不变，同时 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 对运动时间进行缩放。纯速度倍率 [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) **不**缩放加速度。

该参数与 [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)（制动速率）配对使用。底层段数据通过 [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) 提供，并保存在 [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) 中。

### CNCB 说明

`CNCBAccel` 报告独立第二 CNC 组的相同量。

## 示例

```text
ACNCAAccel          ; 读取 A 组当前活动段加速度
ACNCBAccel          ; 读取 B 组当前活动段加速度
```

## 另请参阅

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — 当前活动段减速度
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 该斜坡所趋向的巡航速度
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — 以其因子的平方缩放加速度
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 已排队的段数据
