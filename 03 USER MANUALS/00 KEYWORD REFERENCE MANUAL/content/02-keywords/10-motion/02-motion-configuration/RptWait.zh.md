---
keyword: RptWait
summary: 重复点到点运动各次重复之间的驻留时间，单位为毫秒。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 147
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 65.536
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RptWait

重复点到点运动各次重复之间的驻留时间，单位为毫秒。

## 概述

`RptWait` 是在重复运动期间相邻点到点运动之间插入的驻留时间，单位为毫秒。它仅在 [MotionMode](MotionMode.md) = 2（重复点到点运动）时使用，用于控制由 [RptCycles](RptCycles.md) 计数的各次单独重复之间的暂停。它是一个轴相关参数，保存至闪存，可在任何时候更改，包括运动期间。

## 工作原理

当一次重复完成并需要开始另一次重复时，控制器将 [MotionStat](../05-motion-status/MotionStat.md) 的 bit 1（驻留）置位，并清零一个驻留计数器。在该位置位期间，规划器处于驻留分支：每个控制周期递增驻留计数器并与 `RptWait` 比较。在计数器达到 `RptWait` 之前，规划器使轴保持静止（规划器速度强制为零），并执行正常的到位/整定记账，与各次独立运动之间完全相同。

当驻留计数器达到 `RptWait` 时，控制器清除 bit 1，加载下一个目标（由 [RptMode](RptMode.md) 决定该目标是原始起点还是下一步），重新置位到位状态和摩擦补偿标志，然后下一次运动开始。当 `RptWait = 0` 时，等待分支立即满足，因此下一次运动在紧接的下一个周期开始，没有驻留。

您设置的值以毫秒为单位；控制器使用采样时间缩放因子将其转换为整数个伺服周期（驻留计数器每个控制周期递增，并计数至该转换后的目标值），因此实际暂停时间约为 `RptWait` 毫秒，四舍五入到最接近的控制周期。如果在驻留期间到达 [StopRep](../04-motion-command/StopRep.md)（或故障停止），运动立即结束，不会开始下一次重复。

### 边界情况

- **电机失能：** 保持该值；轴禁用时不进入驻留分支。
- **越界写入：** 参数系统拒绝负值；范围在缩放单位下为 `0`–`2^31−1`。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 无关；驻留计数器与位置无关。
- **存在活动故障：** 轴被禁用，驻留立即结束；该次重复被放弃。
- **其他运动模式：** 在 [MotionMode](MotionMode.md) `= 2` 之外 `RptWait` 被忽略。
- **`RptWait = 0`：** 无驻留——下一次运动在紧接的下一个控制周期开始。通常在驻留期间运行的整定/到位记账被合并到运动转换中。
- **驻留期间停止/中止：** [Stop](../04-motion-command/Stop.md)、[Abort](../04-motion-command/Abort.md) 和 [StopRep](../04-motion-command/StopRep.md) 都会在下一个周期结束该次重复（无后续运动）。
- **可在运动中更改：** 与 `RptCycles`/`RptMode` 不同，`RptWait` 可在轴运动期间更改——在驻留期间更改会立即生效（与运行中的计数器比较）。

## 示例

```text
ARptWait=500         ; dwell 500 ms between repetitions
ARptWait            ; query current value
```

## 参见

- [MotionMode](MotionMode.md) — 必须为 2，`RptWait` 才适用
- [RptCycles](RptCycles.md) — 重复次数
- [RptMode](RptMode.md) — 重复方向
- [MotionStat](../05-motion-status/MotionStat.md) — bit 1 报告驻留
- [StopRep](../04-motion-command/StopRep.md) — 结束重复运动（也包括在驻留期间）
