---
keyword: VecJerk
summary: 矢量运动的加加速度限制选择（0-9），将合成速度平滑为 S 曲线。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 639
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 9
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-30'
doc_revision: '2026.06'
---
# VecJerk

矢量运动的加加速度限制选择（0-9），将合成速度平滑为 S 曲线。

## 概述

`VecJerk` 是矢量运动（[MotionMode](../02-motion-configuration/MotionMode.md) = 16）的旧版加加速度限制选择器（`0`-`9`）。在当前固件版本中，它**不**对矢量路径进行整形：沿路径的 S 曲线平滑由 [VecJerkMode](VecJerkMode.md) 启用，并由 [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) 调整。`VecJerk` 为轴相关参数，保存至闪存，在轴运动过程中不可更改。

## 工作原理

`VecJerk` 是旧版 `0`-`9` 选择器，在当前固件中**对矢量路径无效**。矢量路径曲线由其他关键字选择和整形：

- 矢量路径默认为梯形——路径速度以 [VecAccel](VecAccel.md) 线性加速，以 [VecSpeed](VecSpeed.md) 巡航，以 [VecDecel](VecDecel.md) 线性减速，因此加速度在拐角处瞬间变化。
- 沿路径的 S 曲线整形由 [VecJerkMode](VecJerkMode.md) = 1 启用，并由 [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) 调整，使梯形的拐角处加速度本身平滑过渡。

`VecJerk` 保留以维持兼容性；请使用 [VecJerkMode](VecJerkMode.md) 配合 [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) 对矢量路径进行整形。在依赖 `VecJerk` 进行矢量运动之前，请针对您的固件版本验证实际行为。

## 示例

```text
AVecJerk=0           ; legacy selector, default (no effect on the vector path)
AVecJerk=9           ; highest legacy setting (no effect on the vector path)
```

## 另请参阅

- [VecJerkMode](VecJerkMode.md) — 启用矢量路径的 S 曲线整形
- [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) — 调整加速/减速斜坡上的 S 曲线
- [VecAccel](VecAccel.md) — 矢量加速度
- [VecDecel](VecDecel.md) — 矢量减速度
- [VecSpeed](VecSpeed.md) — 目标合成速度
