---
keyword: CurrStbleDtct
summary: 使能对轴上不稳定（振荡）电流环的运行时检测。
availability:
  standalone: []
  central-i:
  - v5
can_code: 789
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrStbleDtct

使能对轴上不稳定（振荡）电流环的运行时检测。

## 概述

`CurrStbleDtct` 开启或关闭电流环稳定性检测器。使能后，控制器持续监测电流环，若判定环路出现振荡，则关断电机并记录控制器故障，防止不稳定的环路持续驱动电机。在电流环整定期间以及生产环境中，对于整定较差或处于边界状态的环路，该功能可作为安全保护手段。

| 值 | 含义 |
|---|---|
| 0 | 检测器禁用（默认）。 |
| 1 | 检测器使能。 |

本关键字仅从 v5（central-i）起可用。

## 工作原理

电机使能且检测器处于使能状态时，控制器在最近样本的滑动窗口内维护运行统计量，并在每个控制周期检测以下两个条件：

- 测量到的电机电流的方差明显大于指令电流参考的方差，且
- 电流跟踪误差的平均幅值超过其阈值。

两个条件同时满足时，判定环路出现振荡：控制器关断电机并记录故障，该故障以故障码 1071（检测到电流环不稳定）出现在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中。

两个阈值以轴峰值电流限值（[PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)）的百分比进行配置：[CurrStbleSTD](CurrStbleSTD.md) 设置方差阈值，[CurrStbleErr](CurrStbleErr.md) 设置跟踪误差阈值。实时统计量和当前生效的阈值可通过 [CurrStbleStat](CurrStbleStat.md) 读回。

使能检测器在电机使能时生效；此时统计窗口清零，确保检测从干净状态开始。将该关键字重新写为 0 将立即禁用检测。由于检测器可随时开启或关闭，本关键字可在轴运动中及电机使能时写入。

## 示例

```text
ACurrStbleSTD=2       ; spread threshold 2% of peak current limit
ACurrStbleErr=2       ; tracking-error threshold 2% of peak current limit
ACurrStbleDtct=1      ; enable the current-loop stability detector
ACurrStbleDtct[1]     ; read back the enable state
```

## 另请参阅

- [CurrStbleErr](CurrStbleErr.md) — 电流环跟踪误差阈值
- [CurrStbleSTD](CurrStbleSTD.md) — 电流环方差阈值
- [CurrStbleStat](CurrStbleStat.md) — 电流环稳定性检测器状态数组
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 控制器故障码（检测到时为 1071）
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — 阈值基准的峰值电流限值
