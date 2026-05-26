---
keyword: EventNextPos
availability:
  standalone:
  - v4
  central-i:
  - v4
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
---
# EventNextPos

**Definition:**

EventNextPos is a read-only parameter that reports the position at which the next event output pulse will be generated, based on the current event table and selection. It is an axis-related status variable expressed in user units and is not saved to flash.

**See also:**

[EventTable](EventTable.md), [EventTableSel](EventTableSel.md), [EventSelect](EventSelect.md)
