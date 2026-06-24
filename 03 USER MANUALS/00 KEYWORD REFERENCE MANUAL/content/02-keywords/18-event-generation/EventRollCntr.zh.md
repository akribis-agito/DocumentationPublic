---
keyword: EventRollCntr
summary: 事件位置计数器发生环绕的位置跨度（循环回绕阈值）。
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 738
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
language: zh-CN
---
# EventRollCntr

事件位置计数器发生环绕的位置跨度（循环回绕阈值）。

## 概述

`EventRollCntr` 设置事件生成机制的循环回绕阈值，定义事件位置计数器发生环绕前的位置跨度（以用户单位表示）。它与 [EventRollOff](EventRollOff.md) 配合使用——后者在每次循环回绕后对事件网格进行偏移——以支持周期性或旋转类应用。该参数为轴相关参数，保存至闪存，可随时更改。

## 工作原理

在旋转或重复性应用中，比较器可通过对其内部位置参考进行环绕来无限持续触发，而无需超出表格范围或数值范围。`EventRollCntr` 设置该环绕发生的位置跨度，[EventRollOff](EventRollOff.md) 设置每次环绕后事件网格的偏移量，使下一周期的事件触发到预期位置。

当使用 [EventOn](EventOn.md) = 1 使能事件时，这些设置将被读取并应用于循环回绕单元，适用于单事件和按间距方案（[EventType](EventType.md) = 0 和 1）。若 [EventRollOff](EventRollOff.md) 为 0，则循环回绕被禁用：控制器将 `EventRollCntr` 强制置 0，比较器不进行环绕运行。在使能之前，须同时设置 `EventRollCntr`（跨度）和非零的 [EventRollOff](EventRollOff.md)，以启用周期性行为。

## 示例

```text
AEventRollOff=100        ; non-zero shift per cycle; this also enables rollover
AEventRollCntr=360000    ; wrap the event counter every 360000 user units
AEventRollCntr           ; query the current rollover threshold
```

## 版本间差异

在 central-i v5 上，循环回绕功能仅部分实现。建议在 v4 上使用基于循环回绕的周期性事件生成；在 v5 上，请在正式依赖之前验证您的配置下的行为。

## 另请参阅

- [EventRollOff](EventRollOff.md) — 循环回绕时应用的偏移量
- [EventSelect](EventSelect.md) — 选择事件脉冲驱动的输出线
- [EventTable](EventTable.md) — 事件位置表
