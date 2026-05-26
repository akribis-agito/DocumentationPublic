---
keyword: Jerk
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 139
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
# Jerk

**Definition:**

Jerk sets the rate of change of acceleration (third derivative of position) for point-to-point motion. A finite jerk value produces an S-curve profile that reduces mechanical vibration at the start and end of moves. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[Accel](Accel.md), [Decel](Decel.md), [JerkInAcc](JerkInAcc.md), [JerkInDec](JerkInDec.md), [JerkMode](JerkMode.md)
