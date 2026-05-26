---
keyword: BuffStatus
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 549
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 9
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
# BuffStatus

**Definition:**

BuffStatus is a read-only array that reports the current state of the spline buffer motion mode. The elements indicate whether the buffer is idle, executing, the current waypoint index, and any error conditions. It is an axis-related, read-only array that is not saved to flash.

**See also:**

[BuffCalc](BuffCalc.md), [BuffCycles](BuffCycles.md), [StopBuff](../04-motion-command/StopBuff.md)
