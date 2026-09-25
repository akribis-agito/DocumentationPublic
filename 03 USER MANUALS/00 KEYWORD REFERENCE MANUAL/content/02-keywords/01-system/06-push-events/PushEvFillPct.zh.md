---
keyword: PushEvFillPct
summary: 强制发送的推送事件队列填充百分比。
availability:
  standalone: []
  central-i:
  - v5
can_code: 914
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 100
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvFillPct

强制发送的推送事件队列填充百分比。

## 概述

`PushEvFillPct` 是[推送事件](00-overview.md)的压力触发条件。当事件队列的填充程度至少达到 `PushEvFillPct` 百分比时，控制器立即发送已入队的事件，无需等待 [PushEvFlushMs](PushEvFlushMs.md)。取值范围为 1 至 100，默认值为 **50**。它是非轴设置，可通过 [Save](../02-operation/Save.md) 保存至闪存。

当该触发条件或 `PushEvFlushMs` 定时器**任一**满足时即发送队列。

## 工作原理

填充程度与 64 行的队列深度进行比较：

| `PushEvFillPct` | 队列中达到以下事件数时立即发送 |
|---|---|
| `1` | 1 个事件 |
| `25` | 16 个事件 |
| `50`（默认） | 32 个事件 |
| `100` | 64 个事件（队列已满） |

每个数据包最多携带 28 个事件，且控制器每个后台轮次只发送一个数据包，因此较大的积压需要经过数个轮次才能发送完毕。

该设置采用百分比而非行数，这样即使队列深度改变，其含义也保持不变。[Identity](../01-status/Identity.md)`[75]` 报告队列深度。

`PushEvFillPct` 仅作用于推送事件。同一套接字上的 `printf` 输出保持其自身固定的触发条件。

## 示例

```text
APushEvFillPct       ; read the fill trigger
APushEvFillPct=50    ; default: send once the queue is half full
APushEvFillPct=25    ; send earlier under a burst
```

## 另请参阅

- [PushEvFlushMs](PushEvFlushMs.md) — 周期性触发条件
- [PushEvStat](PushEvStat.md) — 队列中的空闲行数
- [Push Events 概述](00-overview.md) — 发送规则
