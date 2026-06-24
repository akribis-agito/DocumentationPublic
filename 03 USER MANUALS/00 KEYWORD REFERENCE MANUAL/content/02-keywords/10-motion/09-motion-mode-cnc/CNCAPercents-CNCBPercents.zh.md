---
summary: 实时缩放 CNC 路径速度及加减速度。
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# CNCAPercents/CNCBPercents

实时缩放 CNC 路径速度及加减速度。

## 概述

`CNCAPercents`（以及第二 CNC 组上的对应参数 `CNCBPercents`）以百分比形式同时缩放 CNC 路径速度**及**其加减速度。由于同时缩放斜坡和巡航速度，其效果是对整个 CNC 运动的**时间**进行重缩放，同时保持路径几何形状和速度曲线形状不变。

`CNCAPercents` 可随时修改，包括 CNC 运动过程中。如需特定时间缩放，请在启动运动前设置其值。

## 工作原理

每个控制周期，控制器根据编程段值和 `CNCAPercents`（设其值为 `P`，单位为百分比）推导活动路径曲线量：

| 量 | 应用的缩放 |
|----|----|
| 路径速度（[CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md)） | × `P/100`（还 × [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md)/100） |
| 段末速度（[CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md)） | × `P/100` |
| 加速度（[CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md)）和减速度（[CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)） | × `(P/100)²` |
| 加加速度（[CNCAJerk/CNCBJerk](CNCAJerk-CNCBJerk.md)） | × `(P/100)³` |

将速度按 `P/100` 缩放、斜坡按 `P/100` 的平方缩放，正是使运动时长按 `100/P` 缩放同时保持曲线形状（及路径）不变的关键：

- `P = 100`（%）——运动按段队列中定义的值运行。
- `P = 50`（%）——速度减半，加减速度缩小为四分之一，运动时间变为名义时间的两倍。
- `P` 大于 100（%）是允许的，会加快运动速度。

例如，若某段编程 `CNCASpeed = 200000` 用户单位/秒，`CNCAAccel = 100000` 用户单位/秒²，设置 `CNCAPercents = 50` 后，该段以巡航速度 `100000` 用户单位/秒和加速度 `25000` 用户单位/秒² 运行——速度时间曲线保持相同形状，仅时间拉伸为两倍。`CNCAPercents = 200` 则将时间缩短为一半：巡航速度升至 `400000` 用户单位/秒，加速度缩放至 `400000` 用户单位/秒²。

由于该因子每个周期重新应用，在路径进行中修改 `CNCAPercents` 会在下一周期重新定目标速度和斜坡，同时活动段使用梯形（向后兼容）曲线。当活动段运行加加速度限制（S 曲线）曲线时，实时修改不在该段中途应用；而是在下一段开始时生效。此参数的作用范围比 [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) 更广，后者仅缩放速度而不改变斜坡。两者相乘得到净速度因子。

### CNCB 说明

`CNCBPercents` 对独立第二 CNC 组进行相同的缩放。

## 示例

```text
ACNCAPercents=100    ; 以名义编程速度和斜坡运行
ACNCAPercents=50     ; 半速，四分之一加减速度——时间加倍
ACNCBPercents=200    ; 组 B 以名义时间的一半运行
```

## 另请参阅

- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 指令路径速度
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — 速度百分比覆盖（仅速度）
- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) / [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — 同样被缩放的活动段斜坡
