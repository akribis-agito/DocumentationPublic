---
keyword: PushEvLost
summary: 自上次发送数据包以来丢弃的推送事件数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 909
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvLost

自上次发送数据包以来丢弃的推送事件数。

## 概述

`PushEvLost` 统计自上次成功发送数据包以来，控制器因事件队列已满而不得不丢弃的[推送事件](00-overview.md)数。相同的计数也会在每个数据包的包头中作为 `missed` 字段发送给上位机，因此读取推送套接字的上位机无需轮询该关键字即可获知丢失的事件。

它是非轴计数器，不保存至闪存，上电后读数为 0。

## 工作原理

- 当 64 行的队列已满时，**新**事件被丢弃，`PushEvLost` 和 [PushEvTotLost](PushEvTotLost.md) 同时加 1。已在队列中的事件保留。
- 构建数据包时，其 `missed` 字段取 `PushEvLost` 的当前值，上限为 65535。数据包成功发送后，从 `PushEvLost` 中恰好减去该数值。因此，在构建数据包期间丢弃的事件以及超过 65535 的部分会在下一个数据包中报告，而不会丢失。
- 如果发送失败，`PushEvLost` 不变。
- [PushEvEnable](PushEvEnable.md) 在 0 与 1 之间切换时将其清零。

该关键字可写，因此上位机也可以通过写入 0 将其复位。

## 示例

```text
APushEvLost          ; events dropped since the last successful send
APushEvLost=0        ; clear the counter
```

## 另请参阅

- [PushEvTotLost](PushEvTotLost.md) — 自上电以来丢弃的事件数，从不自动清零
- [PushEvStat](PushEvStat.md) — 队列中的空闲行数
- [PushEvFlushMs](PushEvFlushMs.md) / [PushEvFillPct](PushEvFillPct.md) — 队列何时发送
