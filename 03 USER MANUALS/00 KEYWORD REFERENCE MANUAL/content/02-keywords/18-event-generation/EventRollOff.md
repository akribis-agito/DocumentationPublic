---
keyword: EventRollOff
availability:
  standalone:
  - v4
  central-i:
  - v4
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
  implemented: final
overrides: {}
---
# EventRollOff

**Definition:**

EventRollOff sets the position offset applied when the event counter rolls over, allowing the event grid to be shifted after each cycle. It is an axis-related parameter expressed in user units, saved to flash, and can be changed at any time.

**See also:**

[EventRollCntr](EventRollCntr.md), [EventSelect](EventSelect.md), [EventTable](EventTable.md)
