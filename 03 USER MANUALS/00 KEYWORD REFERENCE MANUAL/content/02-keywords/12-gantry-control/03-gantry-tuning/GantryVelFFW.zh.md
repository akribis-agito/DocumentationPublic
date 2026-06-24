---
summary: 龙门偏摆校正控制器的速度前馈增益。
keyword: GantryVelFFW
availability:
  standalone: []
  central-i:
  - v5
can_code: 678
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
  - 50000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryVelFFW

龙门偏摆校正控制器的速度前馈增益。

## 概述

`GantryVelFFW` 是龙门速度环的速度前馈增益。它是普通速度前馈（[VelFFW](../../11-control-tuning/05-feedforwards/00-overview.md)）在龙门中的对应项：注入一个与指令速度成比例的电流项，使负载无需等待反馈环积累速度误差即可运动。它是一个轴相关参数，可在运动中和电机使能时读写，是控制器在龙门模式激活时（参见 [GantryOn](../01-general-variables/GantryOn.md)）替代普通控制增益的龙门整定增益之一。它逐轴保存：第一个轴运行线性（共模）龙门环，第二个轴运行偏摆（相位）环，各自使用其自身的 `GantryVelFFW` 值。

## 工作原理

速度前馈仅在位置运行模式下生效。控制器将指令速度（位置参考的变化率）乘以 `GantryVelFFW`，并将结果与加速度前馈项（[GantryAccFFW](GantryAccFFW.md)）一起叠加到速度 PI 输出上，形成电机电流指令（[CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)）：

$$
\text{CurrRef} = \text{VelPIOutput} + (\text{AccFFW term}) + \frac{\text{dPosRef} \cdot \text{GantryVelFFW}}{65536}
$$

由于该项仅依赖于参考轨迹而非速度误差，它在运动过程中提供预见性电流，否则 [GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md) 反馈环须从积累误差中获取。

该值无量纲。默认值为 0（除非配置否则速度前馈关闭）；有关特定控制器上的范围，请参阅关键字属性。`GantryVelFFW` 与其他龙门整定增益属于同一龙门增益组，在支持龙门增益调度的控制器上与它们同步切换。

## 示例

```text
AGantryVelFFW[1]=0  ; set gantry velocity feedforward gain (first gain set)
AGantryVelFFW[1]    ; read the current value
```

### 边界情况

- **索引 0** — 无效；有效索引为 `GantryVelFFW[1]`–`GantryVelFFW[5]`（增益组）。活动组由增益调度选择。
- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）— 写入被接受；在龙门启用之前增益无效。
- **模式错误** — 前馈仅在位置环参考推进时生效；在电流/力专用模式下该项无贡献。
- **零增益** — 禁用龙门速度前馈。
- **逐轴生效** — 龙门配对的每个轴各自使用其 `GantryVelFFW`（第一轴 = 线性/共模环，第二轴 = 偏摆/相位环）。非龙门轴的值被接受但不使用。
- **超出范围** — 超出每元素 `0`–`50000` 的值将被拒绝。
- **保存** — 可保存至闪存。
- **平台** — 仅限 v5 Central-i。v4 上不存在 `GantryVelFFW`。

## 另请参阅

- [GantryVelGain](GantryVelGain.md) — 偏摆速度环比例增益
- [GantryAccFFW](GantryAccFFW.md) — 加速度前馈增益
