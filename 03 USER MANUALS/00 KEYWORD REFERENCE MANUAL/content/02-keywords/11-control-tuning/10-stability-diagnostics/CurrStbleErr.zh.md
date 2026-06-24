---
keyword: CurrStbleErr
summary: 稳定性检测用电流环跟踪误差阈值，以峰值电流限值的百分比表示。
availability:
  standalone: []
  central-i:
  - v5
can_code: 790
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
  - 1
  - 100
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrStbleErr

稳定性检测用电流环跟踪误差阈值，以峰值电流限值的百分比表示。

## 概述

`CurrStbleErr` 设置电流环稳定性检测器（[CurrStbleDtct](CurrStbleDtct.md)）使用的两个阈值之一。该值为跟踪误差阈值：在电流方差异常的同时，被视为电流环不稳定证据的最小平均电流跟踪误差。

该值以轴峰值电流限值（[PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)）的百分比表示。值越大，检测器越不灵敏（环路需更大的跟踪偏差才触发跳闸）；值越小，更小的误差即可触发跳闸。默认值为 2（即峰值电流限值的 2%）。

本关键字仅从 v5（central-i）起可用。

## 工作原理

检测器在滑动窗口内计算指令电流参考与测量电机电流之差的平均幅值。仅当该平均误差超过 `CurrStbleErr` 阈值，*且* 同时满足电流方差测试（参见 [CurrStbleSTD](CurrStbleSTD.md)）时，才会触发故障。要求两个条件同时满足，可避免因静态偏置导致误触发（环路仍在稳定跟踪），也可避免因参考值噪声大但环路跟踪正常而误触发。

在内部，百分比通过与峰值电流限值相乘转换为电流阈值，因此更改 [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) 会自动重新缩放有效误差阈值。该值保存至闪存，可在轴运动中及电机使能时修改。写入新值后，有效跟踪误差阈值在下一个控制周期立即生效，无需重新使能检测器。

当前生效的阈值可从 [CurrStbleStat](CurrStbleStat.md) 的元素 5 读回。

## 示例

```text
ACurrStbleErr=2       ; tracking-error threshold = 2% of peak current limit (default)
ACurrStbleErr=5       ; less sensitive: require a larger tracking error
ACurrStbleErr[1]      ; read back the configured percentage
```

## 另请参阅

- [CurrStbleDtct](CurrStbleDtct.md) — 使能电流环稳定性检测器
- [CurrStbleSTD](CurrStbleSTD.md) — 电流环方差阈值（另一个触发条件）
- [CurrStbleStat](CurrStbleStat.md) — 电流环稳定性检测器状态数组
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — 阈值基准的峰值电流限值
