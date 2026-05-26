---
keyword: EventTableCor
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 315
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 101
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
# EventTableCor

**Definition:**

EventTableCor is a read-only array that holds the corrected event positions after applying the position correction computed by EventCorrect. It mirrors EventTable but with mapping offsets applied. It is an axis-related array status variable expressed in user units and is not saved to flash.

**See also:**

[EventTable](EventTable.md), [EventCorrect](EventCorrect.md), [EventTableSel](EventTableSel.md)
