---
keyword: FIFOCycleTime
summary: 当前正在执行的 FIFO 运动段的持续时长，以控制周期采样数表示。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 283
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 65536000
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# FIFOCycleTime

当前正在执行的 FIFO 运动段的持续时长，以控制周期采样数表示。

## 概述

`FIFOCycleTime` 是每个 FIFO 运动段的持续时长，以控制环采样数表示。它决定了控制器在取出队列中下一个条目之前，在当前段上进行插值的时间长度。默认值为 65536 个采样。

有关 FIFO 运动模式及所有相关关键字的完整说明，请参阅 [FIFOType](FIFOType.md)。

## 工作原理

周期时间仅在段边界处生效——即控制器完成一段并即将开始下一段时。它不会在段中途应用，因此修改该值不会干扰正在进行的段。

`FIFOCycleTime` 为**只读**；它从队列中更新：通过 [FIFOPushCycle](FIFOPushCycle.md) 压入的周期时间条目，在控制器到达该条目时成为活动周期时间，并适用于其后的每个段，直到出现下一个周期时间条目。这是在序列中改变各段时长的方式。

当一段开始时，其采样倒计时从周期时间加载（见 [FIFOStatus](FIFOStatus.md) 索引 3），每采样的运动量由此推导——例如对于位置增量段，请求的增量被分配到此采样数上。

## 范围

在所有固件版本中，周期时间被限定在 1 个控制采样到 1000 秒对应的控制采样数之间。上限随控制器的控制环采样率而变化——例如，65 536-采样/秒控制器上为 65 536 000 采样，16 384-采样/秒控制器上为 16 384 000 采样。支持的范围不因版本而异。

独立控制器在 v4 上支持此关键字；Central-i 在 v4 和 v5 上均支持。

## 示例

```text
AFIFOCycleTime            ; 读取当前段的持续采样数
AFIFOPushCycle=16         ; 压入一个周期时间条目，使下一段持续 16 个采样
```

## 另请参阅

- [FIFOType](FIFOType.md) — FIFO 模式完整说明
- [FIFOPushCycle](FIFOPushCycle.md) — 向队列压入周期时间条目
- [FIFOStatus](FIFOStatus.md) — 当前段剩余采样数（索引 3）
