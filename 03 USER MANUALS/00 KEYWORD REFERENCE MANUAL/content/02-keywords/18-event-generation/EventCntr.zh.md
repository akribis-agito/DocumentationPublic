---
keyword: EventCntr
summary: 报告事件进度；已验证硬件表计数已退出目标。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 186
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
language: zh-CN
---
# EventCntr

统计自上次 EventOn 以来生成的事件数；可由用户重置。

## 已验证硬件事件表（EventType=3，且由 EventLoad 会话占用）

报告当前一致远程快照中的**已退出目标数**，不是实测电气脉冲或边沿数。零脉宽或零输出掩码记录可无边沿退出；翻转记录的边沿数和周期数也不同。接受 EventLoad 时清零，完成或中止后保留最终计数，直到接受新加载。须结合 EventStatus 检查会话、新鲜度和完成状态。表会话持有所有权时禁止写入此状态；写计数器不等于重置远程引擎。下文传统脉冲计数说明不适用于此模式。

下文的传统行为也适用于没有已验证表会话占用轴时的 EventType=3。已验证表能力仅限制 EventLoad，不限制传统硬件表使能。

## 概述

`EventCntr` 统计自上次置位 [EventOn](EventOn.md) 以来发生的事件数。使用它可确认运动过程中产生了多少事件脉冲，或验证相对于已配置的表或范围的预期事件覆盖情况。

## 工作原理

控制器每次事件输出触发时将 `EventCntr` 加一——即在每个产生脉冲的位置越过时（包括单次事件或表序列的最后一个事件）。计数器在 [EventOn](EventOn.md) `0 → 1` 置位边沿时重置为 `0`，因此每次置位运行都从零开始计数。用户也可以随时写入 `0` 来重置它。

由于它按触发脉冲递增，`EventCntr` 是确认短暂事件的可靠方式，这些事件可能太短暂而无法通过 [EventLoopback](EventLoopback.md) 观测。

## 示例

```text
AEventCntr          ; read the number of events since the last EventOn
AEventCntr=0         ; reset the counter
```

## 另请参阅

- [EventOn](EventOn.md) — 切换它将重置此计数器
- [EventNextPos](EventNextPos.md) — 下一个将要生成的事件的位置
