---
keyword: PDEncFilt
summary: 保留的脉冲方向关键字；在当前固件中未实现。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 62
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# PDEncFilt

保留的脉冲方向关键字；在当前固件中未实现。

## 概述

`PDEncFilt` 是一个保留关键字。它被标记为未实现，没有读/写行为。它原本用作 P/D 输入的噪声滤波器，但该功能从未实现，因此该关键字无效。P/D 输入格式本身通过 [PDSubType](PDSubType.md) 选择。

> **文档待补充：** 该关键字为保留且未实现。请勿使用。

## 另请参阅

- [PDPos](PDPos.md) — 缩放后的 P/D 计数器
- [PDEncDir](PDEncDir.md) — P/D 累积方向
- [PDSubType](PDSubType.md) — 选择输入信号格式
