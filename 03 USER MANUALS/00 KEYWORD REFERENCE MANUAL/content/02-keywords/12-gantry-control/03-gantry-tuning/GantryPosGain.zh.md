---
keyword: GantryPosGain
summary: 龙门偏摆校正控制器的位置比例增益。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 654
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100000
  default: 100
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    type: array
    array_size: 6
    data_type: float32
    range:
    - 0
    - 1000000
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryPosGain

龙门偏摆校正控制器的位置比例增益。

## 概述

`GantryPosGain` 是龙门偏摆校正环的位置比例增益。当龙门模式激活时（参见 [GantryOn](../01-general-variables/GantryOn.md)），控制器为龙门轴运行专用的偏摆位置/速度控制器，替代单轴位置/速度控制器，`GantryPosGain` 在其中扮演普通 [PosGain](../../11-control-tuning/03-position-control/00-overview.md) 在普通环路中的角色。它是一个轴相关参数，保存至闪存，可在任何时候修改，包括运动中和电机使能时。

## 工作原理

在龙门模式下，每个轴根据其龙门反馈（[GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md)）而非单轴反馈来计算位置误差——主轴为共模（线性）反馈，偏摆轴为差模（偏摆）反馈：

$$
\text{PosErr} = \text{PosRef}_{\text{shaped}} - \text{GantryFdbk}
$$

`GantryPosGain` 对此位置误差进行缩放，生成传入匹配速度环的速度指令（内置速度跟踪前馈项在其上叠加，与普通位置环完全相同）：

$$
\text{VelRef} = \text{PosErr} \cdot \text{GantryPosGain} + \frac{\text{PosRef} \cdot \text{VelTrackFact}}{1024}
$$

增大 `GantryPosGain` 会提高单位位置误差所产生的速度指令（及相应的校正电流）。该速度指令进入由 [GantryVelGain](GantryVelGain.md) / [GantryVelKi](GantryVelKi.md) 设定的速度 PI 环，其输出构成该轴电机电流指令（[CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)）的一部分。偏摆校正参考本身由 [GantryYawRef](../01-general-variables/GantryYawRef.md) 设定。

该值无量纲。允许范围为 0 至 100000，默认值为 100（在龙门增益为 6 元素增益调度数组的控制器上，上限范围扩展；详见关键字属性）。值为 0 时禁用该环路的位置比例作用。

## 示例

```text
AGantryPosGain=200  ; set yaw position proportional gain
AGantryPosGain     ; read the current gain
```

### 边界情况

- **龙门关闭**（[GantryOn](../01-general-variables/GantryOn.md) = 0）— 偏摆环未运行；写入被接受，但在龙门模式启用之前增益无效。
- **逐轴生效** — 每个龙门成员轴使用其自身的 `GantryPosGain`：主轴（共模/线性）在线性位置环中应用其值，偏摆轴在偏摆位置环中应用其值。当该轴处于龙门模式时逐轴读取（v4 和 v5 均如此）；v5 上每轴还支持增益调度。非龙门轴的写入被接受但不使用。
- **电机关闭** — 被接受；该值在龙门启用前持续保留。
- **超出范围** — 超出 `0`–`100000`（v4）/ `0`–`1000000`（v5）的值将被拒绝。
- **零增益** — 禁用位置比例作用；偏摆环仅依靠积分和前馈运行，跟踪性能较差。
- **保存** — 可保存至闪存。
- **平台** — v5 以 6 元素 `float32` 数组存储以支持增益调度；v4 以单个 `int32` 存储。两个分支均在偏摆环中使用相同的公式。

## 另请参阅

- [GantryPosKi](GantryPosKi.md) — 偏摆位置环积分增益
- [GantryVelGain](GantryVelGain.md) — 偏摆速度环比例增益
- [GantryAccFFW](GantryAccFFW.md) — 加速度前馈增益
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — 偏摆校正参考值
