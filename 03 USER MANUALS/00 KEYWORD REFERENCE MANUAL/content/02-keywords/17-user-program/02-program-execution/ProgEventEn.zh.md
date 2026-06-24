---
keyword: ProgEventEn
summary: 启用或禁用单个用户程序事件的处理服务。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 524
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 6
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
# ProgEventEn

启用或禁用单个用户程序事件的处理服务。

## 概述

`ProgEventEn` 按事件编号索引，启用（`1`）或禁用（`0`）单个用户程序事件的处理服务。当某事件被禁用时，即使触发条件发生且事件进入待处理状态，其处理程序也不会运行。感知不受影响：只要 [ProgEventOn](ProgEventOn.md)` = 1`，被禁用的事件仍会评估其触发条件并可进入待处理状态；只是在重新启用前不会被服务。这使其成为各事件的服务门控，与 [ProgEventGEn](ProgEventGEn.md)（暂停所有事件的服务）和 [ProgEventOn](ProgEventOn.md)（同时门控感知与服务的主开关）并列。每个事件的触发条件由 [ProgEventPar](ProgEventPar.md)、[ProgEventType](ProgEventType.md)、[ProgEventVal](ProgEventVal.md) 和 [ProgEventMask](ProgEventMask.md) 定义。它是一个非轴数组参数，每个事件对应一个元素（索引 `[1]`–`[5]`，最多支持 5 个事件），不保存至闪存（默认值为 `0`）。

## 工作原理

只有当三个门控全部打开时，事件的处理程序才会运行：[ProgEventOn](ProgEventOn.md)` = 1`、[ProgEventGEn](ProgEventGEn.md)` = 1`，以及该事件的 `ProgEventEn = 1`。当 [ProgEventOn](ProgEventOn.md)` = 1` 时，控制器在每个控制周期读取被监控的参数（[ProgEventPar](ProgEventPar.md)），应用 [ProgEventMask](ProgEventMask.md)，并使用 [ProgEventType](ProgEventType.md) 中的条件与 [ProgEventVal](ProgEventVal.md) 进行比较；当条件满足时，事件进入待处理状态。`ProgEventEn` 随后决定是否对该事件的待处理实例进行服务：当 `ProgEventEn[n] = 1` 时，其处理程序在主线程上运行，并在处理程序执行 [Return](Return.md) 后重新置位；当 `ProgEventEn[n] = 0` 时，处理程序被挂起，即使事件仍处于感知状态且可能保持待处理。若要清除所有待处理实例并强制每个事件回到"等待触发"状态，可将 [ProgEventOn](ProgEventOn.md) 设置为 `0`。

## 示例

```text
AProgEventEn[1]=1    ; enable servicing of event 1
AProgEventEn[1]=0    ; stop servicing event 1 (it is still sensed and may stay pending)
```

## 另请参阅

- [ProgEventGEn](ProgEventGEn.md) — 所有事件的全局启用
- [ProgEventStat](ProgEventStat.md) — 各事件状态（等待 / 待处理 / 处理中）
- [ProgEventPar](ProgEventPar.md) — 触发事件的参数
