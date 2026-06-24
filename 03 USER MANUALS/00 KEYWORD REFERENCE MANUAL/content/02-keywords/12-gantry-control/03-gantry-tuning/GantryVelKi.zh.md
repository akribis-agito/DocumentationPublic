---
keyword: GantryVelKi
summary: 龙门偏摆速度环的积分增益。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 657
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# GantryVelKi

龙门偏摆速度环的积分增益。

## 概述

`GantryVelKi` 是龙门速度环的积分增益。当龙门模式激活时（参见 [GantryOn](../01-general-variables/GantryOn.md)），它的作用等同于普通 [VelKi](../../11-control-tuning/04-velocity-control/00-overview.md) 在各轴速度环中的作用。比例增益 [GantryVelGain](GantryVelGain.md) 响应当前的龙门速度误差，而 `GantryVelKi` 则作用于累积速度误差，从而消除比例项留下的稳态偏差。该参数为轴相关的可读写参数，保存至闪存，可在任何时刻修改，包括运动中和电机使能状态下。该参数按轴对中的每根轴分别保持：第一根轴运行共模（线性）龙门环，第二根轴运行偏摆（相位）环，各自使用各自的 `GantryVelKi` 值。

## 工作原理

龙门速度误差是龙门位置环输出的速度指令与龙门速度反馈（[GantryVel](GantryVel.md)）之差——第一根轴为共模（线性）速度，第二根轴为差模（偏摆/相位）速度：

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

控制器将比例项（$\text{VelErr} \cdot$ [GantryVelGain](GantryVelGain.md)）乘以 `GantryVelKi` 及一个固定的内部积分缩放因子，然后在每个控制周期将其累加到速度积分器中（当抗积分饱和钳位激活时，累加暂停，避免在电流指令饱和时积分继续增大）：

$$
\text{Integral} \mathrel{+}= (\text{VelErr} \cdot \text{GantryVelGain}) \cdot \text{GantryVelKi} \cdot k_i
$$

比例项与积分项相加并缩放，形成速度 PI 输出；经速度滤波器和前馈处理后，成为龙门电流指令（[CurrRef](../../09-current-and-voltage/02-motor-variables/CurrRef.md)）；线性（共模）和偏摆（相位）指令随后合并并分配至两台龙门电机。

该值无量纲，允许范围为 0 至 100000，默认值为 100（在龙门增益为 6 元素增益调度数组的控制器上，类型遵循关键字属性，范围仍为 0 至 100000）。值为 0 时，龙门速度环的积分作用被禁用。

## 示例

```text
AGantryVelKi[1]=50     ; set gantry velocity integral gain (first gain set)
AGantryVelKi[1]        ; read the current gain
```

在 v4 上，该关键字为单值（`AGantryVelKi=50`）；在 v5 上，它是一个 6 元素增益调度数组，寻址为 `AGantryVelKi[1]`–`AGantryVelKi[5]`。

### 边界情况

- **龙门关闭** — 写入被接受；在 [GantryOn](../01-general-variables/GantryOn.md) = 1 之前，增益无效。
- **增益为零** — 禁用积分作用；龙门速度环仅保留比例加前馈。
- **按轴分配** — 龙门轴对中的每根轴使用各自的 `GantryVelKi`（第一根轴对应线性/共模环，第二根轴对应偏摆/相位环）。非龙门轴上，该值被接受但不使用。
- **超出范围** — 超出 `0`–`100000` 范围的值在 v4 和 v5 上均被拒绝（v5 每元素范围同为 `0`–`100000`）。
- **接入时的积分器处理** — 在龙门接入时，两轴的速度环积分器被重新合并为共模（半和）和差模（半差）部分，以实现无扰动切换。
- **保存** — 可保存至闪存。
- **平台** — v5 以 6 元素增益调度 `float32` 数组存储；v4 以单个 `int32` 存储。

## 另请参阅

- [GantryVelGain](GantryVelGain.md) — 偏摆速度环比例增益
- [GantryPosKi](GantryPosKi.md) — 偏摆位置环积分增益
