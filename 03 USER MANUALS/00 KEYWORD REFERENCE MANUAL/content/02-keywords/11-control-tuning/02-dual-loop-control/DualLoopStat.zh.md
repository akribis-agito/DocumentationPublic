---
keyword: DualLoopStat
availability:
  standalone: []
  central-i:
  - v5
can_code: 727
attributes:
  access: ro
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 当前激活的双环控制结构的只读状态。
---
# DualLoopStat

当前激活的双环控制结构的只读状态。

## 概述

`DualLoopStat` 报告当前激活的控制结构。它反映 [DualLoopOn](DualLoopOn.md)、[DualEncSwapOn](DualEncSwapOn.md)、[DualEncMode](DualEncMode.md) 和 [DualEncRange](DualEncRange.md) 的运行时结果——包括范围限制切换（该切换可在运动中改变激活结构）——因此可能与已配置的 `DualLoopOn` 值不同。

| `DualLoopStat` | 说明 |
|---|---|
| 0 | 默认控制激活（两个环均使用主编码器）。 |
| 1 | 伪双环控制激活（位置环来源于辅助编码器，换算至负载单位）。 |
| 2 | 双环控制激活（位置环使用主/负载编码器，速度环使用电机反馈）。 |

## 工作原理

双环禁用时，`DualLoopStat` 读回 `0`。当 [DualLoopOn](DualLoopOn.md) = 1（辅助编码器速度反馈）且伪双环关闭时，读回 `2`。伪双环开启（[DualEncSwapOn](DualEncSwapOn.md) = 1）时，读回 `1`。当 [DualLoopOn](DualLoopOn.md) = 2（模拟测速机速度反馈）时，读回 `0`。

当配置了范围限制切换（[DualEncMode](DualEncMode.md) = 1）时，控制器根据电机反馈是否在 [DualEncRange](DualEncRange.md) 窗口内，在伪双环与全双环之间切换：在范围内时 `DualLoopStat` 变为 `2`，超出范围时变为 `1`。因此读取 `DualLoopStat` 可反映当前时刻生效的控制结构。

## 示例

```text
ADualLoopStat        ; read the active dual-loop control structure
```

## 另请参阅

- [DualLoopOn](DualLoopOn.md) — 配置双环控制
- [DualEncSwapOn](DualEncSwapOn.md) — 伪双环开关
- [DualEncMode](DualEncMode.md) / [DualEncRange](DualEncRange.md) — 本状态所反映的范围限制切换
