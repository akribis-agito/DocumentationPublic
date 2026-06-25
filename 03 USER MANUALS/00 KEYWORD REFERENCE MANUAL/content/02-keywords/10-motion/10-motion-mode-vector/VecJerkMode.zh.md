---
keyword: VecJerkMode
summary: 选择向量运动急动限制的应用方式：0 为梯形曲线，1 为急动限制 S 形曲线。
availability:
  standalone: []
  central-i:
  - v5
can_code: 755
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# VecJerkMode

选择向量运动急动限制的应用方式：0 为梯形曲线，1 为急动限制 S 形曲线。

> 仅适用于 v5（central-i）。

## 概述

`VecJerkMode` 用于选择向量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）所使用的路径速度规划器。当该模式关闭时，路径速度遵循梯形曲线，加速度在拐角处可以瞬间改变。当该模式开启时，路径速度遵循急动限制 S 形曲线，其加速度在起始和结束时分别按 [VecJerkInAcc](VecJerkInAcc.md) 和 [VecJerkInDec](VecJerkInDec.md) 指定的速率进行斜坡过渡，从而减少加减速拐角处的机械冲击。

该参数为轴相关参数，保存至闪存。由于控制器在运动开始时读取该值以选择规划器，因此在轴运动过程中不能更改。

这是 v5 针对向量运动的急动控制方案，以用户单位表示的显式急动限制形式体现，独立于传统的 [VecJerk](VecJerk.md)（0-9）平滑选择器。

## 工作原理

`VecJerkMode` 在 `Begin` 时读取，并作用于驱动所有成员轴的单一路径速度（参见 [VecSpeed](VecSpeed.md)）：

| 值 | 路径曲线 |
|----|----|
| 0 | 梯形曲线（默认）。路径速度以 [VecAccel](VecAccel.md) 线性加速，以 [VecSpeed](VecSpeed.md) 巡航，再以 [VecDecel](VecDecel.md) 线性减速。加速度在拐角处突变。[VecJerkInAcc](VecJerkInAcc.md) 和 [VecJerkInDec](VecJerkInDec.md) 不起作用。 |
| 1 | 急动限制 S 形曲线。路径速度通过限制加速度变化率的规划器处理，梯形的拐角被平滑化。加速度以急动限制 [VecJerkInAcc](VecJerkInAcc.md) 斜坡上升，以 [VecJerkInDec](VecJerkInDec.md) 斜坡下降，同时 [VecAccel](VecAccel.md) 和 [VecDecel](VecDecel.md) 仍限制加速度和减速度的幅值。 |

由于曲线作用于**合成**路径速度，急动限制同时惠及协调路径上的所有成员轴。模式开启时，运动在 S 形曲线规划器完成其最终段时视为结束；模式关闭时，在路径参考以足够低的路径速度到达目标点时结束。

模式在运动期间固定不变。如需切换规划器，请在发出 `Begin` 之前更改 `VecJerkMode`。

## 示例

```text
AVecJerkMode=0       ; 梯形路径曲线（默认）
AVecJerkMode=1       ; 急动限制 S 形路径曲线
AVecJerkMode         ; 读取当前值
```

## 另请参阅

- [VecJerkInAcc](VecJerkInAcc.md) — 加速阶段的急动限制
- [VecJerkInDec](VecJerkInDec.md) — 减速阶段的急动限制
- [VecAccel](VecAccel.md) — 向量加速度
- [VecDecel](VecDecel.md) — 向量减速度
- [VecJerk](VecJerk.md) — 传统 0-9 急动平滑选择器
