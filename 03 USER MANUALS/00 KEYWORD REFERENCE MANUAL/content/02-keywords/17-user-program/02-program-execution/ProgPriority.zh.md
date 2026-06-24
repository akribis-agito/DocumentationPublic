---
keyword: ProgPriority
summary: 设置用户程序线程的调度优先级（服务间隔）。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 296
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 10
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# ProgPriority

设置用户程序线程的调度优先级（服务间隔）。

## 概述

`ProgPriority` 设置用户程序线程的调度优先级。它是一个以线程编号为索引的数组参数，有效范围为 `1`–`10`，默认值为 `1`，用于控制解释器相对于通过 [ProgRun](ProgRun.md) 启动的其他线程，执行该线程的频率。这是一个非轴参数，并保存至闪存。

## 工作原理

解释器以协作方式运行线程，每次执行一条低级指令。在每个调度轮次中，调度器以轮询方式推进到下一个活动线程，并为其执行一条低级指令后继续，因此默认情况下所有运行中的线程以相同速率推进。

`ProgPriority` 通过充当*间隔*来改变该速率：每个线程持有一个计数器，每当调度器到达该线程时计数器递增，只有当计数器达到线程的 `ProgPriority` 值时才执行一行，之后计数器重置。效果如下：

- `ProgPriority[t] = 1`（默认值）—— 线程在每个轮次都执行一行：全速，有效优先级最高。
- 较高的值使线程执行*较少*频繁 —— 值为 `2` 时每隔一次才执行，值为 `10` 时每隔九次才执行。

换言之，**较低**的数值使线程获得**更大**的执行时间份额。可使用此参数将时间偏向时间关键型线程（保持为 `1`），同时限制后台线程（设置较高值）。该值是按线程设置的，因此适用于当前作为该线程编号运行的任何任务（参见 [ProgRun](ProgRun.md)）。

## 示例

```text
AProgPriority[1]=1   ; thread 1 at full rate (default, highest effective priority)
AProgPriority[2]=5   ; thread 2 runs one low-level instruction every 5th scheduling pass
```

## 另请参阅

- [ProgRun](ProgRun.md) — 将任务作为线程运行
- [ProgReset](ProgReset.md) — 将任务重置为初始状态
- [ProgStatAll](ProgStatAll.md) — 所有任务的综合状态
