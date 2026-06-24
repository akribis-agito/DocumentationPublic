---
keyword: StopCNCA
summary: 停止 CNC 运动队列 A 执行的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 456
attributes:
  access: ro
  scope: non-axis
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# StopCNCA

停止 CNC 运动队列 A 执行的指令。

## 概述

`StopCNCA` 是一个指令函数，用于停止驱动队列 A 的 CNC 运动引擎。运动以受控方式减速至静止，不再取用后续排队的段。由于它是一条指令，可在任意时刻发出，包括运动期间。

使用 `StopCNCA` 可在保留队列的同时停止运动，与 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md)（清空段队列）不同。第二引擎的对应指令为 [StopCNCB](StopCNCB.md)。

## 工作原理

- 若队列 A 未处于运动中，`StopCNCA` 不执行任何操作。
- 若队列 A 处于运动中，引擎被标记为停止：CNC 运动状态（[CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) 的第 10 个元素）设置其停止进行中位（位 12，掩码 `0x00001000`），并取消 CNC 步进模式，使停止始终生效。
- CNCA 的每个成员轴的 [MotionStat](../05-motion-status/MotionStat.md) **CNCA 停止位（位 12，掩码 `0x00001000`）** 被置位，其 [MotionReason](../05-motion-status/MotionReason.md) 设置为 **12**（运动因 `StopCNCA` 结束）。
- 运动引擎随后在下一个取段机会结束运动，而不继续路径：队列中剩余的段不会被执行，但也**不会**被移除——若需从头开始，请使用 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 清除。若需暂停后在同一路径上继续，请使用 [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md)。

## 示例

```text
AStopCNCA            ; stop CNC motion on queue A
```

## 另请参阅

- [StopCNCB](StopCNCB.md) — 第二 CNC 引擎的停止指令
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — 从队列中清除所有待处理段
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — 在同一路径上暂停/继续，而非停止
- [MotionStat](../05-motion-status/MotionStat.md) — CNCA 停止位（位 12）
- [MotionReason](../05-motion-status/MotionReason.md) — `StopCNCA` 后设置为 12
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 查看已排队的段数据
