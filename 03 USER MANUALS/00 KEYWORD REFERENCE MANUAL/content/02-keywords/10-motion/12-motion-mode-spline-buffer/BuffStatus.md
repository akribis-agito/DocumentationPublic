---
keyword: BuffStatus
summary: Read-only array reporting the state of the spline buffer motion mode.
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

Read-only array reporting the state of the spline buffer motion mode.

## Overview

`BuffStatus` is a read-only array that reports the current state of the spline buffer motion mode, such as whether the buffer is idle or executing, the current waypoint index, and any error conditions. It is used to monitor a trajectory computed by [BuffCalc](BuffCalc.md) and repeated according to [BuffCycles](BuffCycles.md). It is not saved to flash.

> **Documentation pending:** The meaning of each individual element of the `BuffStatus` array was not available in the source reference. Verify element assignments against current firmware before relying on specific indices.

## Examples

```text
BuffStatus[1]?      ; query the first status element
```

## See also

- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
- [BuffCycles](BuffCycles.md) — number of repetitions
- [StopBuff](../04-motion-command/StopBuff.md) — stop spline buffer motion
