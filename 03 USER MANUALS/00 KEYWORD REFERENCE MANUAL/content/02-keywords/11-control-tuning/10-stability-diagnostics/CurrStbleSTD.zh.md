---
keyword: CurrStbleSTD
summary: 稳定性检测用电流环方差阈值，以峰值电流限值的百分比表示。
availability:
  standalone: []
  central-i:
  - v5
can_code: 791
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
# CurrStbleSTD

稳定性检测用电流环方差阈值，以峰值电流限值的百分比表示。

## 概述

`CurrStbleSTD` 设置电流环稳定性检测器（[CurrStbleDtct](CurrStbleDtct.md)）使用的方差（标准差）阈值。它定义了测量电机电流允许的最大波动下限，超出该下限才可被视为振荡。

该值以轴峰值电流限值（[PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md)）的百分比表示。默认值为 2（即峰值电流标准差的 2%）。值越大，检测器对电流波动的容忍度越高；值越小，灵敏度越高。

本关键字仅从 v5（central-i）起可用。

## 工作原理

检测器在滑动窗口内跟踪测量电机电流的方差。当电流波动超过以下两个限值中的较大值时，则认为电流波动过大：

- 指令电流参考方差的固定倍数（确保轴在接受大幅指令时不被误标记），以及
- `CurrStbleSTD` 设定的绝对下限（确保在指令平稳而电机电流剧烈波动时能被标记）。

当电机电流方差超过上述组合限值，*且* 同时跟踪误差超过其阈值（[CurrStbleErr](CurrStbleErr.md)）时，检测器关断电机并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中记录故障码 1071。

百分比内部以峰值电流限值为基准进行缩放，并以平方形式参与比较（因为方差比较基于方差域），因此比较下限会随 [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) 自动调整。该值保存至闪存，可在轴运动中及电机使能时修改。写入新值后，方差阈值在下一个控制周期立即生效，无需重新使能检测器。

[CurrStbleStat](CurrStbleStat.md) 的元素 4 报告组合/有效触发限值——即 `CurrStbleSTD` 导出的下限与指令参考方差固定倍数中的较大值——而非 `CurrStbleSTD` 下限本身。

## 示例

```text
ACurrStbleSTD=2       ; spread threshold = 2% of peak current limit (default)
ACurrStbleSTD=10      ; tolerate more current swing before flagging
ACurrStbleSTD[1]      ; read back the configured percentage
```

## 另请参阅

- [CurrStbleDtct](CurrStbleDtct.md) — 使能电流环稳定性检测器
- [CurrStbleErr](CurrStbleErr.md) — 电流环跟踪误差阈值（另一个触发条件）
- [CurrStbleStat](CurrStbleStat.md) — 电流环稳定性检测器状态数组
- [PeakCL](../../06-protections/02-current-and-voltage/PeakCL.md) — 阈值基准的峰值电流限值
