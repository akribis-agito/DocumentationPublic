---
keyword: EventTableSrc
summary: 选择用于评估事件表触发的位置来源。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 313
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
---
# EventTableSrc

选择用于评估事件表触发的位置来源。

## 概述

`EventTableSrc` 选择在生成表驱动事件时比较器使用哪组表位置：[EventTable](EventTable.md) 中的原始条目，或 [EventTableCor](EventTableCor.md) 中经误差映射校正的条目。这是一个保存至闪存的轴相关参数，可随时修改。

## 工作原理

| 值 | 与反馈进行比较的位置来源 |
|-------|-------------------------------------------|
| 0 | 原始表：直接使用 [EventTable](EventTable.md) 中的值作为比较位置。 |
| 1 | 已校正表：使用由 [EventCorrect](EventCorrect.md) 生成的 [EventTableCor](EventTableCor.md) 中的值作为比较位置。 |

当编码器误差映射处于活动状态且希望脉冲在*真实*指令位置触发而非未校正位置时，使用 `EventTableSrc` = 1。在使能事件前先运行 [EventCorrect](EventCorrect.md) 以填充 [EventTableCor](EventTableCor.md)。

当纯软件比较生效时，比较器读取的反馈已经过误差校正，因此无论本参数设置如何，均使用原始 [EventTable](EventTable.md)。

## 示例

```text
AEventTableSrc=0     ; 与原始 EventTable 比较（默认）
AEventTableSrc=1     ; 与已校正的 EventTableCor 比较
AEventTableSrc       ; 查询当前来源
```

## 另请参阅

- [EventTable](EventTable.md) — 事件位置表
- [EventSelect](EventSelect.md) — 选择事件脉冲驱动哪条输出线
- [EventTableBeg](EventTableBeg.md) — 第一个活动表索引
