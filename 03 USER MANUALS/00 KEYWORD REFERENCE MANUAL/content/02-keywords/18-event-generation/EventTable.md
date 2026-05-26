---
keyword: EventTable
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 316
attributes:
  access: rw
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
# EventTable

**Definition:**

EventTable is an array of positions at which event output pulses are generated. Each element defines an absolute position trigger point in user units. It is an axis-related array parameter and is not saved to flash.

**See also:**

[EventTableCor](EventTableCor.md), [EventTableSel](EventTableSel.md), [EventTableSrc](EventTableSrc.md), [EventTableWid](EventTableWid.md)
