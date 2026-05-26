---
keyword: InjectCurrAmp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 114
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 64000
  default: 2133
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectCurrAmp

**Condition:**

InjectCurrAmp is only applicable for injection at current command (InjectPoint = 0).

**Definition:**

InjectCurrAmp is the amplitude of the current injection, in terms of mA.
