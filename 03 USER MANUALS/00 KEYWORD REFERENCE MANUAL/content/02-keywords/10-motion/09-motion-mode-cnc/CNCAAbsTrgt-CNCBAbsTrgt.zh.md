---
summary: 当前活动 CNC 路径段沿路径的运动距离。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAAbsTrgt/CNCBAbsTrgt

当前活动 CNC 路径段沿路径的运动距离。

## 概述

`CNCAAbsTrgt`（及其在第二 CNC 组上的对应项 `CNCBAbsTrgt`）以用户单位报告**当前活动 CNC 段**沿路径的长度。路径位置参考 [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) 从段起点的零值递增，直至段终点的 `CNCAAbsTrgt`，因此该值是当前活动段速度曲线的运行终点。

CNC 模式沿路径运行协调的多轴运动，路径以段列表（FIFO）的形式流式传输到控制器。`CNCAAbsTrgt` 为只读参数，反映当前正在执行的段；每当路径推进到下一段时，该值随之更新。

## 工作原理

当新段变为活动状态时，控制器根据段数据和成员轴端点解算其路径长度：

- **直线段** — 控制器计算各成员轴的行程（段终点减去每个成员轴的起始位置），并取该位移矢量的欧式（直线）长度。单个成员轴时，简化为该轴的绝对行程。
- **弧线段** — 路径长度为以编程圆心为基准，从起始角到终止角所扫过的弧长。

解算出的长度即为 `CNCAAbsTrgt`。路径速度曲线（参见 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md)、[CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md)、[CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)）以该长度为基准生成：段的减速点由距 `CNCAAbsTrgt` 的剩余距离与当前减速度推算，使得路径速度在 `CNCAPosRef` 到达 `CNCAAbsTrgt` 时恰好降至段末速度。

路径坐标在内部以高于用户单位的精度累积，以防各段之间的分数路径运动产生漂移；一段末尾未消耗的 `CNCAAbsTrgt` 余量将传递到下一段起点，从而使路径在混合转角处保持连续。

`CNCAAbsTrgt` 仅在直线或弧线运动段变为活动状态时更新。非运动段类型（延时、等待、设置位置、滤波器配置）不推进路径，也不改变 `CNCAAbsTrgt`，因此在这些段等待处理期间，该值继续保持最近一次运动段的长度。

### CNCB 说明

`CNCBAbsTrgt` 是应用于第二 CNC 组的相同机制。两组完全独立：各自跟踪其当前活动段长度、路径参考和速度曲线。

## 示例

```text
ACNCAAbsTrgt        ; 读取 A 组当前活动段路径长度
ACNCBAbsTrgt        ; 读取 B 组当前活动段路径长度
```

## 另请参阅

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — 从 0 递增至 `CNCAAbsTrgt` 的路径位置
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — 路径位置每周期的变化量（路径速度）
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 当前活动段的指令路径速度
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 已排队的段数据
