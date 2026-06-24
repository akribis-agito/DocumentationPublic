---
keyword: RptCycles
summary: 重复点到点运动的重复次数；0 表示无限期重复。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 713
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 731
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# RptCycles

重复点到点运动的重复次数；`0` 表示无限期重复。

## 概述

`RptCycles` 定义重复点到点运动的重复次数。它仅在 [MotionMode](MotionMode.md) = 2（重复点到点运动）时使用。何为一次重复取决于 [RptMode](RptMode.md)。一旦计数达到 `RptCycles`，运动即结束；若 `RptCycles=0`，运动将无限期重复（直至 [StopRep](../04-motion-command/StopRep.md)）。运行中的重复计数由 [RptCounter](../05-motion-status/RptCounter.md) 报告。它无法在轴运动中更改。

## 工作原理

当重复运动开始时，`Begin` 会将 [RptCounter](../05-motion-status/RptCounter.md) 重置为 `0`。在每个单独运动结束时 —— 在平滑尾段（`2^Jerk` 个周期）已刷新之后 —— 控制器递增 `RptCounter`，然后决定是否继续：

```text
continue  if  MotionMode == 2
          and StopRep not requested
          and ( RptCycles == 0  OR  RptCycles != RptCounter )
```

当该条件成立时，轴进入停留状态（[MotionStat](../05-motion-status/MotionStat.md) 位 1 被置位，等待计数器复位），并在 [RptWait](RptWait.md) 后跟随另一次运动；否则所有运动中位被清除，运动结束。由于比较条件是 `RptCycles != RptCounter`，值 `0` 永远不会与计数器匹配，因此会永久重复，而正值会在 `RptCounter` 恰好达到它时停止。

请注意计数如何与 [RptMode](RptMode.md) 交互：在**双向**模式下，每一段（去程，然后返程）算一次计数，因此一个完整的往返周期为两次计数；在**单向**模式下，每一步算一次计数。

## 示例

```text
ARptCycles=10        ; perform 10 repetitions
ARptCycles=0         ; repeat indefinitely
ARptCycles          ; query current value
```

一个实例。在 `RptMode = 0`（双向）且 `RptCycles = 4` 时，轴进行两次往返：去、回、去、回（共 4 段）。在 `RptMode = 1`（单向）且 `RptCycles = 4` 时，轴以相同的增量前进四次（仅一个方向）。

### 边界情况

- **电机失能：** 值被保持；在下一次 `Begin` 时读取。
- **超范围写入：** 参数系统拒绝负值；有效范围为 `0`–`2^31−1`。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 无关；无论该段期间发生何种环绕事件，循环计数器都按段递增。
- **激活的故障：** 轴被禁用，运行中的重复被放弃；在重新使能并下一次 `Begin` 时，[RptCounter](../05-motion-status/RptCounter.md) 被重置为 `0`。
- **其他运动模式：** `RptCycles` 在 [MotionMode](MotionMode.md) `= 2` 之外被忽略；非重复 PTP 无论如何都只完成一次。
- **`RptCycles = 0`：** 永久重复；只有 [StopRep](../04-motion-command/StopRep.md)（或 [Stop](../04-motion-command/Stop.md)/[Abort](../04-motion-command/Abort.md)/故障）才能结束它。
- **无法在运动中更改：** 在轴运动中写入会被拒绝；排队的新值仅在下一次 `Begin` 时生效。
- **值在低于当前 RptCounter 时减小（运动之间）：** 因为测试是 `RptCycles != RptCounter`，将 `RptCycles` 降低到 `RptCounter` 已超过的值，只会在*下一次*递增时停止运动 —— 但这一点无实际意义，因为 `RptCycles` 无法在运动中写入；如果轴处于两次 `Begin` 之间，下一次 `Begin` 无论如何都会重置 `RptCounter`。

## 参见

- [RptMode](RptMode.md) —— 定义何为一次重复
- [RptWait](RptWait.md) —— 重复之间的停留时间
- [RptCounter](../05-motion-status/RptCounter.md) —— 运行中的重复计数（与 `RptCycles` 比较）
- [StopRep](../04-motion-command/StopRep.md) —— 在计数达到之前停止重复运动
- [MotionStat](../05-motion-status/MotionStat.md) —— 位 1 标记计数重复之间的停留
