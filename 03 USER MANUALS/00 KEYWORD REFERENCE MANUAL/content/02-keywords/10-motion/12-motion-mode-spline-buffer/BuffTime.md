---
keyword: BuffTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 542
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 10001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffTime

**Definition:**

BuffTime is an array that stores the time duration (in servo samples) for each waypoint segment of the spline buffer. Together with BuffPos it defines the spline trajectory: the axis follows the position profile in BuffPos, spending BuffTime samples on each segment. It is an axis-related array, not saved to flash, and can be changed at any time.

**See also:**

[BuffPos](BuffPos.md), [BuffCalc](BuffCalc.md), [BuffStatus](BuffStatus.md)
