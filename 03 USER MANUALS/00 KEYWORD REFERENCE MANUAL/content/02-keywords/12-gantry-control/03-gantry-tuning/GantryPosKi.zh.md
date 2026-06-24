---
summary: 龙门偏摆位置环的积分增益。
keyword: GantryPosKi
availability:
  standalone: []
  central-i:
  - v5
can_code: 715
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryPosKi

龙门偏摆位置环的积分增益。

## 概述

`GantryPosKi` 是龙门偏摆位置环的积分增益。它是普通位置环积分增益（[PosKi](../../11-control-tuning/03-position-control/00-overview.md)）在偏摆环中的对应项：比例项 [GantryPosGain](GantryPosGain.md) 响应当前的偏摆位置误差，而 `GantryPosKi` 作用于累积的偏摆位置误差，以便随时间消除残余（稳态）偏摆失准。它是一个轴相关参数，可在运动中和电机使能时读写，是控制器在龙门模式激活时（参见 [GantryOn](../01-general-variables/GantryOn.md)）替代普通控制增益的龙门整定增益之一。

## 工作原理

当龙门模式激活时，每个轴根据其龙门反馈（[GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md)）计算位置误差——主轴为共模（线性）反馈，偏摆轴为差模（偏摆）反馈：

$$
\text{PosErr} = \text{PosRef}_{\text{shaped}} - \text{GantryFdbk}
$$

`GantryPosKi` 对该位置误差的积分（累加和）进行缩放。比例部分（[GantryPosGain](GantryPosGain.md)）与该积分部分共同构成传入匹配速度 PI 环（[GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md)）的速度指令，该速度 PI 环的输出成为施加到该轴电机的电流。`GantryPosKi` 与 [GantryPosGain](GantryPosGain.md)、[GantryVelGain](GantryVelGain.md)、[GantryVelKi](GantryVelKi.md)、[GantryAccFFW](GantryAccFFW.md) 和 [GantryVelFFW](GantryVelFFW.md) 属于同一龙门增益组；在支持龙门增益调度的控制器上，六者作为一组同步切换。

该值无量纲。值为 0 时禁用龙门位置环的积分作用。有关特定控制器上的范围和默认值，请参阅关键字属性。

## 示例

```text
AGantryPosKi[1]=0   ; set yaw position integral gain (first gain set)
AGantryPosKi[1]     ; read the current value
```

### 边界情况

- **索引 0** — 无效；有效索引为 `GantryPosKi[1]`–`GantryPosKi[5]`（增益组 1 至 5）。活动组由增益调度选择。
- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）— 写入被接受；在龙门启用之前增益无效。
- **零增益** — 禁用积分作用；偏摆位置环仅以比例 + 前馈方式运行。
- **启用时的积分积累** — 固件在龙门启用时将速度环积分对半分配给主轴/偏摆轴；较大的 `GantryPosKi` 可能在初始稳定过程中使积分快速积累。
- **逐轴生效** — 每个龙门成员轴使用其自身的 `GantryPosKi`：主轴（共模/线性）在线性位置环中应用其值，偏摆轴在偏摆位置环中应用其值。当该轴处于龙门模式时逐轴读取。非龙门轴的写入被接受但不使用。请注意，积分作用仅在位置环包含积分支持的固件版本中有效；不支持时范围为 `0`–`0`（参见关键字属性）。
- **增益组选择** — 活动组由增益调度子系统选择（参见 [ScheduleMode](../../11-control-tuning/01-general-keywords/ScheduleMode.md)）；读取返回活动组存储的值。
- **保存** — 可保存至闪存。
- **平台** — 仅限 v5 Central-i。v4 上不存在 `GantryPosKi`。

## 另请参阅

- [GantryPosGain](GantryPosGain.md) — 偏摆位置环比例增益
- [GantryVelGain](GantryVelGain.md) — 偏摆速度环比例增益
- [GantryVelKi](GantryVelKi.md) — 偏摆速度环积分增益
