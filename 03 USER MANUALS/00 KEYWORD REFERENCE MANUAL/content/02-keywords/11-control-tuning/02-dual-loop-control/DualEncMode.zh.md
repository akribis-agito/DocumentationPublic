---
keyword: DualEncMode
availability:
  standalone: []
  central-i:
  - v5
can_code: 725
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
summary: 启用范围限定双环控制。
---
# DualEncMode

启用范围限定双环控制。

## 概述

`DualEncMode` 选择伪双环是否在全范围内使用，还是仅在定义的位置范围之外使用。仅当 [DualLoopOn](DualLoopOn.md) = 1 且 [DualEncSwapOn](DualEncSwapOn.md) = 1 时，本参数才有效。

| `DualEncMode` | 行为 |
|---|---|
| 0 | 始终使用伪双环控制，与位置无关。 |
| 1 | 当电机反馈处于 [DualEncRange](DualEncRange.md) 定义的范围内时使用真双环控制；超出该范围时使用伪双环控制。 |

## 工作原理

当 `DualEncMode = 1` 时，控制器每个控制周期将电机（辅助）反馈 [AuxPos](../../../02-keywords/10-motion/01-kinematics-status/AuxPos.md) 与 [DualEncRange](DualEncRange.md) 中的上下边界进行比较：

- **在范围内** — 真双环有效：位置环以负载反馈闭合。[DualLoopStat](DualLoopStat.md) 读数为 `2`。
- **在范围外** — 伪双环有效：位置环从辅助编码器取值并缩放至负载单位（参见 [DualEncSwapOn](DualEncSwapOn.md)）。[DualLoopStat](DualLoopStat.md) 读数为 `1`。

切换时保持位置偏置，以避免切换产生位置阶跃。

`DualEncMode` 不在重新上电后保留：上电时恢复默认值 `0`（伪双环全范围生效），因此每次上电后须重新激活范围限定切换。可在电机使能时修改，但不能在运动中修改。相比之下，[DualEncRange](DualEncRange.md) 可保留，且在运动中也可调整。

![True dual-loop runs while AuxPos lies between DualEncRange[1] and DualEncRange[2]; pseudo dual-loop runs outside that window](dual-enc-range-switch.svg)

## 示例

```text
ADualEncMode=1       ; use true dual-loop only within DualEncRange
ADualEncRange[1]=-100000
ADualEncRange[2]=100000
```

## 参见

- [DualEncRange](DualEncRange.md) — 限定真双环范围的电机反馈边界
- [DualEncSwapOn](DualEncSwapOn.md) — 伪双环切换开关（须为 1）
- [DualLoopOn](DualLoopOn.md) — 使能双环控制（须为 1）
- [DualLoopStat](DualLoopStat.md) — 报告当前位置下激活的控制结构
