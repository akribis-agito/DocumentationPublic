---
keyword: InjectForceA
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 590
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
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectForceA

**Condition:**

InjectForceA is only applicable for injection at force command (InjectPoint = 3).

**Definition:**

InjectForceA is the amplitude of the force injection, in terms of internal force unit.
