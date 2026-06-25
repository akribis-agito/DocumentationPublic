---
keyword: CurrStbleStat
summary: 只读状态数组，提供电流环稳定性检测器的实时统计量和阈值。
availability:
  standalone: []
  central-i:
  - v5
can_code: 792
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 7
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# CurrStbleStat

只读状态数组，提供电流环稳定性检测器的实时统计量和阈值。

## 概述

`CurrStbleStat` 是一个只读数组，报告电流环稳定性检测器（[CurrStbleDtct](CurrStbleDtct.md)）在每个控制周期的计算结果。在整定电流环时，可同步查看运行统计量和当前生效的触发阈值，从而为 [CurrStbleSTD](CurrStbleSTD.md) 和 [CurrStbleErr](CurrStbleErr.md) 选取合理的值，并了解触发跳闸前的余量。

检测器使能且电机使能时，数组持续更新。检测器禁用时，数组不刷新，保持最后一次的内容。

本关键字仅从 v5（central-i）起可用。

## 工作原理

数组以 1 为起始索引。可用元素如下：

| 索引 | 元素 |
|---|---|
| 1 | 窗口内指令电流参考的方差。 |
| 2 | 窗口内测量电机电流的方差。 |
| 3 | 窗口内电流跟踪误差的平均幅值。 |
| 4 | 电机电流方差（索引 2）所对比的当前生效方差阈值。 |
| 5 | 误差（索引 3）所对比的当前生效跟踪误差阈值。 |
| 6 | 保留。 |

当电机电流方差（索引 2）超过方差阈值（索引 4），且同时跟踪误差（索引 3）超过误差阈值（索引 5）时，触发故障。索引 4 和 5 处的阈值由 [CurrStbleSTD](CurrStbleSTD.md) 和 [CurrStbleErr](CurrStbleErr.md) 与峰值电流限值缩放后得出。触发跳闸时，控制器关断电机并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中记录故障码 1071。

## 示例

```text
ACurrStbleStat[2]     ; live spread of the measured motor current
ACurrStbleStat[4]     ; active spread threshold (trip level for index 2)
ACurrStbleStat[3]     ; live average tracking error
ACurrStbleStat[5]     ; active tracking-error threshold (trip level for index 3)
```

## 另请参阅

- [CurrStbleDtct](CurrStbleDtct.md) — 使能电流环稳定性检测器
- [CurrStbleSTD](CurrStbleSTD.md) — 方差阈值（反映于索引 4）
- [CurrStbleErr](CurrStbleErr.md) — 跟踪误差阈值（反映于索引 5）
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 控制器故障码（检测到时为 1071）
