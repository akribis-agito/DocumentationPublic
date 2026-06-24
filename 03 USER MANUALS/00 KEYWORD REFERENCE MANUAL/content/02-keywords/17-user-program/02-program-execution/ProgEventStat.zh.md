---
keyword: ProgEventStat
summary: 报告每个事件的状态，并允许清除待处理的事件。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 525
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# ProgEventStat

报告每个事件的状态，并允许清除待处理的事件。

## 概述

`ProgEventStat` 报告每个用户程序事件的状态（索引 `[1]`–`[5]`，每个事件对应一个索引）。它与触发定义（[ProgEventPar](ProgEventPar.md)、[ProgEventType](ProgEventType.md)、[ProgEventVal](ProgEventVal.md)、[ProgEventMask](ProgEventMask.md)）以及使能控制（[ProgEventEn](ProgEventEn.md)、[ProgEventGEn](ProgEventGEn.md)）共同协作，显示每个事件在其生命周期中的状态。事件处理期间，在处理完成之前——即事件处理程序执行 [Return](Return.md) 之前——该事件不能再次被触发。虽然访问属性为读/写，但只能写入 `0`，用户可通过写入 `0` 来清除待处理的事件。该参数为非轴数组参数，不保存至闪存（默认值为 `0`）。

## 工作原理

每个元素按以下生命周期步进：

| 值 | 状态 | 含义 |
|----|----|----|
| 0 | 等待触发 | 已置位并每个周期进行评估；触发条件尚未（或暂未）满足 |
| 1 | 待处理（已触发） | 条件已满足；处理程序尚未运行 |
| 2 | 处理中 | 处理程序当前正在主线程上运行 |

状态转换：

- **0 → 1**：在感测期间触发条件满足时（感测要求 [ProgEventOn](ProgEventOn.md)` = 1`；与 [ProgEventEn](ProgEventEn.md) 无关，因此即使事件的处理被禁用，事件也可变为待处理状态）。
- **1 → 2**：控制器分派处理程序时。仅当 [ProgEventGEn](ProgEventGEn.md)` = 1` 且该事件的 [ProgEventEn](ProgEventEn.md)` = 1` 时才会发生；处理程序在主线程（线程 1）上运行，当多个事件待处理时，优先处理编号最小的事件。
- **2 → 0**：处理程序执行 [Return](Return.md) 时：事件重新置位（重新捕获基准读数）并恢复感测。

将元素强制写入 `0`（唯一可写值）可清除待处理的事件并将事件返回等待状态。将 [ProgEventOn](ProgEventOn.md)` = 0` 也会将所有事件的状态强制返回 `0`。

## 示例

```text
AProgEventStat[1]   ; read the state of event 1
AProgEventStat[1]=0  ; clear a pending occurrence of event 1
```

## 另请参阅

- [ProgEventEn](ProgEventEn.md) — 单事件使能/禁用
- [ProgEventGEn](ProgEventGEn.md) — 全局处理使能
- [Return](Return.md) — 完成事件函数的处理
