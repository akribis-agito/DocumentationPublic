---
keyword: EventTableEnd
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 185
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
# EventTableEnd

**Definition:**

EventTableEnd sets the ending index of the active region within the event table, defining the last entry used for event generation. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventTableBeg](EventTableBeg.md), [EventTable](EventTable.md), [EventTableSel](EventTableSel.md)
