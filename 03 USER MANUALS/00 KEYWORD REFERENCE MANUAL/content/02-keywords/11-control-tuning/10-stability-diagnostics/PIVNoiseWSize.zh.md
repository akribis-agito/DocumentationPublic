---
keyword: PIVNoiseWSize
summary: 计算 PIV 噪声统计量所用滑动窗口的长度，单位为毫秒。
availability:
  standalone: []
  central-i:
  - v5
can_code: 800
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 5.0
  - 125.0
  default: 30.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PIVNoiseWSize

计算 PIV 噪声统计量所用滑动窗口的长度，单位为毫秒。

## 概述

`PIVNoiseWSize` 设置 PIV 噪声检测器（[PIVNoiseDtct](PIVNoiseDtct.md)）在测量静止状态下电流参考方差时所使用的近期样本窗口长度，单位为毫秒。较长的窗口可平滑统计量并抑制短暂瞬变，但对持续噪声问题的响应较慢；较短的窗口响应更快，但统计量本身的噪声也更大。

窗口长度以毫秒为单位，内部被钳位至控制器支持的范围；可接受约 5 ms 至 125 ms 的值，30 ms 为典型设置。检测器还要求轴在指令静止状态下保持略长于一个窗口长度的时间后才对统计量采取动作，因此较长的窗口会延长轴在噪声被上报前所需观察的稳定时间。

此关键字仅在 v5（central-i）中可用。

## 工作原理

控制器将毫秒值按控制环速率转换为采样计数，并将其用作方差计算的滑动窗口长度。所得计数被钳位至控制器支持的窗口大小，因此过小或过大的毫秒值被限制在可用范围内而不是被拒绝。

由于更改窗口大小会调整内部缓冲区，此关键字不能在轴运动中或电机使能时修改。请在启用检测器之前进行设置。该值保存至闪存。

## 示例

```text
APIVNoiseWSize=30     ; 30 ms window (typical)
APIVNoiseWSize=125    ; longest window: smoothest statistic, slowest to react
APIVNoiseWSize[1]     ; read back the configured window length in ms
```

## 另请参阅

- [PIVNoiseDtct](PIVNoiseDtct.md) — 启用 PIV 噪声检测器
- [PIVNoiseSTD](PIVNoiseSTD.md) — PIV 噪声方差阈值
- [PIVNoiseStat](PIVNoiseStat.md) — PIV 噪声检测器状态数组
