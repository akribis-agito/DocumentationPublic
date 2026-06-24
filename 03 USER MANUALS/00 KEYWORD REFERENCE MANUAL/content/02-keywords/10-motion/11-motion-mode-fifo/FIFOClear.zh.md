---
keyword: FIFOClear
summary: 命令功能，清空 FIFO 运动队列，丢弃所有条目。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 290
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# FIFOClear

命令功能，清空 FIFO 运动队列，丢弃所有条目。

## 概述

`FIFOClear` 一次性清空 FIFO 运动队列，丢弃所有已排队的条目。轴在运动中时不能发出此命令。若只需丢弃单个条目而非整个队列，请使用 [FIFORemove](FIFORemove.md)。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

执行清空操作后，队列恢复至初始空状态：回放指针返回第一个槽位，空闲条目计数恢复为 128（完整可用深度），当前段的倒计时计数、速度和加速度均清零——详见 [FIFOStatus](FIFOStatus.md) 各元素。所有已存储的类型和数值条目均被清除，因此 [FIFOType](FIFOType.md) 和 [FIFOValue](FIFOValue.md) 读回值为 0。

由于此操作会丢弃正在执行的段，`FIFOClear` 适用于运动开始前或结束后，而非回放过程中。若需平稳结束正在运行的运动，请改用 [StopFIFO](StopFIFO.md)。

## 示例

```text
AFIFOClear           ; 清空队列（空闲计数恢复为 128）
```

## 另请参阅

- [FIFORemove](FIFORemove.md) — 移除单个 FIFO 条目
- [FIFOStatus](FIFOStatus.md) — FIFO 队列状态
- [FIFOType](FIFOType.md) — FIFO 模式完整说明
