---
summary: 报告组 A（或 B）当前活动 CNC 段路径速度曲线的加加速度（平滑）。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAJerk/CNCBJerk

报告组 A（或 B）当前活动 CNC 段路径速度曲线的加加速度（急动度）。

## 概述

`CNCAJerk`（以及第二 CNC 组上的对应参数 `CNCBJerk`）是只读参数，以用户单位每秒三次方报告当前活动 CNC 段路径速度曲线的加加速度（加速度的变化率）。加加速度对速度斜坡的拐角进行圆滑处理，使路径遵循更平滑的 S 曲线，而非加速度的突变。该值反映推入队列的段中编码的加加速度。该参数为非轴只读参数，不保存至闪存。

## 工作原理

CNC 路径速度曲线由指令路径速度 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md)、斜坡 [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) 和 [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) 以及此加加速度限值共同构成：

- 当活动段的加加速度**大于等于 10** 时，规划器应用真实加加速度限制，产生 S 曲线加速和减速阶段。
- 当加加速度为 **0 到 9** 时，段以向后兼容模式运行，使用梯形（线性）加减速斜坡，不进行加加速度平滑。

加加速度由时间缩放因子 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 的三次方实时缩放（`CNCAJerk × (CNCAPercents/100)³`），与指令速度按一次方缩放、加减速斜坡按二次方缩放的方式一致——在运动时间被重缩放时保持曲线形状及路径不变。

### CNCB 说明

`CNCBJerk` 以相同方式报告独立第二 CNC 组活动段所携带的加加速度值。但需注意，加加速度限制（S 曲线）路径曲线目前仅适用于组 A：组 B 报告段的加加速度值，但始终以向后兼容的梯形曲线运行，因此其值不改变速度斜坡的形状。

## 示例

```text
ACNCAJerk           ; 读取组 A 活动段的加加速度值
ACNCBJerk           ; 读取组 B 活动段的加加速度值
```

## 另请参阅

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — 活动段加速度
- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — 活动段减速度
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 指令路径速度
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — 实时时间缩放（加加速度按其因子的三次方缩放）
