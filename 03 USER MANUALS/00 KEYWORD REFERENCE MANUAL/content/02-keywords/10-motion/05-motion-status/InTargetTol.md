---
keyword: InTargetTol
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 265
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
  - 0
  - 2147483647
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetTol

**Condition:**

It is only used when OperationMode = 2 or 3.

**Definition:**

In position or velocity control operation mode, InTargetTol is the settling window which the absolute position error (PosErr) must stay within for InTargetTime, before InTargetStat signals that target is reached (InTargetStat=4).
