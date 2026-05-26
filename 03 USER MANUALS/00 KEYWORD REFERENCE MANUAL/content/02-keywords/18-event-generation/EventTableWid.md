---
keyword: EventTableWid
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 497
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
  - -1
  - 10000000
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableWid

**Definition:**

EventTableWid is an array that specifies the pulse width for each event table entry individually, overriding the global EventPulseWid for selected entries. A value of -1 uses the global pulse width. It is an axis-related array parameter and is not saved to flash.

**See also:**

[EventPulseWid](EventPulseWid.md), [EventTableSel](EventTableSel.md), [EventTable](EventTable.md)
