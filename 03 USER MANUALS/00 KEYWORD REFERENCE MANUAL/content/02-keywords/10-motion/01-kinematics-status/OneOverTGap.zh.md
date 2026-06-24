---
keyword: OneOverTGap
summary: 触发 1/T 轮询保存的编码器计数器变化量（以二的幂表示）。
availability:
  standalone:
  - v4
  central-i: []
can_code: 190
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
  - 11
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
removed_in:
- v5
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# OneOverTGap

每个 1/T 速度采样所计时的编码器计数变化量（以二的幂表示）。

## 概述

`OneOverTGap` 定义 1/T 单元在锁存测得时间之前所累积的编码器计数数量，以二的幂表示：`gap = 2^OneOverTGap` 计数。1/T 速度（[Vel](Vel.md)`[4]`）为该固定位移除以编码器走过该位移所用的时间。较大的间隔在更多计数上取平均（读数更平稳、更新率更低）；较小的间隔更新更快，但对编码器边沿抖动更敏感。

它仅在独立产品上、且仅在使用数字增量式编码器（[EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) `= 1`）时受支持。请将其与 [OneOverTOn](OneOverTOn.md)（使能）和 [OneOverTFreq](OneOverTFreq.md)（定时器频率）配合使用。

有效范围为 `0`–`11`（该值被掩码为 4 位并写入单位位置事件预分频器）。最大值 `11` 是硬件支持的最大间隔。默认值为 `2`。

## 工作原理

$$
\text{Gap}\,[\text{counts}] = 2^{\text{OneOverTGap}}
$$

计时单元对编码器前进 `gap` 个计数的时间间隔进行计时，在达到间隔时锁存定时器周期；随后内部计数器复位，为下一个间隔做好准备。在每个控制周期，间隔与定时器频率组合为速度：

$$
\text{Vel}[4] = \frac{2^{\text{OneOverTGap}}}{2^{\text{OneOverTFreq}}} \cdot \frac{\text{system clock}}{\text{latched timer period}}
$$

第一个因子（`2^OneOverTGap / 2^OneOverTFreq`）在每次写入 `OneOverTGap` 或 [OneOverTFreq](OneOverTFreq.md) 时预计算一次，因此每个控制周期只需执行系统时钟除以周期的除法和一次乘法。

| `OneOverTGap` | 间隔 `2^n`（计数） |
|---------------|--------------------|
| 0 | 1 |
| 1 | 2 |
| 2 (默认) | 4 |
| 3 | 8 |
| 4 | 16 |
| … | … |
| 11 (最大) | 2048 |

> **注意：** 至少为 4 的间隔（`OneOverTGap` ≥ 2）可提供更准确的速度读数，因为它不受 A 与 B 编码器信号之间相移（其并不总是恰好 90 度）的影响。这就是默认值为 `2` 的原因。

## 示例

```text
AOneOverTGap=2       ; default: gap = 2^2 = 4 counts on axis A
AOneOverTGap=4       ; gap = 16 counts (steadier reading, slower update)
AOneOverTGap         ; read current value
```

## 另请参阅

- [Vel](Vel.md) — 反馈速度数组（`Vel[4]` 为 1/T 方法）
- [OneOverTOn](OneOverTOn.md) — 使能/禁用 1/T 速度计算
- [OneOverTFreq](OneOverTFreq.md) — 1/T 定时器频率分频器（分辨率与溢出的权衡）
- [OneOverTAuto](OneOverTAuto.md) — 预留的频率/间隔自整定（未实现）
- [EncType](../../03-encoder/01-general-settings/EncType-AuxEncType.md) — 必须为数字增量式编码器
