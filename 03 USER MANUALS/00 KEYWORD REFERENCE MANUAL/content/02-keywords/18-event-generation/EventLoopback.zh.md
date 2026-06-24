---
keyword: EventLoopback
summary: 控制器输入电路所检测到的事件输出状态（硬件回环），只读。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 565
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    can_code: 372
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EventLoopback

控制器输入电路所检测到的事件输出状态（硬件回环），只读。

## 概述

`EventLoopback` 是一个只读状态变量，用于报告当前轴的事件生成是否正在进行。可使用该变量确认事件输出在预期时处于激活状态。它是一个轴相关状态变量，不保存至闪存。

该状态仅在 Central-i 产品上维护，其值来自远程驱动器在每个控制周期回报的"事件进行中"指示。在独立产品上，固件不更新此变量，因此其值保持为 `0`。

## 工作原理

| 值 | 含义 |
|-------|---------|
| 0 | 无事件生成进行中。 |
| 1 | 该轴的事件生成正在进行中。 |

在 Central-i 产品上，控制器每个控制周期从远程驱动器回报的指示刷新此状态。由于该值跟踪驱动器的"进行中"指示，而非每个单独脉冲边沿，因此单个极短脉冲不一定能被观测为 `1`；可使用 [EventCntr](EventCntr.md) 确认已产生的脉冲数量。`EventLoopback` 最适合用于确认持续有效或长时间有效的输出。

## 示例

```text
AEventLoopback      ; 读取事件生成是否进行中（0 或 1）
```

## 另请参阅

- [EventOn](EventOn.md) — 使能位置触发输出
- [EventCntr](EventCntr.md) — 计数脉冲；用于验证短事件
- [EventAlwaysOn](EventAlwaysOn.md) — 连续按间隔生成
- [EventSelect](EventSelect.md) — 选择脉冲驱动的输出线路
