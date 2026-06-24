---
keyword: VecAccel
summary: 矢量加速度（用户单位/s^2），将合成速度斜坡加速至 VecSpeed。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 636
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 100.0
    - 686700000000.0
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# VecAccel

矢量加速度（用户单位/s^2），将合成速度斜坡加速至 VecSpeed。

## 概述

`VecAccel` 设置协调多轴矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的加速度，单位为用户单位每秒平方。它定义合成（矢量）速度向 [VecSpeed](VecSpeed.md) 斜坡加速的快慢，作用于整条路径而非某一单轴。该参数为轴相关参数，保存至闪存，可在任何时候（包括运动中）修改。

`VecAccel` 控制加速斜坡；[VecDecel](VecDecel.md) 控制受控减速斜坡。默认情况下路径曲线为梯形，加速度在斜坡开始时即刻跳变至 `VecAccel`；路径的 S 曲线平滑通过 [VecJerkMode](VecJerkMode.md) = 1 单独启用，并由 [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) 进行整定。

## 工作原理

矢量运动沿几何路径运行单一速度曲线（参见 [VecSpeed](VecSpeed.md)）；`VecAccel` 是该路径速度允许上升的速率。在默认梯形路径曲线下，规划器每个控制周期将路径速度递增 `VecAccel × Ts`（其中 `Ts` 为控制周期时间），直至达到 [VecSpeed](VecSpeed.md)：

$$
v_k = v_{k-1} + \text{VecAccel} \cdot T_s ,\qquad v_k \le \text{VecSpeed}
$$

减速侧单独处理：每个周期，规划器还根据到 [VecAbsTrgt](VecAbsTrgt.md) 的剩余路径距离，计算仍能使用 [VecDecel](VecDecel.md) 及时制动至停止的最高路径速度，并将路径速度钳位至该值。因此，`VecAccel` 设定梯形的前沿斜率，`VecDecel` 设定后沿斜率。当启用 S 曲线平滑（[VecJerkMode](VecJerkMode.md) = 1，Central-i v5）时，`VecAccel` 作为加速度约束传递给急动限制路径规划器，急动限值取自 [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md)。

由于斜坡作用于**合成**路径速度，任一成员轴上的表观加速度为 `VecAccel` 乘以该轴在路径中的分量（直线运动时为方向余弦）。该值每个周期重新读取，因此运动中途修改将在下一个周期生效。

## 示例

```text
AVecAccel=100000     ; vector acceleration (user units/s^2, default)
AVecAccel           ; read the current value
```

## 另请参阅

- [VecDecel](VecDecel.md) — 矢量减速度
- [VecSpeed](VecSpeed.md) — 目标合成速度
- [VecJerkMode](VecJerkMode.md) — 启用矢量路径 S 曲线平滑
