---
keyword: ddPosRef
summary: 加速度参考，即位置参考 PosRef 的二阶微分。
availability:
  standalone: []
  central-i:
  - v5
can_code: 857
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-08-02'
doc_revision: '2026.07'
language: zh-CN
---
# ddPosRef

加速度参考，即位置参考 PosRef 的二阶微分。

## 概述

`ddPosRef` 是轴的加速度参考。它是控制器通过加速度前馈增益 `AccFFW` 前馈的信号，也是参考微分链 [PosRef](PosRef.md) → [dPosRef](dPosRef.md) → `ddPosRef` → [dddPosRef](dddPosRef.md) 中的第二项。

`ddPosRef` 是一个*参考*，由指令轨迹推导而来。它不是对轴的测量：不存在加速度反馈信号，`ddPosRef` 不受电机实际运动的影响。

## 工作原理

每个控制周期，控制器以两种方式之一产生 `ddPosRef`，并自动选择。当前使用的方式由只读关键字 `FFWMode` 报告：

- **轨迹模式**（`FFWMode` = 1）——加速度**直接取自轮廓发生器自身的方程**，与速度参考和加加速度参考一并取得。由于这四个量来自对轨迹的同一次求值，它们与位置参考按周期对齐，且不带采样延迟。
- **微分模式**（`FFWMode` = 0）——加速度按经完整后处理的位置参考（即位置环本身所用的经整形和滤波的信号）的**二阶差分**计算：

$$
\text{ddPosRef} = \left( P_k - 2P_{k-1} + P_{k-2} \right) \times 2^{n}
$$

其中 $P$ 为经整形+滤波的位置参考，$n$ 为采样率指数（`SAMPLE_FREQUENCY_TWO_POWER`，在标准 16 kHz 控制周期下为 14，32 kHz 下为 15，64 kHz 下为 16）。

### 模式的选择

仅当轨迹足够平滑、可以解析求导时才使用轨迹模式，控制器将其理解为**同时**满足以下各项：

- 轮廓发生器正在运行平滑轮廓，
- 输入整形关闭（`ShapingOn` = 0），
- 轮廓发生器加加速度限制未设置（`Jerk` = 0），且
- 位置参考滤波器关闭（`PosFiltOn` = 0）。

若其中任一项不满足，则参考信号经过了轮廓方程未描述的后处理，控制器回退到微分模式。因此，在运行中的轴上启用输入整形或位置滤波器会改变 `ddPosRef` 的产生方式，这可从 `FFWMode` 的变化观察到。

## 如何使用

`ddPosRef` 乘以加速度前馈增益，构成加入电流指令的加速度前馈项：

$$
\text{FFW}_{\text{acc}} = \text{ddPosRef} \times \text{AccFFW} \times k
$$

其中 $k$ 为固定的内部增益缩放。当 `VelFFW` 与 `AccFFW` 均为零且加加速度前馈被禁用时，控制器会完全跳过前馈乘法运算，作为一项 ISR 时间预算优化；`ddPosRef` 本身仍会产生，仍可读取。

### 边界情况

- **电机失能：** 微分模式所用的上一周期加速度存储被复位为 `0`，因此使能后的第一个周期从干净的差分开始，而不会跨越失能区间做差分。
- **轮廓发生器停止：** 轨迹模式的加速度来源在轮廓发生器完成或被停止时清零，因此已完成的运动不会遗留过期的加速度参考。
- **运动中切换模式：** `FFWMode` 每周期求值。轨迹模式与微分模式之间的切换会在同一周期改变 `ddPosRef` 的来源。
- **超出范围写入：** `ddPosRef` 为只读。

## 示例

```text
AddPosRef           ; read the current acceleration reference
AFFWMode            ; is it coming from the profiler (1) or a derivative (0)?
```

## 另请参阅

- [PosRef](PosRef.md) — 位置参考，微分链的来源
- [dPosRef](dPosRef.md) — 速度参考，一阶微分
- [dddPosRef](dddPosRef.md) — 加加速度参考，三阶微分
- [AccFFW](../../11-control-tuning/05-feedforwards/AccFFW.md) — 施加于 `ddPosRef` 的增益
