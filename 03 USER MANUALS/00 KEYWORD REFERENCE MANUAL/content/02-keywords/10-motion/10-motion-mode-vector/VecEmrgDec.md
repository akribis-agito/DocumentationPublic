---
keyword: VecEmrgDec
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 638
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
# VecEmrgDec

**Definition:**

VecEmrgDec sets the emergency deceleration rate applied to all axes participating in vector motion when a stop or fault is triggered. It is typically set higher than VecDecel to halt the vector move as quickly as possible. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[VecDecel](VecDecel.md), [StopVec](StopVec.md)
