---
keyword: PushEvStat
summary: 推送事件队列中的空闲行数。
availability:
  standalone: []
  central-i:
  - v5
can_code: 911
attributes:
  access: ro
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
  - 64
  default: 64
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvStat

推送事件队列中的空闲行数。

## 概述

`PushEvStat` 是[推送事件](00-overview.md)队列中空闲行数的只读计数。队列容量为 **64 行**，每行保存一个事件。队列为空时 `PushEvStat` 读数为 64，队列已满时为 0。

控制器的后台循环在每个轮次都会更新它，无论是否发送了数据。相同的数值也会在每个数据包的包头中作为 `freeRows` 字段发送给上位机，因此读取推送套接字的上位机无需轮询该关键字。包头中的值在构建数据包时（其中的事件从队列中移除之前）获取。

它是非轴值，不保存至闪存。

## 读数含义

| 取值 | 含义 |
|---|---|
| `64` | 队列为空：迄今为止的所有事件均已发送 |
| `1`-`63` | 有事件正在等待发送 |
| `0` | 队列已满：下一个事件将被丢弃并计入 [PushEvLost](PushEvLost.md) |

如果在 [PushEvEnable](PushEvEnable.md) 为 1 时该值持续偏低，可能表示没有上位机在读取推送套接字，控制器的发送不断失败，事件正在累积。

队列深度（64）也在 [Identity](../01-status/Identity.md)`[75]` 中报告。

## 示例

```text
APushEvStat          ; free rows in the event queue (64 = empty)
```

## 另请参阅

- [PushEvLost](PushEvLost.md) / [PushEvTotLost](PushEvTotLost.md) — 队列已满时丢弃的事件
- [PushEvFillPct](PushEvFillPct.md) — 强制发送的填充程度
- [Push Events 概述](00-overview.md)
