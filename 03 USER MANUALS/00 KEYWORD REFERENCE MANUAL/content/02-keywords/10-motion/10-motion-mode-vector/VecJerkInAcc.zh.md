---
keyword: VecJerkInAcc
summary: 限制加加速度（用户单位）用于加加速度限制矢量运动的加速阶段。
language: zh-CN
availability:
  standalone: []
  central-i:
  - v5
can_code: 756
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 10000.0
  - 1.0e+20
  default: 100000000.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# VecJerkInAcc

限制加加速度（用户单位）用于加加速度限制矢量运动的加速阶段。

> 仅适用于 v5（central-i）。

## 概述

`VecJerkInAcc` 设置加加速度限制矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）中合成速度**上升**期间所使用的加加速度限值。加加速度是加速度的变化率，因此该值限制了路径加速度在运动加速至 [VecSpeed](VecSpeed.md) 的过程中建立和消退的速率。较小的值使速度曲线的前沿拐角更平缓（冲击更小，运动时间略长）；较大的值趋近于梯形的尖锐拐角。

该参数为轴相关参数，保存至闪存，以用户单位表示，可随时更改，包括运动过程中。它作用于整体路径，而非单个轴。

`VecJerkInAcc` 仅在 [VecJerkMode](VecJerkMode.md) = 1 时生效；模式关闭时，矢量运动使用梯形曲线，该值被忽略。配套关键字 [VecJerkInDec](VecJerkInDec.md) 设置减速阶段的加加速度限值。

## 工作原理

当 [VecJerkMode](VecJerkMode.md) = 1 时，路径速度由 S 曲线规划器生成，该规划器以加速度限值 [VecAccel](VecAccel.md)、减速度限值 [VecDecel](VecDecel.md) 以及两个加加速度限值——加速阶段的 `VecJerkInAcc` 和减速阶段的 [VecJerkInDec](VecJerkInDec.md)——作为输入。`VecJerkInAcc` 控制路径加速度从零升至 [VecAccel](VecAccel.md) 再降回零的 S 曲线段（即速度爬升至 [VecSpeed](VecSpeed.md) 的过程）。由于它整形的是**合成**路径速度，平滑效果由协调路径上的每个成员轴共享。

该值在 `Begin` 时读取以初始化规划器，并在每个控制周期重新应用，因此运动中途所做的更改将在下一个周期生效。

有效加加速度存在内部上限。若所请求的加加速度足够大，使得加速度在约两个控制周期内即可达到其限值，则控制器会将其钳位至该上限。因此，设置非常大的 `VecJerkInAcc` 会使加速斜坡近似立即完成（接近梯形拐角），而不会产生超出范围的结果。

可用范围和默认值在文档头部给出；最小值为一个小正数，因此模式开启时加速阶段的加加速度限制始终为有限值。

## 示例

```text
AVecJerkInAcc=100000000   ; jerk limit for the acceleration phase (user units, default)
AVecJerkInAcc=20000000    ; gentler acceleration corners
AVecJerkInAcc             ; read the current value
```

## 另请参阅

- [VecJerkMode](VecJerkMode.md) — 选择是否应用加加速度限制
- [VecJerkInDec](VecJerkInDec.md) — 减速阶段的加加速度限值
- [VecAccel](VecAccel.md) — 矢量加速度
- [VecSpeed](VecSpeed.md) — 目标合成速度
