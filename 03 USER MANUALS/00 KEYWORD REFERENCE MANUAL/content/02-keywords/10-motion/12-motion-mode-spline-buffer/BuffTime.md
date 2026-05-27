---
keyword: BuffTime
summary: Array of per-segment durations (servo samples) for the spline buffer trajectory.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Array of per-segment durations (servo samples) for the spline buffer trajectory.

## Overview

`BuffTime` stores the time duration, in servo samples, of each waypoint segment of the spline buffer. Together with the waypoint positions in [BuffPos](BuffPos.md) it defines the spline trajectory: the axis follows the position profile, spending the corresponding number of `BuffTime` samples on each segment. The arrays are turned into spline coefficients by [BuffCalc](BuffCalc.md). It is not saved to flash and can be changed at any time.

## Examples

```text
ABuffTime[1]=100     ; spend 100 servo samples on the first segment
ABuffTime[2]=200     ; spend 200 servo samples on the second segment
```

## See also

- [BuffPos](BuffPos.md) — waypoint positions paired with these durations
- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
- [BuffStatus](BuffStatus.md) — spline buffer status
