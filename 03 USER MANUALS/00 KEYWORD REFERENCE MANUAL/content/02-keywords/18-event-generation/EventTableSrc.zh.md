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

`EventTableSrc` 选择在生成表驱动事件时比较器使用哪组表位置：[EventTable](EventTable.md) 中的原始条目，或 [EventTableCor](EventTableCor.md) 中经误差映射校正的条目。这是一个保存至闪存的轴相关参数，通常可随时修改；由 EventLoad 管理的模式 3 须遵守下述已准备硬件表的限制。

## 工作原理

| 值 | 与反馈进行比较的位置来源 |
|-------|-------------------------------------------|
| 0 | 原始表：直接使用 [EventTable](EventTable.md) 中的值作为比较位置。 |
| 1 | 已校正表：使用由 [EventCorrect](EventCorrect.md) 生成的 [EventTableCor](EventTableCor.md) 中的值作为比较位置。 |

当编码器误差映射处于活动状态且希望脉冲在*真实*指令位置触发而非未校正位置时，使用 `EventTableSrc` = 1。在使能事件前先运行 [EventCorrect](EventCorrect.md) 以填充 [EventTableCor](EventTableCor.md)。

当纯软件比较生效时，比较器读取的反馈已经过误差校正，因此无论本参数设置如何，均使用原始 [EventTable](EventTable.md)。

### AGM800 已准备的硬件表

对于支持 [EventLoad](EventLoad.md) 的 `EventType=3`，应在加载前选择位置源。源为 1 时，先运行 `EventCorrect` 并检查 `EventTableCor`，再执行 `EventLoad`。加载器将这些校正值与原有表偏移及硬件坐标转换配合使用，不会重复应用误差映射。修改位置源或相关表格、映射、坐标设置会使已准备的数据失效，运行期间不允许修改。


校正点间距较小时，应在运行前检查实际的 `EventTableCor` 数值。现有 EventCorrect 舍入可能产生一个计数的误差或重复位置；本预加载功能不改变该运算。


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
