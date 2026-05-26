---
keyword: EventBegPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 181
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
# EventBegPos

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

EventBegPos is the position of the first event that will be generated in modes 1 and 2 (single
event or by gap).
