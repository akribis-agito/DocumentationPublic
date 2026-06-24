---
keyword: MasterFilt
summary: 应用于经缩放主位置增量的一阶低通滤波器系数（直接齿轮运动）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 161
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
  - 1
  - 64
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# MasterFilt

应用于经缩放主位置增量的一阶低通滤波器系数（直接齿轮运动）。

## 概述

`MasterFilt` 是在**直接**齿轮运动（[MotionMode](../02-motion-configuration/MotionMode.md) `= 5`）中对齿轮参考量应用的一阶低通滤波器系数。它平滑从动轴跟踪主轴的过程，抑制由粗糙或脉冲型主信号与高齿轮比组合所引起的跳变。间接齿轮运动（`= 6`）不使用该参数——该模式下由 PTP 规划器进行运动平滑。

## 工作原理

### 滤波器

在直接齿轮运动中，自 `Begin` 起的齿轮位移 $u_{k} = \text{MasterPos} - \text{MasterPosInitial}$，经一阶低通滤波后加至 `Begin` 时锁存的参考值，从而形成 `PosRef`。滤波器系数为 `MasterFilt / 64`：

$$
y_{k} = \frac{\text{MasterFilt}}{64} \cdot u_{k} + \left( 1 - \frac{\text{MasterFilt}}{64} \right) \cdot y_{k - 1}
$$

其中 $t = k \cdot T_{s}$，$T_{s}$ 为控制采样时间（通常为 61 µs）。

### 参数选取

`MasterFilt` 范围为 `1 … 64`。两个极端值界定了行为：

- `MasterFilt = 64` ⇒ 系数为 1，即**无滤波**（从动轴无滞后地跟踪主轴）。
- 较小的 `MasterFilt` ⇒ 重度平滑，跟踪滞后更大。

通过后向欧拉估计，可根据目标截止频率 $f_{c}$（Hz）选取 `MasterFilt`。默认值 `MasterFilt = 3` 对应约 128 Hz 的截止频率：

$$
\text{MasterFilt} = 64 \cdot \left( \frac{2\pi \cdot f_{c} \cdot T_{s}}{1 + 2\pi \cdot f_{c} \cdot T_{s}} \right)
$$

例如，在典型的 61 µs 采样时间下，选取 `MasterFilt = 16`（系数 16/64 = 0.25）可得到约 `f_c = 0.25 / (2π × 61 µs) ≈ 650 Hz` 的一阶极点，这是一种适度平滑，仍能跟踪较快的主轴变化。将其减小至 `MasterFilt = 3` 可将截止频率降至约 128 Hz，对于相同的主轴阶跃，从动轴响应明显更慢，但对主信号上的高频噪声抑制更强。

## 示例

```text
AMasterFilt=3        ; 默认（约 128 Hz 截止频率）
AMasterFilt=64       ; 无滤波（1:1 无滞后跟踪）
AMasterFilt          ; 读取当前值
```

## 另请参阅

- [MasterPos](MasterPos.md) — 其变化量经该滤波器的齿轮位移
- [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) — 在此滤波器之前应用的齿轮比
- [GearMaster](GearMaster.md) — 选择主变量
- [MotionMode](../02-motion-configuration/MotionMode.md) — `MasterFilt` 在直接齿轮运动（`= 5`）中生效
- [MotionMode10](MotionMode10.md) — 独立的直接从动模式；**不**使用 `MasterFilt`
