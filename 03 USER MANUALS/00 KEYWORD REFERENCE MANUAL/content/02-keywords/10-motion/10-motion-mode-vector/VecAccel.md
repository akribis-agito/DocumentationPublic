---
keyword: VecAccel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 636
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecAccel

**Definition:**

VecAccel sets the vector acceleration rate for coordinated multi-axis motion in user units per second squared. It defines how quickly the resultant velocity ramps up to VecSpeed. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[VecDecel](VecDecel.md), [VecSpeed](VecSpeed.md), [VecJerk](VecJerk.md)
