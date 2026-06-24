---
keyword: OneOverTFreq
summary: Vel[4] 所用硬件轮询频率的降采样指数。
availability:
  standalone:
  - v4
  central-i: []
can_code: 189
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
  - 7
  default: 4
  scaling: 1.0
  implemented: final
overrides: {}
removed_in:
- v5
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# OneOverTFreq

用于测量 Vel[4] 中 1/T 周期的定时器时钟的降采样指数。

## 概述

`OneOverTFreq` 设置应用于系统时钟的二的幂分频器的指数，由此产生 1/T 单元用于*计时*编码器事件之间间隔的定时器时钟。1/T 速度（[Vel](Vel.md)`[4]`）为 `counts / time`，因此定时器时钟频率决定了测量的**时间分辨率**以及定时器溢出前的最大（最慢）周期。

它仅在独立产品上、且仅在使用数字增量式编码器（[EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`）时受支持。请将其与 [OneOverTOn](OneOverTOn.md)（使能）和 [OneOverTGap](OneOverTGap.md)（计数间隔）配合使用以整定测量。

有效范围为 `0`–`7`（该值被掩码为 3 位并写入捕获定时器预分频器）。最大值 `7` 是硬件支持的最大分频比。默认值为 `4`。

## 工作原理

系统时钟为 300 MHz。1/T 定时器时钟为：

$$
\text{Timer frequency}\,[\text{Hz}] = \frac{\text{system clock}}{2^{\text{OneOverTFreq}}} = \frac{300\,000\,000}{2^{\text{OneOverTFreq}}}
$$

较大的 `OneOverTFreq` 以较大的二的幂进行分频，从而降低定时器频率。较低的定时器频率会使时间分辨率变粗，但延长了 16 位捕获寄存器在溢出前可保持的最长周期——因此它使 1/T 单元能够测量**更慢**的速度而不溢出（默认值 300/16 = 18.75 MHz 允许在不溢出的情况下进行低速监测）。

`OneOverTFreq` 与 [OneOverTGap](OneOverTGap.md) 组合为预计算因子 `2^OneOverTGap / 2^OneOverTFreq`，在写入任一关键字时计算一次。随后在每个控制周期，速度为：

$$
\text{Vel}[4] = \frac{\text{system clock}}{\text{latched timer period}} \cdot \frac{2^{\text{OneOverTGap}}}{2^{\text{OneOverTFreq}}}
$$

其中锁存的定时器周期（以定时器节拍计）对应于最近的间隔。符号取自 `Vel[2]`，因为 1/T 单元本身不感知方向。如果捕获发生溢出或出现方向变化，`Vel[4]` 被强制为 `0`。

| `OneOverTFreq` | 分频比 `2^n` | 定时器频率 | 节拍周期 |
|----------------|---------------|-----------------|-------------|
| 0 | 1 | 300 MHz | 3.33 ns |
| 1 | 2 | 150 MHz | 6.67 ns |
| 2 | 4 | 75 MHz | 13.3 ns |
| 3 | 8 | 37.5 MHz | 26.7 ns |
| 4 (默认) | 16 | 18.75 MHz | 53.3 ns |
| 5 | 32 | 9.375 MHz | 107 ns |
| 6 | 64 | 4.6875 MHz | 213 ns |
| 7 | 128 | 2.34375 MHz | 427 ns |

较高的定时器频率（较低的 `OneOverTFreq`）在较高速度下提供更精细的速度分辨率；较低的频率（较高的 `OneOverTFreq`）可在较低速度下避免定时器溢出。默认值 `4` 是一种倾向于低速监测的折中。

## 示例

```text
AOneOverTFreq=4      ; default: 18.75 MHz timer on axis A
AOneOverTFreq=0      ; full 300 MHz timer (finest resolution, overflows sooner)
AOneOverTFreq        ; read current value
```

## 另请参阅

- [Vel](Vel.md) — 反馈速度数组（`Vel[4]` 为 1/T 方法）
- [OneOverTOn](OneOverTOn.md) — 使能/禁用 1/T 速度计算
- [OneOverTGap](OneOverTGap.md) — 每个 1/T 采样测量的编码器计数间隔
- [OneOverTAuto](OneOverTAuto.md) — 预留的频率/间隔自整定（未实现）
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — 必须为数字增量式编码器
