---
keyword: FIFOPosPush
summary: 将新的位置段压入 FIFO 位置队列的指令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 666
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# FIFOPosPush

将新的位置段压入 FIFO 位置队列的指令。

## 概述

`FIFOPosPush` 向位置跟踪队列追加一个绝对位置目标。随该指令写入的值即为所存储的目标位置，以位置计数为单位。当队列处于活动状态（[FIFOPosFIFOEn](FIFOPosFIFOEn.md) 置为 `1`）时，控制器随后每个周期弹出一个目标，并向各目标插值运动参考。

该指令可在任意时刻发出，包括运动过程中，这正是上位机流式传输连续轨迹的方式：上位机持续在播放进度前方压入目标，使队列永不为空。

## 工作原理

队列是固定深度的循环缓冲区（详见下方说明）。每次压入操作：

1. 检查空闲空间。若队列已满，则压入被拒绝，返回错误 273，且不添加任何内容。
2. 否则，将值存入下一个空闲（最新）槽位，并减少空闲空间计数。

控制器按 [FIFOPosCycle](FIFOPosCycle.md) 设定的周期速率从最旧端消耗目标。若压入速度落后于播放速度导致队列为空，轴将保持在最后一个目标处，而不会结束运动。队列深度、空闲空间及满载情况可从 [FIFOPosStatus](FIFOPosStatus.md) 读取，整个队列可通过 [FIFOPosClear](FIFOPosClear.md) 清空。

压入目标之间的插值方式由 [FIFOPosType](FIFOPosType.md) 设定。在应用流式参考的同时，[FIFOPosPosOf](FIFOPosPosOf.md) 叠加到位置参考，[FIFOPosVelOf](FIFOPosVelOf.md) 叠加到速度参考，[FIFOPosCurrOf](FIFOPosCurrOf.md) 叠加到电流参考。

> 队列深度因产品而异。紧凑型控制器及特定处理器版本可容纳 32 个目标；大型驱动平台可容纳 1024 个目标。请通过读取 [FIFOPosStatus](FIFOPosStatus.md) 获取实际空闲空间，而非假定固定深度。

## 示例

压入的值即为随 `FIFOPosPush` 指令写入的值，与 [FIFOPosTrgt](FIFOPosTrgt.md) 无关。

```text
AFIFOPosPush=100000  ; append target 100000 to the queue
AFIFOPosPush=120000  ; append the next target
```

## 另请参阅

- [FIFOPosFIFOEn](FIFOPosFIFOEn.md) — 使能队列流式传输
- [FIFOPosType](FIFOPosType.md) — 插值模式
- [FIFOPosCycle](FIFOPosCycle.md) — 每目标采样数
- [FIFOPosClear](FIFOPosClear.md) — 清空队列
- [FIFOPosStatus](FIFOPosStatus.md) — 队列状态
