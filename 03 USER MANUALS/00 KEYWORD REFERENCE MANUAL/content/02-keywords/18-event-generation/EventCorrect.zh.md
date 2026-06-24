---
keyword: EventCorrect
summary: 根据当前轴位置和映射重新计算修正后事件表位置的命令。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 419
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EventCorrect

根据当前轴位置和映射重新计算修正后事件表位置的命令。

## 概述

`EventCorrect` 是一个命令，使用轴的有效编码器误差映射将 [EventTable](EventTable.md) 中的事件表位置转换为修正后的位置，并将其写入 [EventTableCor](EventTableCor.md)。表驱动的事件生成随后可以使用修正后的表（[EventTableCor](EventTableCor.md)），使脉冲在*真实*机械位置处触发，而不是在原始编码器读数处触发。

它是一个命令而非存储值，因此不需要参数；发出该命令即可触发重新计算。轴运动中无法执行该命令，且它不保存至闪存。

## 工作原理

对于表中的每个有效条目（从 [EventTableBeg](EventTableBeg.md) 到 [EventTableEnd](EventTableEnd.md)），控制器将列出的位置视为所需真实位置，并查找编码器必须读取的位置，以使映射（修正）后的反馈等于该值，通过有效误差映射进行插值。结果存储在 [EventTableCor](EventTableCor.md) 的对应条目中。对于多维映射，修正还使用其他已映射轴的当前位置，这就是为什么在命令运行时这些轴必须使能且静止。

该命令会检查几个前提条件，若任何条件不满足则拒绝执行（返回错误）：

| 前提条件 | 违反时的错误 | 原因 |
|--------------|-------------------|-----|
| 此轴上必须激活编码器误差映射 | 219 | 修正值来源于映射；没有映射则无从修正。 |
| 此轴的主编码器必须是其误差映射的第一个编码器 | 220 | 表位置针对此轴自身的反馈进行修正。 |
| 对于 2D/3D 映射，其他已映射轴必须使用其主编码器 | 222 | 插值读取这些轴的反馈。 |
| 对于 2D/3D 映射，其他已映射轴必须电机使能且不处于运动中 | 221 | 重新计算表时其位置必须稳定。 |

每当误差映射或源 [EventTable](EventTable.md) 发生变化时，需重新运行 `EventCorrect`，然后为表模式生成选择修正后的表。

## 示例

```text
AEventCorrect        ; recompute the corrected event-table positions
```

## 另请参阅

- [EventTable](EventTable.md) — 被修正的源位置
- [EventTableCor](EventTableCor.md) — 保存修正后的位置
- [EventType](EventType.md) — 可使用修正后表的表模式
