---
keyword: VecJerk
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 639
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 9
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecJerk

**Definition:**

VecJerk sets the jerk limit for vector motion, controlling the rate of change of the resultant acceleration to produce a smoother S-curve velocity profile. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[VecAccel](VecAccel.md), [VecDecel](VecDecel.md), [VecSpeed](VecSpeed.md)
