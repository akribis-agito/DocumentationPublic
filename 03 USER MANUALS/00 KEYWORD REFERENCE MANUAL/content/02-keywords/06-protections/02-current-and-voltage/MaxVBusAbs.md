---
keyword: MaxVBusAbs
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 94
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
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxVBusAbs

**Definition:**

MaxVBusAbs defines maximum allowable absolute value of bus voltage. If absolute bus voltage value exceeds MaxVBusAbs, axis will be instantaneously disabled and an error is thrown to ConFlt.
