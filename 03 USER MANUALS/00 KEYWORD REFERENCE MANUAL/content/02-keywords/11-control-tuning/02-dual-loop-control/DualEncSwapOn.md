---
keyword: DualEncSwapOn
availability:
  standalone: []
  central-i:
  - v5
can_code: 724
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualEncSwapOn

**Condition:**

This keyword is only used when DualLoopOn=1.

**Definition:**

DualEncSwapOn is the switch for pseudo dual-loop control. Under pseudo dual-loop control, both position and velocity loops will use the motor/auxiliary feedback, as described above.
