---
keyword: VecDecel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 637
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
# VecDecel

**Definition:**

VecDecel sets the vector deceleration rate for coordinated multi-axis motion in user units per second squared. It defines how quickly the resultant velocity ramps down from VecSpeed to rest. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[VecAccel](VecAccel.md), [VecSpeed](VecSpeed.md), [VecEmrgDec](VecEmrgDec.md)
