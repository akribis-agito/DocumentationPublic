---
keyword: InjectPosAmp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 116
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectPosAmp

**Condition:**

InjectPosAmp is only applicable for injection at position command (InjectPoint = 2).

**Definition:**

InjectPosAmp is the amplitude of the position injection, in terms of main user unit (configurable by UsrUnits).
