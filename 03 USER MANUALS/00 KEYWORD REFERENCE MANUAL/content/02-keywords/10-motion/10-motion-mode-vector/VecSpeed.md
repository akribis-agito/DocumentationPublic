---
keyword: VecSpeed
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 635
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
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecSpeed

**Definition:**

VecSpeed sets the maximum vector (resultant) speed for coordinated multi-axis motion in user units per second. The individual axis velocities are scaled so that the vector magnitude does not exceed this value. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[VecAccel](VecAccel.md), [VecDecel](VecDecel.md), [VecJerk](VecJerk.md)
