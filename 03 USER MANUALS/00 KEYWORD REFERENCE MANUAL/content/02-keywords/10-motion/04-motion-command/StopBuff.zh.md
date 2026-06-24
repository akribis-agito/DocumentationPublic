---
keyword: StopBuff
summary: 在当前回放周期结束时停止样条缓冲区（Buff）运动，停止播放并减速至静止。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 550
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
# StopBuff

在当前回放周期结束时停止样条缓冲区（Buff）运动。

## 概述

`StopBuff` 结束样条缓冲区运动（[MotionMode](../02-motion-configuration/MotionMode.md) 样条缓冲区模式）。它不会立即减速，而是请求在**当前正在进行的周期结束时**停止回放：缓冲区播放至下一个周期起始处后终止运动。这样可保持样条轨迹连续，避免速度不连续。该命令为轴相关命令函数，可在运动过程中发出。

如需立即停止缓冲区运动，请使用 [Abort](Abort.md)（立即清除运动）；如需对所有缓冲区成员进行 `Decel` 斜坡式停止，请使用 [Stop](Stop.md)。

## 工作原理

### 请求停止

除非轴正处于样条缓冲区运动中，否则 `StopBuff` 不起作用。当轴处于该状态时，请求被置于缓冲区组的**主轴**上——主轴从 [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md) 低字节读取——在中断禁用状态下执行：

| `StopBuff` 设置的字段（在主轴上） | 值 | 含义 |
|---|---|---|
| [MotionStat](../05-motion-status/MotionStat.md) 第 17 位（样条缓冲区停止请求） | 1 | 请求在周期结束时终止缓冲区运动 |
| [MotionReason](../05-motion-status/MotionReason.md) | 35 | 记录运动因 `StopBuff` 而结束 |

### 在周期边界处结束

规划器仅在**回放周期的第一个采样时刻**检查该请求。当到达该边界且停止请求挂起时，规划器清除所有运动位，将规划器运行时间锁存至 [MotionSamples](../05-motion-status/MotionSamples.md)，并将 [MotionReason](../05-motion-status/MotionReason.md) = 35（StopBuff 指令）传播至所有成员轴。这与控制器在 [BuffCycles](../12-motion-mode-spline-buffer/BuffCycles.md) 耗尽时使用的周期结束路径相同——`StopBuff` 仅强制运动在下一个边界处结束，而非在编程的周期数完成后结束。

## 示例

```text
AStopBuff            ; end spline-buffer playback at the end of the current cycle
```

### 边界情况

- **电机关闭：** 接受但无效果。
- **未处于样条缓冲区运动中：** 无效果。
- **超出范围的"写"操作：** 该函数无值。
- **仿真模式（`MotorType` = 5）：** 不变。
- **ModRev 环绕：** 无关。
- **活动故障：** 若任一成员轴发生故障，整个缓冲区运动立即结束——所有成员的运动位被清除（包括挂起的停止请求位 17），原因变为电机关闭原因，而非 `StopBuff` 原因。之前发出的 `StopBuff` 请求在故障后不保留。
- **其他运动模式：** 只有样条缓冲区模式响应 `StopBuff`；在其他模式下为空操作。
- **单周期缓冲区：** 在周期中途发出 `StopBuff` 仍需等待周期边界；运动在当前周期完成后结束。
- **需要立即停止：** 使用 [Abort](Abort.md)（立即冻结参考值）或 [Stop](Stop.md)（通过 `Decel` 受控斜坡停止）。

## 另请参阅

- [Stop](Stop.md) — 受控停止（对缓冲区成员按 `Decel` 减速）
- [Abort](Abort.md) — 立即结束缓冲区运动
- [BuffStatus](../12-motion-mode-spline-buffer/BuffStatus.md) — 样条缓冲区回放状态（主轴、周期/索引）
- [BuffCycles](../12-motion-mode-spline-buffer/BuffCycles.md) — `StopBuff` 提前终止的编程周期数
- [MotionStat](../05-motion-status/MotionStat.md) — `StopBuff` 设置的第 17 位（样条缓冲区停止请求）
- [MotionReason](../05-motion-status/MotionReason.md) — `StopBuff` 设置的原因码 35
