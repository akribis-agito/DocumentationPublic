---
keyword: DualEncRange
availability:
  standalone: []
  central-i:
  - v5
can_code: 726
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
summary: 使用真双环控制的电机反馈位置范围。
---
# DualEncRange

使用真双环控制的电机反馈位置范围。

## 概述

`DualEncRange` 定义范围限定双环控制所用的电机反馈（[AuxPos](../../../02-keywords/10-motion/01-kinematics-status/AuxPos.md)）上下边界。当电机反馈处于该范围内时使用真双环控制，超出范围时使用伪双环控制。仅当 [DualLoopOn](DualLoopOn.md) = 1、[DualEncSwapOn](DualEncSwapOn.md) = 1 且 [DualEncMode](DualEncMode.md) = 1 时，本参数才有效。

| 索引 | 描述 |
|---|---|
| `DualEncRange[1]` | 位置范围的下边界 |
| `DualEncRange[2]` | 位置范围的上边界 |

边界单位为电机（辅助）编码器计数。仅使用 `DualEncRange[1]`（下边界）和 `DualEncRange[2]`（上边界）。

## 工作原理

在范围限定模式有效的情况下，控制器每个控制周期将电机反馈与两个边界进行比较：

$$
\text{DualEncRange}[1] \le \text{AuxPos} \le \text{DualEncRange}[2]
$$

当条件成立时，真双环控制有效，[DualLoopStat](DualLoopStat.md) 读数为 `2`；当条件不成立时，伪双环控制有效，[DualLoopStat](DualLoopStat.md) 读数为 `1`。切换时保持位置偏置，以避免切换产生位置阶跃。

## 示例

```text
ADualEncRange[1]=-500000   ; lower bound (motor-encoder counts)
ADualEncRange[2]=500000    ; upper bound (motor-encoder counts)
ADualEncMode=1             ; enable range-limited dual-loop
```

## 参见

- [DualEncMode](DualEncMode.md) — 使能范围限定双环（须为 1）
- [DualEncSwapOn](DualEncSwapOn.md) — 伪双环切换开关（须为 1）
- [DualLoopOn](DualLoopOn.md) — 使能双环控制（须为 1）
- [DualLoopStat](DualLoopStat.md) — 报告当前位置下激活的控制结构
- [AuxPos](../../../02-keywords/10-motion/01-kinematics-status/AuxPos.md) — 与范围进行比较的电机反馈
