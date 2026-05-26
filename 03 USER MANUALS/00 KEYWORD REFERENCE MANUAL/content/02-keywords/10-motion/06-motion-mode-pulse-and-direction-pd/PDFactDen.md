---
keyword: PDFactDen
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 119
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
  - 16777215
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDFactDen

**Definition:**

PDFactDen is the denominator of the scaling factor applied onto the number of pulses detected, before the sign correction and accumulation on internal counter (PDPos).
