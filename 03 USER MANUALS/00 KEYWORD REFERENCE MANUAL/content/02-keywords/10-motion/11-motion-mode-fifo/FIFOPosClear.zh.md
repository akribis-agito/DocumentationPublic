---
keyword: FIFOPosClear
summary: 命令，清除 FIFO 位置队列中所有待处理的段。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 667
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
---
# FIFOPosClear

命令，清除 FIFO 位置队列中所有待处理的段。

## 概述

`FIFOPosClear` 清空位置跟踪队列，丢弃所有已压入但尚未消耗的目标，并将空闲空间重置为完整队列深度。它是 [FIFOPosPush](FIFOPosPush.md)（填充队列）的对应命令。可在任何时刻发出，包括运动中。

## 工作原理

清空操作重置队列的内部记账状态，使所有槽位均空闲，且不存在最旧或最新条目——下次读取 [FIFOPosStatus](FIFOPosStatus.md) 时队列报告为空。它仅丢弃已排队的目标，不会停止轴。在队列激活（[FIFOPosFIFOEn](FIFOPosFIFOEn.md) 设为 `1`）的情况下，于运动中执行清空后队列中无内容可弹出，轴将保持最后一个工作目标，直到压入新目标或运动停止。

此命令适用于在流式传输新轨迹前冲刷旧轨迹，或在原计划目标集不再需要时进行恢复。

## 示例

```text
AFIFOPosClear        ; 丢弃所有已排队的目标
```

## 另请参阅

- [FIFOPosPush](FIFOPosPush.md) — 压入位置目标
- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — 使能队列流式传输
- [FIFOPosStatus](FIFOPosStatus.md) — 队列状态
