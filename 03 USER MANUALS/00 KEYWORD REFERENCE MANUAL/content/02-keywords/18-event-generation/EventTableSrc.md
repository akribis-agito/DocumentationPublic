---
keyword: EventTableSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 313
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventTableSrc

**Definition:**

EventTableSrc selects the position source used to evaluate event table triggers, such as the command position, actual position, or an external encoder. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventTable](EventTable.md), [EventSelect](EventSelect.md), [EventTableBeg](EventTableBeg.md)
