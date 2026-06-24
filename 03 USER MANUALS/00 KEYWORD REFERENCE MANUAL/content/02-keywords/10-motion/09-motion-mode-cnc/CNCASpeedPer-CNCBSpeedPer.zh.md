---
summary: 应用于 CNC 运动组 A（或 B）的速度百分比覆盖值。
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# CNCASpeedPer/CNCBSpeedPer

应用于 CNC 运动组 A（或 B）的速度百分比覆盖值。

## 概述

`CNCASpeedPer`（以及对应的 `CNCBSpeedPer`）是 CNC 组 A（或 B）的动态速度百分比覆盖值，以百分比表示。将其设为 `100` 时按编程段速度运行；较低值等比例降低整个路径速度，较高值则加快速度，无需重新编程段队列。该参数为非轴参数，不保存至闪存，可随时修改，包括运动过程中。

与 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 的根本区别在于：**`CNCASpeedPer` 仅缩放路径速度**——不改变加速度或减速度。因此降低该值会减小巡航进给速率，而斜坡保持与编程一致。

## 工作原理

每个控制周期，控制器将指令路径速度 [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) 乘以 `CNCASpeedPer/100`（以及 [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) 因子和逐段速度因子），形成路径速度所趋近的巡航目标。由于只有**速度**目标受 `CNCASpeedPer` 缩放，加减速度保持不变，降低 `CNCASpeedPer` 会减小巡航进给速率，但路径以相同斜坡速率加速和减速至该较低的巡航速度。

拐角/前瞻所使用的段末速度同样受相同速度因子缩放，因此在修改覆盖值时拐角混合保持一致。

这与 `CNCAPercents` 不同——后者同时缩放速度**和**加减速斜坡（从而等效缩放整个运动的时间轴）。两个因子相乘，因此净速度缩放为 `(CNCAPercents/100) × (CNCASpeedPer/100)`。

### CNCB 说明

`CNCBSpeedPer` 是独立第二 CNC 组的等效覆盖值。

## 示例

```text
ACNCASpeedPer=100    ; run at programmed segment speeds
ACNCASpeedPer=50     ; half the feed rate, same accel/decel ramps
ACNCBSpeedPer=120    ; 20 % faster on group B
```

## 另请参阅

- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — 被缩放的指令路径速度
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — 同时缩放速度和加减速（重新缩放时间轴）
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — 实际合速度
