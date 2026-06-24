---
keyword: EventTable
summary: 生成事件输出脉冲的绝对位置数组。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 316
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 101
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EventTable

生成事件输出脉冲的绝对位置数组。

## 概述

`EventTable` 是一个绝对位置数组，在表格驱动事件模式（[EventType](EventType.md) = 2）下，在这些位置处生成事件输出脉冲。每个元素定义一个以用户单位表示的位置触发点。条目通常按轴到达的顺序排列，但不要求单调递增——支持位置先升后降的表格（详见*工作原理*）。表格的活动范围由 [EventTableBeg](EventTableBeg.md)（第一个使用的索引）和 [EventTableEnd](EventTableEnd.md)（最后一个使用的索引）界定。该参数为轴相关数组参数，不保存至闪存。

可用条目数取决于型号：独立控制器为 100 条，central-i 最多为 65000 条。由于事件表格索引以 1 为起始，条目从索引 1 开始存储，索引 0 不作为表格位置使用。

## 工作原理

当使用 [EventOn](EventOn.md) = 1 使能表格驱动事件时，控制器将 [EventTableBeg](EventTableBeg.md) 处的条目加载为第一个比较位置，并从 [EventTableSel](EventTableSel.md) 中复制其每条目选择值。随着轴运动，位置比较器监视反馈位置，当位置到达当前比较值时输出一个脉冲。每次脉冲后，控制器立即将索引推进一位，将下一个表格条目加载为新的比较位置，并应用该条目的选择值和脉冲宽度。当索引超过 [EventTableEnd](EventTableEnd.md) 后，生成停止。

比较器所监视的位置源由 [EventTableSrc](EventTableSrc.md) 选择：`EventTable` 中的原始条目，或 [EventTableCor](EventTableCor.md) 中的校正条目（当编码器误差映射激活时由 [EventCorrect](EventCorrect.md) 生成）。当使用纯软件比较时，反馈已经过校正，因此直接读取原始表格，源选择无效。

每次比较还根据相邻条目之差的符号跟踪预期的运动方向，因此位置先升后降的表格在轴反向时仍能正确触发。

## 示例

```text
AEventTable[1]=1000      ; first table position (user units)
AEventTable[2]=3000      ; second table position
AEventTable[1]           ; query the first table entry
```

触发三个脉冲的最小表格驱动设置：

```text
AEventType=2             ; table mode
AEventTableBeg=1         ; use entries 1..3
AEventTableEnd=3
AEventTable[1]=1000
AEventTable[2]=3000
AEventTable[3]=6000
AEventPulseWid=50        ; 50 us output pulse at each entry
AEventOn=1               ; arm (set while below the first entry)
```

## 另请参阅

- [EventTableCor](EventTableCor.md) — EventCorrect 后的校正位置
- [EventTableSel](EventTableSel.md) — 每条目选择值
- [EventTableSrc](EventTableSrc.md) — 表格求值的位置源
- [EventTableWid](EventTableWid.md) — 每条目脉冲宽度覆盖值
