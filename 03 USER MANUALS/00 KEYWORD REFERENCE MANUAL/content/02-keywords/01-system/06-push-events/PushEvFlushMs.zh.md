---
keyword: PushEvFlushMs
summary: 已入队的推送事件在发送前的最长等待时间，单位为毫秒。
availability:
  standalone: []
  central-i:
  - v5
can_code: 913
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
  - 1000
  default: 5
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvFlushMs

已入队的推送事件在发送前的最长等待时间，单位为毫秒。

## 概述

`PushEvFlushMs` 是[推送事件](00-overview.md)的周期性发送触发条件。自上次**成功**发送以来经过的时间超过 `PushEvFlushMs` 毫秒后，控制器发送已入队的事件。取值范围为 1 至 1000，默认值为 **5**。它是非轴设置，可通过 [Save](../02-operation/Save.md) 保存至闪存。

它与 [PushEvFillPct](PushEvFillPct.md) 配合工作：**任一**触发条件满足时即发送队列。

## 工作原理

定时器仅在数据包成功发送时重新开始计时，队列为空时不会重新开始。因此：

- **空闲通道上的单个事件**会在控制器的下一个后台轮次发送，因为距上次发送的时间通常已超过 `PushEvFlushMs`。
- **在事件持续少量到达时**，数据包最多每 `PushEvFlushMs` 发送一次。其间到达的事件被汇集后一起发送，每包最多 28 个。
- **在突发情况下**，队列达到 [PushEvFillPct](PushEvFillPct.md) 设定的程度，无需等待定时器即发送。

在默认值 5 ms 下，事件到达上位机的速度与每 5 ms 轮询一次的上位机发现该事件的速度大致相同，但不产生轮询流量。周期越长，发送的数据包越少、每包越满。如果机器更倾向于同一套接字上 `printf` 输出所用的 100 ms 节奏，可以设置 `PushEvFlushMs=100`。

`PushEvFlushMs` 仅作用于推送事件，不改变 `printf` 的发送时序。

该周期由控制器的毫秒节拍计数，该节拍以 1024 Hz 运行（每 16 个控制周期一次），因此一个单位约为 0.98 ms。

> **`PushEvFlushMs` 不限制重试。** 如果发送失败，定时器不会重新开始计时，因此无论如何设置，控制器都会在每个后台轮次重试，直到发送成功。如果上位机已连接但不读取，每次重试都可能使后台循环停顿约 5 至 6 秒。参见[概述](00-overview.md)。

## 示例

```text
APushEvFlushMs       ; read the period
APushEvFlushMs=5     ; default: send queued events within about 5 ms
APushEvFlushMs=100   ; send at most every 100 ms under a steady trickle
```

## 另请参阅

- [PushEvFillPct](PushEvFillPct.md) — 填充程度触发条件
- [PushEvStat](PushEvStat.md) — 队列中的空闲行数
- [Push Events 概述](00-overview.md) — 发送规则
