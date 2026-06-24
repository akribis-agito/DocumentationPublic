---
keyword: StopRep
summary: 停止重复（repeat）运动并清除重复运动状态。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 148
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# StopRep

在当前重复执行完成后结束重复点到点运动，而非等到 RptCycles 耗尽。

## 概述

`StopRep` 结束重复点到点（PTP）运动（[MotionMode](../02-motion-configuration/MotionMode.md) `= 2`，PTP 重复模式）。它不会在运动中途停止轴：它请求**不重新启动**当前重复周期，使当前重复正常完成后运动结束——而非继续运行直至 [RptCycles](../02-motion-configuration/RptCycles.md) 耗尽。剩余运动（正在进行的重复或重复间的停留）仍使用正常的 [Decel](../03-kinematics-configuration/Decel.md) 曲线。该命令为轴相关命令函数，可在运动过程中发出。

## 工作原理

### 请求停止

`StopRep`（在中断禁用状态下）设置重复停止请求位并记录原因：

| `StopRep` 设置的字段 | 值 | 含义 |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) 第 2 位（重复停止） | 1 | 请求结束重复运动 |
| [MotionReason](../05-motion-status/MotionReason.md) | 3 | 记录运动因 `StopRep` 而结束 |

### 规划器如何结束重复

重复运动在运动阶段与停留阶段（等待位，持续 [RptWait](../02-motion-configuration/RptWait.md) 个周期）之间交替，并在 [RptCounter](../05-motion-status/RptCounter.md) 中计数已完成的重复次数。在每次重复的平滑尾端，规划器决定是否启动下一次重复。该决定要求重复停止位**清零**：只有在重复停止位清零且 [RptCycles](../02-motion-configuration/RptCycles.md) 为 0（无限）或尚未达到时，才会启动新的重复；否则运动结束并清除所有运动位。

因此，一旦 `StopRep` 置位，下一次重复完成时规划器将结束运动而非启动停留。若在轴已处于重复间停留期间置位，停留**仍将运行至完成**，然后正常运行下一段，运动在该段平滑尾端结束——`StopRep` 仅在平滑后的决策点检查。无论哪种情况，[MotionReason](../05-motion-status/MotionReason.md) 均保持值 `3`。重复的方向/返回行为由 [RptMode](../02-motion-configuration/RptMode.md) 配置。

如需在停留或段中途立即结束，请使用 [Stop](Stop.md)（受控减速）或 [Abort](Abort.md)（立即停止）。

### 边界情况

- **电机关闭：** 接受但无效果（无运动）。
- **未处于运动中：** 重复停止位（第 2 位）无条件置位，即使轴处于空闲状态。但当轴未运动时，规划器每个控制周期都将整个运动状态字重写为"未运动"，因此空闲时置位的第 2 位几乎立即被清除，**不会**延续至下一次运动。只有在活动的重复运动（`Begin` 本身不清除该位，但也不需要——空闲轴已经失去了该过期位）期间置位才有效果。
- **超出范围的"写"操作：** 该函数无值。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 无关——`StopRep` 不修改参考值。
- **活动故障：** 轴被禁用，运动结束；整个运动状态字被强制为"未运动"，同时清除重复停止位，重新使能后不保留任何状态。
- **其他运动模式：** `StopRep` 仅在 [MotionMode](../02-motion-configuration/MotionMode.md) `= 2` 时有意义；在其他模式下该位被置位但不使用。
- **`RptCycles = 0`（无限）：** `StopRep` 是不使用 `Stop`/`Abort` 的情况下结束无限循环的主要方式。
- **已处于最后一次重复：** `StopRep` 无害（运动本来也会结束）。

## 示例

```text
AStopRep             ; finish the current repetition, then stop (do not start another)
```

## 另请参阅

- [Stop](Stop.md) — 通用受控停止（立即减速至静止）
- [RptMode](../02-motion-configuration/RptMode.md) — 重复方向（往返模式与单向模式）
- [RptCycles](../02-motion-configuration/RptCycles.md) — `StopRep` 提前终止的编程重复次数
- [RptWait](../02-motion-configuration/RptWait.md) — 重复间的停留时间
- [RptCounter](../05-motion-status/RptCounter.md) — 已完成重复次数计数
- [MotionStat](../05-motion-status/MotionStat.md) — `StopRep` 设置的第 2 位（重复停止）
- [MotionReason](../05-motion-status/MotionReason.md) — `StopRep` 设置的原因码 3
