---
keyword: StopFIFO
summary: 命令，将当前正在执行的 FIFO 片段设为最后一个片段，从而结束序列。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 291
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# StopFIFO

命令，将当前正在执行的 FIFO 片段设为最后一个片段，从而结束序列。

## 概述

`StopFIFO` 通过将当前正在播放的片段设为序列的最后一个片段来停止 FIFO 运动。与通用 [Stop](../04-motion-command/Stop.md) 命令（将轴减速至零速度）不同，`StopFIFO` 允许当前活动片段以其预设速度执行完毕后再结束运动，从而使轨迹平稳完成，队列中其后剩余的片段将被丢弃。

`StopFIFO` 仅在轴当前正在执行 FIFO 运动时生效；否则无任何效果。

完整的 FIFO 运动模式说明及所有相关关键字，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

被接受后，`StopFIFO`：

- 在 [MotionStat](../05-motion-status/MotionStat.md) 中置位 FIFO 停止位——**位 8**（掩码 `0x00000100`）——使控制器和上位机工具显示 FIFO 运动正在结束。
- 在 [MotionReason](../05-motion-status/MotionReason.md) 中记录停止原因：值变为 **10**（运动因 StopFIFO 命令而结束）。
- 强制设置队列，使正在执行的片段成为最后一个：控制器将其执行至结束，然后结束运动，效果与下溢时完全相同。其后排队的条目不会被播放。

由于活动片段以当前速度运行至完成，本命令不会将轴减速至零。若需要轴停止，请在 `StopFIFO` 后跟随一个将速度降至零的运动，或改用 [Stop](../04-motion-command/Stop.md)。

## 示例

```text
AStopFIFO            ; let the current segment finish, then end the FIFO motion
```

## 另请参阅

- [Stop](../04-motion-command/Stop.md) — 将轴减速至零速度
- [MotionStat](../05-motion-status/MotionStat.md) — FIFO 停止位（位 8）
- [MotionReason](../05-motion-status/MotionReason.md) — 停止原因（StopFIFO 后 = 10）
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
- [FIFOStatus](FIFOStatus.md) — 队列状态
