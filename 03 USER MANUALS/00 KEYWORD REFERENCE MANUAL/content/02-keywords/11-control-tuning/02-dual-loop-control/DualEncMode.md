---
keyword: DualEncMode
availability:
  standalone: []
  central-i:
  - v5
can_code: 725
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualEncMode

**Condition:**

This keyword is only used when DualLoopOn=1 and DualEncSwapOn=1.

**Definition:**

DualEncMode is used to activate/deactivate range-limited dual-loop control.

| DualEncMode | Descriptions |
|----|----|
| 0 | Pseudo dual-loop control is always used regardless of position |
| 1 | Dual-loop control is only used for a defined position range. Pseudo dual-loop control is used outside of this range. |
