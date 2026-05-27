---
keyword: BuffCycles
summary: Number of times the spline buffer trajectory is repeated.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 548
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffCycles

Number of times the spline buffer trajectory is repeated.

## Overview

`BuffCycles` sets how many times the spline buffer trajectory is repeated when executed. The valid range is 1 to 2147483647, with a default of 1 (a single pass). A running spline buffer motion can be ended early with the `StopBuff` command. It is saved to flash and can be changed at any time.

## Examples

```text
BuffCycles=1        ; run the trajectory once (default)
BuffCycles=10       ; repeat the trajectory ten times
```

## See also

- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
- [BuffPos](BuffPos.md) — waypoint positions
- [BuffStatus](BuffStatus.md) — spline buffer status
- [StopBuff](../04-motion-command/StopBuff.md) — stop spline buffer motion
