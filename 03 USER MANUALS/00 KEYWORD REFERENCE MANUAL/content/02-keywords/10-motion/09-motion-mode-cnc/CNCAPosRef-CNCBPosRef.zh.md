---
summary: 当前活动段沿 CNC 路径的期望位置。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPosRef/CNCBPosRef

当前活动段沿 CNC 路径的期望位置。

## 概述

`CNCAPosRef`（及其在第二 CNC 组上的对应项 `CNCBPosRef`）是 CNC 运动沿路径的运行位置参考，以用户单位表示。它从活动段起始处的零值开始，在该段结束时增长至 [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md)。其每个控制周期的变化量（路径速度）由 [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 报告。

`CNCAPosRef` 是驱动组内每个成员轴的单一主坐标，正是这一机制使各轴在路径上保持精确协调。

## 工作原理

CNC 模式沿路径运行**一个**速度曲线，而非为每个轴单独生成曲线。每个控制周期，控制器推进一个标量路径速度（由 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md)、[CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md)、[CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) 整形），并将其累积至 `CNCAPosRef`。该单一数值从 0 向活动段长度递增，然后由每个成员轴从中派生其位置：

- **直线段** — 对于每个成员轴，控制器将 `CNCAPosRef` 乘以该轴的方向余弦（即该轴在直线位移中所占的份额：该轴行程除以段长度），再加上轴起始位置。因此所有轴共同描绘出同一条直线。
- **圆弧段** — `CNCAPosRef` 除以半径得到从起始角度（沿编程方向）扫过的角度；两个成员轴的位置分别为圆心坐标加上半径乘以该角度的余弦值/正弦值。

累积运算在内部以高于用户单位的精度进行，使分数路径运动不会产生漂移；`CNCAPosRef` 通过将该值缩放回用户单位来报告。在将路径位置分配到各轴时，同样使用了额外精度，从而使各轴在路径上保持亚计数精度。可在参考分配至各轴之前应用可选的路径位置平滑滤波器（参见 [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md)）。启用该滤波器时，`CNCAPosRef` 报告的是经过滤波的路径参考——即馈送至成员轴的相同平滑值——而非滤波前的原始曲线；关闭滤波器时，两者相同。同样，[CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) 是该报告（经滤波）参考每个控制周期的变化量。

当一个段结束时，任何剩余的分数路径距离将被带入下一段，使路径在混合转角处保持连续；在最后一段（或请求停止时），路径被精确驱动至端点，成员轴被对齐至其解算出的终止位置。在组处于活动状态期间，[MotionStat](../05-motion-status/MotionStat.md) 的第 11 位（组 A）或第 14 位（组 B）在每个成员轴上置位。

### CNCB 说明

`CNCBPosRef` 是第二个独立 CNC 组上相同的机制，拥有其自己的路径累加器和成员轴。

## 示例

```text
ACNCAPosRef         ; 读取 A 组当前路径位置
ACNCBPosRef         ; 读取 B 组当前路径位置
```

## 另请参阅

- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — 活动段长度（`CNCAPosRef` 的终止值）
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — `CNCAPosRef` 每个控制周期的变化量（路径速度）
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — 从成员轴测量的实际合成速度
- [MotionStat](../05-motion-status/MotionStat.md) — CNCA 成员/活动位 10–12，CNCB 位 13–15
