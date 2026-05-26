---
keyword: EventSelect
availability:
  standalone:
  - v4
  central-i:
  - v4
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
---
# EventSelect

**Definition:**

EventSelect chooses the operating mode of the event output generator, such as table-driven, periodic, or always-on operation. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventAlwaysOn](EventAlwaysOn.md), [EventTable](EventTable.md), [EventTableSel](EventTableSel.md), [EventOn](EventOn.md)
