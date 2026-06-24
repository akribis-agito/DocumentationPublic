---
keyword: EventTableSel
summary: 按条目选择数组，用于指定每个事件表条目的脉冲驱动哪条输出线。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 318
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 101
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 7
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# EventTableSel

按条目选择数组，控制每个事件表条目的输出特性。

## 概述

`EventTableSel` 是一个数组，为每个 [EventTable](EventTable.md) 条目分配一个选择值（范围 0–7），控制该条目的输出特性。它是全局 [EventSelect](EventSelect.md) 的按条目对应项：对于表驱动事件，条目的选择值在产生脉冲时取代全局模式。活动条目的范围由 [EventTableBeg](EventTableBeg.md) 和 [EventTableEnd](EventTableEnd.md) 限定。这是一个轴相关的数组参数，不保存至闪存。

## 工作原理

控制器在推进活动表范围时，读取即将触发的条目的 `EventTableSel` 值，并将其与来自 [EventTableWid](EventTableWid.md) 的该条目宽度一同应用于输出脉冲发生器。这使得不同条目在同一轮中可驱动不同的输出配置——例如，将脉冲路由到不同的事件输出，或选择哪些条目产生有效脉冲、哪些作为空闲（阻断）槽。3 位值（0–7）按脉冲应用；新选择仅在前一个脉冲完成后生效，因此间距紧密的条目不会破坏正在进行中的脉冲。

使能事件（[EventOn](EventOn.md) = 1）时，加载第一个活动条目（位于 [EventTableBeg](EventTableBeg.md)）的选择值；之后随表推进，依次加载各条目的选择值。

## 示例

```text
AEventTableSel[1]=1      ; 第一个表条目的选择值
AEventTableSel[2]=0      ; 第二个表条目的选择值
AEventTableSel[1]       ; 查询第一个条目的选择值
```

## 另请参阅

- [EventTable](EventTable.md) — 事件位置表
- [EventTableWid](EventTableWid.md) — 按条目脉冲宽度覆盖
- [EventTableBeg](EventTableBeg.md) — 第一个活动表索引
- [EventTableEnd](EventTableEnd.md) — 最后一个活动表索引
