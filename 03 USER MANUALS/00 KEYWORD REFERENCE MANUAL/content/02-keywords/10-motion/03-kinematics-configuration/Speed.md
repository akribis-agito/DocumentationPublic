---
keyword: Speed
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 138
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Speed

**Definition:**

Speed sets the maximum velocity for point-to-point motion in user units per second. The axis accelerates up to this speed at the rate defined by Accel and decelerates to rest at the rate defined by Decel. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[Accel](Accel.md), [Decel](Decel.md), [Jerk](Jerk.md)
