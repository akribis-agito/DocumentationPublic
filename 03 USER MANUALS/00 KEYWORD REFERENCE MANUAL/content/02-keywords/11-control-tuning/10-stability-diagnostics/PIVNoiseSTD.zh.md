---
keyword: PIVNoiseSTD
summary: 静止噪声/抖动检测的 PIV 噪声方差阈值，以峰值电流限值的百分比表示。
availability:
  standalone: []
  central-i:
  - v5
can_code: 798
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0.01
  - 100.0
  default: 2.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PIVNoiseSTD

静止噪声/抖动检测的 PIV 噪声方差阈值，以峰值电流限值的百分比表示。

## 概述

`PIVNoiseSTD` 设置 PIV 噪声检测器（[PIVNoiseDtct](PIVNoiseDtct.md)）使用的方差阈值。它定义了在轴保持静止期间，电流参考允许摆动的幅度，超过该幅度则视为过度噪声或抖动。

该值以轴峰值电流限值（[PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)）的百分比表示。较大的值使检测器对静止噪声更宽容；较小的值使其在更低噪声水平时即触发。默认值为 2（即峰值电流限值的 2%），可接受范围为 0.01 至 100 百分比。

此关键字仅在 v5（central-i）中可用。

## 工作原理

在检测器启用且轴已在指令静止状态下保持足够长时间以填满其窗口（参见 [PIVNoiseWSize](PIVNoiseWSize.md)）后，控制器将电流参考的方差与此阈值进行比较。该百分比在内部相对于峰值电流限值进行缩放并平方（比较基于方差），因此有效级别自动跟随 [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)。

当测量方差超过阈值时，控制器关闭电机并记录故障码 1072，可在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中查看。

该值保存至闪存，可在轴运动中及电机使能时修改。写入后阈值立即重新计算——包括检测器已在运行且电机使能时——并在下一个控制周期生效，无需重新启用。当前阈值可从 [PIVNoiseStat](PIVNoiseStat.md) 的第 2 元素读回。

## 示例

```text
APIVNoiseSTD=2        ; threshold = 2% of peak current limit
APIVNoiseSTD=5        ; tolerate more standstill noise before flagging
APIVNoiseSTD[1]       ; read back the configured percentage
```

## 另请参阅

- [PIVNoiseDtct](PIVNoiseDtct.md) — 启用 PIV 噪声检测器
- [PIVNoiseWSize](PIVNoiseWSize.md) — 统计窗口大小
- [PIVNoiseStat](PIVNoiseStat.md) — PIV 噪声检测器状态数组
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — 阈值所基准的峰值电流限值
