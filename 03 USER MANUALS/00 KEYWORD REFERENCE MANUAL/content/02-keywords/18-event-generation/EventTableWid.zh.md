---
keyword: EventTableWid
summary: 按条目脉冲宽度数组；-1 表示使用全局 EventPulseWid。
language: zh-CN
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 497
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
  - -1
  - 10000000
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# EventTableWid

按条目脉冲宽度数组；-1 表示使用全局 EventPulseWid。

## 概述

`EventTableWid` 是一个数组，为每个 [EventTable](EventTable.md) 条目单独指定脉冲宽度，覆盖选定条目的全局 [EventPulseWid](EventPulseWid.md)。宽度单位与 `EventPulseWid` 相同，遵循 [EventPulseRes](EventPulseRes.md)（微秒或纳秒）。这是一个轴相关的数组参数，不保存至闪存。

按条目宽度仅在软件事件按表方案（[EventType](EventType.md) = `2`）中应用。在硬件缓冲表方案（[EventType](EventType.md) = `3`）以及所有非表方案中，`EventTableWid` 被忽略，使用全局 [EventPulseWid](EventPulseWid.md)。

## 工作原理

宽度行为首先由起始条目（位于 [EventTableBeg](EventTableBeg.md) 索引处）的值决定，该值为整个事件会话设定模式：

| 起始条目值 | 整个活动范围的行为 |
|-------------------|-------------------------------------|
| 0 | 整个会话采用**切换模式**：每次事件改变输出状态，而不产生固定时长的脉冲。按条目宽度不应用。 |
| -1（默认） | 对**每个**事件使用全局 [EventPulseWid](EventPulseWid.md)；按条目宽度被忽略。 |
| 正值 | 使用**按条目宽度**，并向后传递（见下文）。 |

当起始条目为正值时，每个条目的宽度按如下规则解析：

| 条目值 | 该条目使用的宽度 |
|-------------|---------------------------|
| 正值 | 该值作为脉冲时长（单位参见 [EventPulseRes](EventPulseRes.md)）。同时成为后续 `-1` 条目的向后传递宽度。 |
| -1 | 向后传递宽度——即活动范围中更早出现的最近非 `-1` 按条目值；若尚未出现，则使用全局 [EventPulseWid](EventPulseWid.md)。（`0` 条目也会将传递宽度更新为 `0`，因此后续 `-1` 条目将产生零宽度脉冲，而非回溯到更早的正值。） |
| 0 | 该条目产生零宽度脉冲。非起始条目的 `0` **不会**触发切换——切换模式仅在起始条目本身为 `0` 时启用。 |

每个条目的有效范围为 -1 至 10000000；-1 是唯一的负值（延用全局宽度）。输出极性取自该条目实际使用宽度的符号：按条目宽度始终为非负值，因此仅当条目通过 `-1` 延用负值全局 [EventPulseWid](EventPulseWid.md) 时才发生反相。正值的按条目宽度不会反相，即使全局值为负。

若希望整个表默认使用全局宽度，将起始条目（[EventTableBeg](EventTableBeg.md) 索引处）设为 `-1`；若希望整个会话处于切换模式，则设为 `0`。

## 示例

```text
; 按条目宽度（起始条目为正值）：将起始条目设为一个宽度值
AEventTableWid[1]=50     ; 起始条目：50 单位脉冲；启用按条目模式
AEventTableWid[2]=100    ; 第二个条目使用 100 单位脉冲
AEventTableWid[3]=0      ; 第三个条目产生零宽度脉冲（不触发切换）
AEventTableWid[2]        ; 查询第二个条目的脉冲宽度

; 整个范围使用全局宽度：将起始条目设为 -1
AEventTableWid[1]=-1     ; 整个活动范围使用全局 EventPulseWid；
                         ; 其他条目的按条目值被忽略

; 整个会话使用切换模式：将起始条目设为 0
AEventTableWid[1]=0      ; 每次事件切换输出状态，而不产生脉冲
```

## 另请参阅

- [EventPulseWid](EventPulseWid.md) — 条目为 -1 时使用的全局脉冲宽度
- [EventTableSel](EventTableSel.md) — 按条目选择
- [EventTable](EventTable.md) — 事件位置表
