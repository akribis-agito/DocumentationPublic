---
keyword: ProgEventOn
summary: 激活或禁用用户程序事件的处理。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 527
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventOn

激活或禁用用户程序事件的处理。

## 概述

`ProgEventOn` 是整个用户程序事件系统的主开关。它同时激活（`1`）或禁用（`0`）事件的*感知*与*服务处理*。当设置为 `0` 时，每个事件都被强制回到"等待触发"状态，所有待处理实例被丢弃，不再进行事件感知或服务处理。它是一个非轴标量参数，不保存至闪存（默认值为 `0`）。

用户程序事件允许控制器在被选参数满足所选条件时自动运行处理程序函数，而无需程序主动轮询。最多可定义 **5 个事件**（编号 1–5）。每个事件由四个参数描述，构成一个与数据记录触发非常相似的触发定义：

- [ProgEventPar](ProgEventPar.md) — 被监控的参数（触发源）
- [ProgEventType](ProgEventType.md) — 比较/边沿条件
- [ProgEventVal](ProgEventVal.md) — 用于比较的阈值
- [ProgEventMask](ProgEventMask.md) — 比较前应用的位掩码

除 `ProgEventOn` 外，另有两个开关对该引擎进行门控：[ProgEventGEn](ProgEventGEn.md)（全局）和 [ProgEventEn](ProgEventEn.md)（各事件）。区别在于它们对*感知*的影响：

| 控制参数 | 作用范围 | 设置为 0 的效果 |
|---|---|---|
| `ProgEventOn` | 所有事件 | 停止感知**和**服务处理；清除所有待处理实例（强制每个事件回到"等待触发"状态） |
| [ProgEventGEn](ProgEventGEn.md) | 所有事件 | 仅停止服务处理；事件仍被感知，可进入待处理状态 |
| [ProgEventEn](ProgEventEn.md) | 单个事件 | 仅停止该事件的服务处理；该事件仍被感知，可进入待处理状态，但在禁用期间不被服务 |

## 工作原理

三个条件必须同时为真，触发的事件才能实际运行其处理程序：`ProgEventOn = 1`、[ProgEventGEn](ProgEventGEn.md)` = 1`，以及该事件的 [ProgEventEn](ProgEventEn.md)` = 1`。完整流程如下：

![User-program event lifecycle: each event moves from waiting-for-trigger to pending-for-service when its condition is met, then to in-service when scheduled (events 1..5 are scanned in order with the lowest number winning), and finally back to waiting-for-trigger when the handler returns; all three of ProgEventOn, ProgEventGEn and ProgEventEn[n] must be 1 to run the handler](progevent-arming-timeline.svg)


1. **感知（评估）。** 在感知启用期间，控制器读取被监控的参数，应用掩码，并使用 [ProgEventType](ProgEventType.md) 所选条件与 [ProgEventVal](ProgEventVal.md) 进行比较；仅当事件处于"等待触发"状态时才对其进行评估。事件 1 为快速事件，每个控制周期都被感知；事件 2–5 按共享调度进行感知，因此评估频率低于事件 1。请将对时序要求最高的触发置于事件 1。
2. **触发。** 当条件满足时，事件进入"待处理服务"状态（由 [ProgEventStat](ProgEventStat.md)` = 1` 报告）。
3. **运行处理程序。** 处理程序在主程序线程（线程 1）上运行，且仅在该线程正在执行程序时运行。每次调度轮次，控制器扫描事件 1→5，并服务第一个已启用且待处理的事件，因此当多个事件同时待处理时，编号较小的事件具有优先权。处理程序以函数调用方式被调用：当前执行点被压入调用栈，执行跳转至该事件的处理程序；事件进入"处理中"状态（`ProgEventStat = 2`）。若没有处理程序函数绑定到该事件编号，或程序调用栈无空间进行调用，则服务处理将引发一个程序错误（通过 [ProgError](ProgError.md) 报告）。
4. **完成。** 当处理程序执行 [Return](Return.md) 时，执行恢复至被中断的位置，事件返回"等待触发"状态，为下一次触发重新置位。事件在处理中时无法再次触发。

## 示例

```text
AProgEventOn=1       ; enable the event system (sensing + servicing)
AProgEventOn=0       ; disable everything and clear all pending events
```

## 另请参阅

- [ProgEventGEn](ProgEventGEn.md) — 在保持感知有效的同时进行全局服务启用
- [ProgEventEn](ProgEventEn.md) — 各事件的启用/禁用
- [ProgEventStat](ProgEventStat.md) — 各事件状态（等待 / 待处理 / 处理中）
- [ProgEventPar](ProgEventPar.md) — 被监控的参数（触发源）
- [Return](Return.md) — 完成事件处理程序的服务
