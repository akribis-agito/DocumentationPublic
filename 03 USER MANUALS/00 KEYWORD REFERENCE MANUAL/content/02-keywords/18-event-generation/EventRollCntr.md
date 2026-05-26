---
keyword: EventRollCntr
availability:
  standalone:
  - v4
  central-i:
  - v4
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
  implemented: final
overrides: {}
---
# EventRollCntr

**Definition:**

EventRollCntr sets the rollover counter threshold for the event generation mechanism, defining the position span after which the event position counter wraps around. It is an axis-related parameter expressed in user units, saved to flash, and can be changed at any time.

**See also:**

[EventRollOff](EventRollOff.md), [EventSelect](EventSelect.md), [EventTable](EventTable.md)
