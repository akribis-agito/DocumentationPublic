---
keyword: StopCNCB
summary: 停止 CNC 运动队列 B 执行的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 688
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
# StopCNCB

停止 CNC 运动队列 B 执行的指令。

## 概述

`StopCNCB` 是一个指令函数，用于停止驱动队列 B 的 CNC 运动引擎。运动以受控方式减速至静止，不再取用后续排队的段。由于它是一条指令，可在任意时刻发出，包括运动期间。

`StopCNCB` 是 [StopCNCA](StopCNCA.md) 的第二引擎对应指令。它在保留队列的同时停止运动，与 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md)（清空段队列）不同。

## 工作原理

- 若队列 B 未处于运动中，`StopCNCB` 不执行任何操作。
- 若队列 B 处于运动中，引擎被标记为停止：CNC 运动状态（[CNCAStatus/CNCBStatus](CNCAStatus-CNCBStatus.md) 的第 10 个元素）设置其停止进行中位（位 12，掩码 `0x00001000`），并取消 CNC 步进模式，使停止始终生效。
- CNCB 的每个成员轴的 [MotionStat](../05-motion-status/MotionStat.md) **CNCB 停止位（位 15，掩码 `0x00008000`）** 被置位，其 [MotionReason](../05-motion-status/MotionReason.md) 设置为 **25**（运动因 `StopCNCB` / CNCB 成员停止而结束）。
- 运动引擎随后在下一个取段机会结束运动，而不继续路径：队列中剩余的段不会被执行，但也**不会**被移除——若需从头开始，请使用 [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) 清除。若需暂停后在同一路径上继续，请使用 [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md)。

## 示例

```text
AStopCNCB            ; stop CNC motion on queue B
```

## 另请参阅

- [StopCNCA](StopCNCA.md) — 第一 CNC 引擎的停止指令
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — 从队列中清除所有待处理段
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — 在同一路径上暂停/继续，而非停止
- [MotionStat](../05-motion-status/MotionStat.md) — CNCB 停止位（位 15）
- [MotionReason](../05-motion-status/MotionReason.md) — `StopCNCB` 后设置为 25
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — 查看已排队的段数据
