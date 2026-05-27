---
keyword: DualEncRange
availability:
  standalone: []
  central-i:
  - v5
can_code: 726
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# DualEncRange

**Condition:**

This keyword is only used when DualLoopOn=1, DualEncSwapOn=1 and DualEncMode=1.

**Definition:**

DualEncRange defines lower and upper values of motor feedback (AuxPos) when the dual-loop control is active. Pseudo dual-loop is used outside of this range.

| Index | Descriptions         |
|-------|----------------------|
| 1     | Lower position range |
| 2     | Upper position range |
