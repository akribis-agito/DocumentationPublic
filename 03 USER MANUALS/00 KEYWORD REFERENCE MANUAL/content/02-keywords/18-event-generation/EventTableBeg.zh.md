---
keyword: EventTableBeg
summary: 事件表格活动区域的起始索引。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 184
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 100
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EventTableBeg

事件表格活动区域的起始索引。

## 概述

`EventTableBeg` 设置 [EventTable](EventTable.md) 活动区域的起始索引，允许仅使用表格条目的子集进行事件生成。它与 [EventTableEnd](EventTableEnd.md) 配对，后者标记最后一个活动条目。索引以 1 为起始；其上限等于表格大小——独立控制器为 100，central-i 最多为 65000。该参数为轴相关参数，保存至闪存，可随时更改。

## 工作原理

当使用 [EventOn](EventOn.md) = 1 使能表格驱动事件时，控制器将 `EventTableBeg` 索引处的 [EventTable](EventTable.md) 条目加载为第一个比较位置，并将该条目的 [EventTableSel](EventTableSel.md) 选择值和 [EventTableWid](EventTableWid.md) 脉冲宽度复制到活动输出设置中。之后每生成一个脉冲索引推进一位，当超过 [EventTableEnd](EventTableEnd.md) 后停止。

`EventTableBeg` 在事件使能时读取，因此须在设置 `EventOn` = 1 之前完成更改。该参数对不会与 `EventTableEnd` 相互进行范围校验：使能时始终使用 `EventTableBeg` 处的条目作为第一个比较位置，之后索引推进，超过 `EventTableEnd` 时停止。若 `EventTableBeg` 设置高于 `EventTableEnd`，则仅触发 `EventTableBeg` 处的单个条目，之后生成停止。

## 示例

```text
AEventTableBeg=1     ; start event generation at the first table entry
AEventTableBeg      ; query the configured start index
```

## 另请参阅

- [EventTableEnd](EventTableEnd.md) — 最后一个活动表格索引
- [EventTable](EventTable.md) — 事件位置表
- [EventTableSel](EventTableSel.md) — 每条目选择值
