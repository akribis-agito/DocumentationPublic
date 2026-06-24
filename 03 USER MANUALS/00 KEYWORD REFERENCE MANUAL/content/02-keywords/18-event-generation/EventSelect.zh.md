---
keyword: EventSelect
summary: 选择多事件输出组中当前事件脉冲所驱动的输出线。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 317
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
  - 7
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-28'
doc_revision: '2026.06'
language: zh-CN
---
# EventSelect

选择多事件输出组中当前事件脉冲所驱动的输出线。

## 概述

事件生成器可驱动一组事件输出线。`EventSelect` 选择下一个事件脉冲被路由到该组中的哪条线（或哪几条线），其余线保持空闲（"阻断"）状态。它**不**选择位置触发方案——那是 [EventType](EventType.md) 的职责——也不对事件生成进行使能，使能由 [EventOn](EventOn.md) 完成。

`EventSelect` 是轴相关参数，保存至闪存，可随时更改。默认值为 `1`（第一条输出线）。

## 工作原理

写入 `EventSelect` 时，控制器对事件输出路由进行编程，使下一个脉冲仅出现在所选线上；未选中的线保持其空闲电平。被阻断线的空闲电平跟随 [EventPulseWid](EventPulseWid.md) 的符号：

| EventPulseWid 符号 | 被阻断线的空闲电平 |
|--------------------|--------------------|
| 正（正常极性） | 低（`0`） |
| 负（反转极性） | 高（`1`） |

在表格模式（[EventType](EventType.md) = 2 或 3）下，活动线取自 [EventTableSel](EventTableSel.md) 中每个条目的值，而非单一的 `EventSelect` 设置：随着生成器在表格中推进，`EventSelect` 从每个事件对应的表格条目中重新加载，因此不同位置可在不同输出线上触发。因此，在表格序列运行期间读取 `EventSelect`，返回的是最近一次事件所使用的输出线。

## 示例

```text
AEventSelect=1       ; route event pulses to output line 1 (default)
AEventSelect        ; read the line used by the current/most recent event
```

## 另请参阅

- [EventTableSel](EventTableSel.md) — 表格模式下各条目的输出线选择
- [EventType](EventType.md) — 单事件 / 按间距 / 表格位置触发方案
- [EventPulseWid](EventPulseWid.md) — 脉冲宽度与极性；其符号设置被阻断线的空闲电平
- [EventOn](EventOn.md) — 使能事件生成
