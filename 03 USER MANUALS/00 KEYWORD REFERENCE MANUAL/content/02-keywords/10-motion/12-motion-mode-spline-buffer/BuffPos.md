---
keyword: BuffPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 543
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 10001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffPos

**Definition:**

BuffPos is an array that stores the waypoint positions in user units for the spline buffer motion profile. The controller uses these positions together with the time values in BuffTime to compute and execute a smooth spline trajectory. It is an axis-related array, not saved to flash, and can be changed at any time.

**See also:**

[BuffTime](BuffTime.md), [BuffCalc](BuffCalc.md), [BuffSplineMod](BuffSplineMod.md)
