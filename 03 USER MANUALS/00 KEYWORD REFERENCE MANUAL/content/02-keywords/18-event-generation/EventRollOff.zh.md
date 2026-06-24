---
keyword: EventRollOff
summary: 事件计数器每次循环回绕时应用于事件网格的位置偏移量。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 739
attributes:
  access: rw
  scope: axis
  flash: true
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
  implemented: '0'
overrides:
  central-i.v4:
    implemented: final
  central-i.v5:
    implemented: partial
last_updated: '2026-05-29'
doc_revision: '2026.06'
language: zh-CN
---
# EventRollOff

事件计数器每次循环回绕时应用于事件网格的位置偏移量。

## 概述

`EventRollOff` 设置事件计数器发生循环回绕时所应用的位置偏移量（以用户单位表示），从而允许在每个周期后对事件网格进行偏移。它与 [EventRollCntr](EventRollCntr.md) 配合使用——后者定义循环回绕的位置跨度。该参数为轴相关参数，保存至闪存，可随时更改。

## 工作原理

`EventRollOff` 同时充当循环回绕功能的使能开关。当使用 [EventOn](EventOn.md) = 1 使能事件时，控制器将其与 [EventRollCntr](EventRollCntr.md) 一起读取，适用于单事件和按间距方案（[EventType](EventType.md) = 0 和 1）：

- `EventRollOff` = 0 — 循环回绕被禁用。控制器同时将 [EventRollCntr](EventRollCntr.md) 强制置 0，比较器不进行环绕运行。
- `EventRollOff` 非零 — 循环回绕被使能。每当比较器的位置参考到达 [EventRollCntr](EventRollCntr.md) 所定义的跨度时发生环绕，并将事件网格偏移 `EventRollOff`，使下一周期的脉冲触发到预期位置。

在使能之前，须同时设置两个参数；在事件运行过程中更改这些参数，不会对已使能的循环回绕单元产生追溯影响。

## 示例

```text
AEventRollCntr=360000    ; rollover span
AEventRollOff=100        ; shift the event grid by 100 user units on each rollover
AEventRollOff            ; query the current offset
```

## 版本间差异

在 central-i v5 上，循环回绕功能仅部分实现。建议在 v4 上使用基于循环回绕的周期性事件生成；在 v5 上，请在正式依赖之前验证您的配置下的行为。

## 另请参阅

- [EventRollCntr](EventRollCntr.md) — 循环回绕位置跨度
- [EventSelect](EventSelect.md) — 选择事件脉冲驱动的输出线
- [EventTable](EventTable.md) — 事件位置表
