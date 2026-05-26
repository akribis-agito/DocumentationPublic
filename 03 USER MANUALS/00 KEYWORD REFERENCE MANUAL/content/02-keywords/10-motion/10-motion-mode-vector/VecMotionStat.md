---
keyword: VecMotionStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 641
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecMotionStat

**Definition:**

VecMotionStat is a read-only parameter that reports the current status of the vector motion mode for the axis. The bit-field indicates whether the axis is actively executing a vector move, waiting for synchronisation, or idle. It is an axis-related status variable that is not saved to flash.

**See also:**

[StopVec](StopVec.md), [VecSpeed](VecSpeed.md)
