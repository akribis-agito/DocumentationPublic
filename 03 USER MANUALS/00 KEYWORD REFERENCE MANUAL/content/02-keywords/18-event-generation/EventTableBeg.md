---
keyword: EventTableBeg
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 184
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
  - 1
  - 100
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableBeg

**Definition:**

EventTableBeg sets the starting index of the active region within the event table, allowing a subset of the table entries to be used for event generation. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventTableEnd](EventTableEnd.md), [EventTable](EventTable.md), [EventTableSel](EventTableSel.md)
