---
keyword: InjectTimeOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 125
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 65536
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectTimeOn

**Condition:**

InjectTimeOn is only applicable for pulse injection (InjectType = 5).

**Definition:**

InjectTimeOn defines the pulse duration, in terms of milliseconds.
