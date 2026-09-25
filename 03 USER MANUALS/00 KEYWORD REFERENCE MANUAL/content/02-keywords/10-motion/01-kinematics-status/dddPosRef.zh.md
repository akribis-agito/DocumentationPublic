---
keyword: dddPosRef
summary: 加加速度参考，即位置参考 PosRef 的三阶微分。
availability:
  standalone: []
  central-i:
  - v5
can_code: 858
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
# dddPosRef

加加速度参考，即位置参考 PosRef 的三阶微分。

## 概述

`dddPosRef` 是轴的加加速度参考——加速度参考 [ddPosRef](ddPosRef.md) 的变化率。它是参考微分链 [PosRef](PosRef.md) → [dPosRef](dPosRef.md) → [ddPosRef](ddPosRef.md) → `dddPosRef` 中的最后一项，其存在是为了驱动可选的加加速度前馈项。

与速度参考和加速度参考不同，`dddPosRef` 仅在明确启用加加速度前馈时才被*施加*。无论如何它都会被计算并可读取。

## 工作原理

`dddPosRef` 由与 [ddPosRef](ddPosRef.md) 相同的双模式机制产生，当前模式由只读关键字 `FFWMode` 报告：

- **轨迹模式**（`FFWMode` = 1）——加加速度直接取自轮廓发生器的方程，与位置、速度和加速度参考按周期对齐，且不带采样延迟。
- **微分模式**（`FFWMode` = 0）——加加速度为**加速度参考的一阶差分**，因而是位置参考的三阶差分：

$$
\text{dddPosRef} = \left( \text{ddPosRef}_k - \text{ddPosRef}_{k-1} \right) \times 2^{n}
$$

其中 $n$ 为采样率指数（`SAMPLE_FREQUENCY_TWO_POWER`，在标准 16 kHz 控制周期下为 14，32 kHz 下为 15，64 kHz 下为 16）。

模式选择条件见 [ddPosRef](ddPosRef.md)——轨迹模式要求平滑轮廓，且输入整形、轮廓发生器加加速度限制和位置参考滤波器均关闭。

由于微分模式对位置参考求导三次，`dddPosRef` 是该链中噪声最大的信号：参考中的任何阶跃或量化都会被每一次逐次差分放大。这正是所施加的项既受门控又受饱和限制的原因。

## 如何使用

仅当 `JerkFFWOn` = 1 时才施加加加速度前馈项：

$$
\text{FFW}_{\text{jerk}} = \text{clamp}\left( \text{dddPosRef} \times \text{JerkFFW} \times k,\; \pm\,\text{JerkFFWLim} \right)
$$

其中 $k$ 为固定的内部增益缩放。`JerkFFWLim` 是对所得项的对称饱和限制——而不是对 `dddPosRef` 本身的限制，后者以未截断的形式报告。当 `JerkFFWOn` = 0 时不计算该项，其贡献为零，而 `dddPosRef` 仍持续更新，仍可读取或记录。

在禁用前馈的情况下记录 `dddPosRef`，是判断加加速度参考是否足够干净、值得施加，以及选择 `JerkFFWLim` 的常规方法。

### 边界情况

- **电机失能：** 微分模式所差分的上一周期加速度存储被复位为 `0`，因此使能后的第一个周期不会因跨越失能区间做差分而产生虚假的加加速度尖峰。
- **轮廓发生器停止：** 轨迹模式的加加速度来源在轮廓发生器完成或被停止时清零。
- **`JerkFFWOn` = 0：** `dddPosRef` 仍会产生；仅前馈项被抑制。
- **超出范围写入：** `dddPosRef` 为只读。

## 示例

```text
AdddPosRef          ; read the current jerk reference
AJerkFFWOn=1        ; enable the jerk feed-forward term
AJerkFFWLim=1000    ; saturate the applied term
```

## 另请参阅

- [ddPosRef](ddPosRef.md) — 加速度参考，本信号对其求导
- [dPosRef](dPosRef.md) — 速度参考，一阶微分
- [PosRef](PosRef.md) — 位置参考，微分链的来源
