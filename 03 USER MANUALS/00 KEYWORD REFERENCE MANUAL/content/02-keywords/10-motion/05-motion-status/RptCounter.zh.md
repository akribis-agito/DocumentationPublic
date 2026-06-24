---
keyword: RptCounter
summary: 统计重复点到点（PTP）运动中已完成的重复次数。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 714
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 732
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RptCounter

统计重复点到点（PTP）运动中已完成的重复次数。

## 概述

`RptCounter` 报告重复 PTP 运动中已完成的重复次数。仅当 [MotionMode](../02-motion-configuration/MotionMode.md) `= 2`（重复 PTP 运动）时使用。重复的定义取决于 [RptMode](../02-motion-configuration/RptMode.md)。一旦 `RptCounter` 等于非零的 [RptCycles](../02-motion-configuration/RptCycles.md)，重复 PTP 运动即停止。

## 工作原理

当命令新的运动时，`RptCounter` 被重置为 `0`（`Begin` 处理程序会在重置 `MotionReason` 和 `InTargetStat` 的同时重置它）。此后，控制器在每次重复结束时将其递增 1——具体而言，是在某次重复的平滑等待时间结束后，且仅在重复 PTP 模式下。

递增后，控制器决定是否开始下一次重复：仅当没有待处理的 [StopRep](../04-motion-command/StopRep.md) 且 [RptCycles](../02-motion-configuration/RptCycles.md) `= 0`（无限运行）或 `RptCounter ≠ RptCycles` 时才继续。当 `RptCounter` 达到非零的 `RptCycles` 时，运动结束而不循环。每次重复的下一个目标由 [RptMode](../02-motion-configuration/RptMode.md) 设定：模式 `0`（双向）返回起始位置，使轴来回运动；模式 `1`（单向）每次重复按相同增量前进，使轴持续向同一方向步进。

## 示例

```text
ARptCounter         ; 读取已完成的重复次数
```

### 边界情况

- **电机关闭：** 保留上次完成重复的值；由下一次 `Begin` 重置为 `0`。
- **越界"写入"：** `RptCounter` 为只读。
- **仿真模式（`MotorType` = 5）：** 计数器在仿真规划器完成时正常递增。
- **ModRev 环绕：** 与计数器无关——计数器按重复次数递增，而非按位置递增。
- **活动故障：** 轴在重复进行中被禁用；计数器保持当前值，直到下一次 `Begin`。
- **其他运动模式：** 计数器在 `MotionMode = 2` 以外不递增；在其他模式下读取将反映上次重复运行的值（或 0）。
- **计数器饱和：** 该参数为 32 位有符号值（最大 ≈ 2.1 × 10⁹）；对于无限 `RptCycles = 0` 运行，计数器理论上可能溢出，但实际机器不会运行足够长的时间到达此值。

## 另请参阅

- [MotionMode](../02-motion-configuration/MotionMode.md) — 选择重复 PTP 运动（`= 2`）
- [RptCycles](../02-motion-configuration/RptCycles.md) — 停止运动的目标重复次数
- [RptMode](../02-motion-configuration/RptMode.md) — 定义重复的计数方式
- [StopRep](../04-motion-command/StopRep.md) — 在当前重复结束后终止重复 PTP 运动
