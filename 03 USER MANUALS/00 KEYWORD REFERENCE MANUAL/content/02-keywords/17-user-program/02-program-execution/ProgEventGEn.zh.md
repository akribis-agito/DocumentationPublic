---
keyword: ProgEventGEn
summary: 所有用户程序事件处理服务的全局启用。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 526
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventGEn

所有用户程序事件处理服务的全局启用。

## 概述

`ProgEventGEn` 全局启用（`1`）或禁用（`0`）所有用户程序事件的*服务处理*，而不影响事件的感知。与 [ProgEventOn](ProgEventOn.md)（同时门控感知与服务，且在设置为 0 时清除所有待处理实例）不同，`ProgEventGEn` 仅门控服务处理。与各事件的服务门控 [ProgEventEn](ProgEventEn.md) 类似，将 `ProgEventGEn = 0` 时，感知仍完全有效：事件仍会评估其触发条件，并可进入"待处理服务"状态（[ProgEventStat](ProgEventStat.md)` = 1`），但不会有处理程序运行。当 `ProgEventGEn` 重新设置为 `1` 时，期间已进入待处理状态的事件将随即得到服务。使用该参数可整体暂停和恢复事件处理，而不会丢失待处理的触发。它是一个非轴标量参数，不保存至闪存（默认值为 `0`）。

## 工作原理

要使事件的处理程序运行，三个门控必须同时打开：[ProgEventOn](ProgEventOn.md)` = 1`、`ProgEventGEn = 1`，以及该事件的 [ProgEventEn](ProgEventEn.md)` = 1`。`ProgEventGEn` 门控的是处理程序调度步骤（该步骤扫描事件 1→5，并在主线程上运行第一个已启用且待处理的事件）。由于在 `ProgEventGEn = 0` 期间感知仍持续进行，该参数适合用于关键区段：待处理事件会排队，并在重新启用服务后按顺序得到处理。

## 示例

```text
AProgEventGEn=0      ; suspend servicing of all events (events still sensed)
AProgEventGEn=1      ; resume servicing; pending events are then handled
```

## 另请参阅

- [ProgEventEn](ProgEventEn.md) — 各事件的启用/禁用
- [ProgEventStat](ProgEventStat.md) — 各事件状态
- [ProgEventOn](ProgEventOn.md) — 事件处理启用
