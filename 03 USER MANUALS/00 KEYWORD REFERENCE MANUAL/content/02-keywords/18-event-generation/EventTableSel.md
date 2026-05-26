---
keyword: EventTableSel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 318
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 101
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
# EventTableSel

**Definition:**

EventTableSel is an array that assigns a width value index or mode selection to each event table entry, controlling per-entry pulse characteristics. It is an axis-related array parameter and is not saved to flash.

**See also:**

[EventTable](EventTable.md), [EventTableWid](EventTableWid.md), [EventTableBeg](EventTableBeg.md), [EventTableEnd](EventTableEnd.md)
