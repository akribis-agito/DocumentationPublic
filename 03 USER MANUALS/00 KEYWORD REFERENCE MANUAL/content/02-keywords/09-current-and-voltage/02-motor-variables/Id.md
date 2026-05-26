---
keyword: Id
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 11
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Id

**Condition:**

Id is only applicable for three-phase motor (MotorType = 3 or 4). Otherwise, Id is 0.

**Definition:**

Id is the feedback current after Park transform in the direct axis, in milliamperes.
