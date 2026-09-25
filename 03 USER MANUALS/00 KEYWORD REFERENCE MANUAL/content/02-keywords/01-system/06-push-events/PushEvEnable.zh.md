---
keyword: PushEvEnable
summary: 推送事件总开关；任何 0 与 1 之间的切换都会清空事件队列。
availability:
  standalone: []
  central-i:
  - v5
can_code: 907
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
language: zh-CN
---
# PushEvEnable

推送事件总开关；任何 0 与 1 之间的切换都会清空事件队列。

## 概述

`PushEvEnable = 1` 开启[推送事件](00-overview.md)：控制器开始检测 [PushEvSelect](PushEvSelect.md) 中所选的事件类型，并通过推送套接字（TCP 端口 50010）将其发送给上位机。`PushEvEnable = 0`（默认）将其关闭，此时不检测也不入队任何事件。

该关键字**不保存至闪存**。上电后推送事件始终处于关闭状态，需要使用推送事件的上位机自行将其开启。

## 工作原理

任何实际的数值变化（从 0 到 1 或从 1 到 0）都会复位事件队列：

- 丢弃所有已入队的事件，因此 [PushEvStat](PushEvStat.md) 恢复为 64（所有行空闲）；
- [PushEvLost](PushEvLost.md) 清零。[PushEvTotLost](PushEvTotLost.md) 不变。

写入与当前值相同的值不会产生任何变化，队列保持不变。

如果在运动过程中开启推送事件，正在进行的运动不会在开启的瞬间被报告为已结束。控制器在开始检测之前会记录每个轴当前的运动状态，因此只有之后发生的运动结束才会产生事件。

若要以空队列开始一次上位机会话（例如重新连接推送套接字之后），请先写入 `0`，再写入 `1`。

## 示例

```text
APushEvEnable=1      ; start detecting and sending push events
APushEvEnable        ; read the switch
APushEvEnable=0      ; stop; the queue is emptied
```

## 另请参阅

- [Push Events 概述](00-overview.md) — 事件类型、发送规则和数据包格式
- [PushEvSelect](PushEvSelect.md) — 各轴检测哪些事件类型
- [PushEvStat](PushEvStat.md) / [PushEvLost](PushEvLost.md) — 复位后的队列状态
