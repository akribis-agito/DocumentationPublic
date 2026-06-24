---
keyword: PIVNoiseStat
summary: 只读状态数组，提供 PIV 噪声检测器的实时噪声统计量和当前阈值。
availability:
  standalone: []
  central-i:
  - v5
can_code: 799
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# PIVNoiseStat

只读状态数组，提供 PIV 噪声检测器的实时噪声统计量和当前阈值。

## 概述

`PIVNoiseStat` 是一个只读数组，报告 PIV 噪声检测器（[PIVNoiseDtct](PIVNoiseDtct.md)）正在计算的内容。它允许在整定过程中实时监测测量到的静止噪声统计量与当前触发阈值的对比，以便为 [PIVNoiseSTD](PIVNoiseSTD.md) 选取合理值并判断余量。

检测器启用且电机使能时，数值持续更新。在轴持续处于指令静止状态——位置参考保持不变且无信号注入激活——约一个半窗口长度（参见 [PIVNoiseWSize](PIVNoiseWSize.md)）之前，报告的统计量读取为零，这是控制器在运动期间及运动后短暂时间内抑制测量的方式。

此关键字仅在 v5（central-i）中可用。

## 工作原理

该数组采用 1 索引。可用元素为：

| 索引 | 元素 |
|---|---|
| 1 | 在窗口内测量到的静止状态下电流参考的方差。在轴处于指令静止状态约一个半窗口长度之前读取为零。 |
| 2 | 与索引 1 处测量值进行比较的当前方差阈值。 |

当测量方差（索引 1）超过阈值（索引 2）时触发故障。索引 2 处的阈值由 [PIVNoiseSTD](PIVNoiseSTD.md) 相对于峰值电流限值缩放得出。触发时控制器关闭电机并在 [ConFlt](../../07-status-and-faults/ConFlt.md) 中记录故障码 1072。

## 示例

```text
APIVNoiseStat[1]      ; live standstill noise statistic
APIVNoiseStat[2]      ; active threshold (trip level for index 1)
```

## 另请参阅

- [PIVNoiseDtct](PIVNoiseDtct.md) — 启用 PIV 噪声检测器
- [PIVNoiseSTD](PIVNoiseSTD.md) — 方差阈值（在索引 2 处反映）
- [PIVNoiseWSize](PIVNoiseWSize.md) — 统计窗口大小
- [ConFlt](../../07-status-and-faults/ConFlt.md) — 控制器故障码（检测到时为 1072）
