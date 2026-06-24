---
keyword: EventNextPos
summary: 下一个事件脉冲将在其处生成的位置，只读。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 319
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
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
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EventNextPos

下一个事件脉冲将在其处生成的位置，只读。

## 概述

`EventNextPos` 是一个只读状态变量，用于报告下一个事件输出脉冲将在其处生成的位置（以用户单位表示）。可使用它监控下一个事件的预期位置，并确认生成器正在按配置的位置推进。它是一个轴相关状态变量，不保存至闪存。

## 工作原理

当 [EventOn](EventOn.md) 使能时，`EventNextPos` 被设置为所选 [EventType](EventType.md) 的第一个比较位置。每次脉冲触发后，控制器将其推进至下一个比较点：

| EventType | EventNextPos 的值 |
|-----------|-----------------------|
| 单次（0） | [EventBegPos](EventBegPos.md)（仅一个事件）。 |
| 按间隔（1） | 最近一次比较位置加 [EventGap](EventGap.md)，直至越过 [EventEndPos](EventEndPos.md)。 |
| 按表（2、3） | 来自 [EventTable](EventTable.md)（或选择校正表时来自 [EventTableCor](EventTableCor.md)）的下一个位置。 |

生成停止后（单次事件完成、按间隔窗口结束或表已耗尽），`EventNextPos` 保留最后一个值，直至引擎重新使能。

## 示例

```text
AEventNextPos       ; 读取下一个待处理事件的位置
```

## 另请参阅

- [EventType](EventType.md) — 决定下一个位置的计算方式
- [EventGap](EventGap.md) — 按间隔模式下的递增量
- [EventTable](EventTable.md) / [EventTableCor](EventTableCor.md) — 位置表（表模式）
- [EventCntr](EventCntr.md) — 已生成事件的计数
