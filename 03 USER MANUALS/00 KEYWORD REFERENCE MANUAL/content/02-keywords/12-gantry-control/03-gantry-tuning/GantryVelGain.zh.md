---
keyword: GantryVelGain
summary: 龙门偏摆校正控制器的速度比例增益。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 656
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
    - 100000000
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryVelGain

龙门偏摆校正控制器的速度比例增益。

## 概述

`GantryVelGain` 是龙门速度环的比例增益。当龙门模式激活时（参见 [GantryOn](../01-general-variables/GantryOn.md)），它扮演普通 [VelGain](../../11-control-tuning/04-velocity-control/00-overview.md) 在单轴速度环中的角色，对龙门速度误差进行缩放以形成校正电流指令。它是一个轴相关参数，保存至闪存，可在任何时候修改，包括运动中和电机使能时。它逐轴保存：第一个轴运行线性（共模）龙门环，第二个轴运行偏摆（相位）环，各自使用其自身的 `GantryVelGain` 值。

## 工作原理

在龙门模式下，速度误差为龙门位置环的速度指令与龙门速度反馈（[GantryVel](GantryVel.md)）之差，而非单轴速度之差。反馈在配对第一轴为共模（线性）速度，在第二轴为差模（偏摆/相位）速度：

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

`GantryVelGain` 对该速度误差进行缩放，生成速度 PI 控制器的比例项：

$$
P = \text{VelErr} \cdot \text{GantryVelGain}
$$

该比例项与由 [GantryVelKi](GantryVelKi.md) 缩放的积分项求和；合并后的 PI 输出经速度环滤波器和内部缩放系数处理，最终与前馈项叠加形成龙门电流指令（[CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)）。线性（共模）和偏摆（相位）电流指令随后被组合并分配至两台龙门电机。增大 `GantryVelGain` 会提高单位速度误差所产生的电流。

该值无量纲。允许范围为 0 至 100000，默认值为 100（在龙门增益为 6 元素增益调度数组的控制器上，上限范围扩展至 100000000；详见关键字属性）。值为 0 时禁用龙门速度环的比例作用。

## 示例

```text
AGantryVelGain[1]=150  ; set gantry velocity proportional gain (first gain set)
AGantryVelGain[1]      ; read the current gain
```

在 v4 上该关键字为单值（`AGantryVelGain=150`）；在 v5 上为 6 元素增益调度数组，寻址方式为 `AGantryVelGain[1]`–`AGantryVelGain[5]`。

### 边界情况

- **龙门关闭** — 写入被接受；在 [GantryOn](../01-general-variables/GantryOn.md) = 1 之前增益无效。
- **零增益** — 禁用速度比例作用；龙门速度环仅以积分 + 前馈方式运行。
- **逐轴生效** — 龙门配对的每个轴各自使用其 `GantryVelGain`（第一轴 = 线性/共模环，第二轴 = 偏摆/相位环）。非龙门轴的值被接受但不使用。
- **超出范围** — 超出 `0`–`100000`（v4）/ `0`–`100000000`（v5 单元素）的值将被拒绝。
- **保存** — 可保存至闪存。
- **平台** — v5 以 6 元素增益调度 `float32` 数组存储；v4 以单个 `int32` 存储。两个分支使用相同的公式。

## 另请参阅

- [GantryVelKi](GantryVelKi.md) — 偏摆速度环积分增益
- [GantryPosGain](GantryPosGain.md) — 偏摆位置环比例增益
- [GantryAccFFW](GantryAccFFW.md) — 加速度前馈增益
- [GantryVelFFW](GantryVelFFW.md) — 速度前馈增益
