---
keyword: BuffSplineMod
summary: Selects the spline interpolation mode used when executing the buffer profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 544
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
  - 3
  default: 3
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffSplineMod

Selects the spline interpolation mode used when executing the buffer profile.

## Overview

`BuffSplineMod` selects the spline interpolation mode applied to the waypoints in [BuffPos](BuffPos.md) and [BuffTime](BuffTime.md) when the buffer profile is executed. Different values (range 1 to 3, default 3) choose the type of curve used to interpolate between waypoints, affecting the shape of the motion. The chosen mode is applied when [BuffCalc](BuffCalc.md) computes the coefficients. It is saved to flash and can be changed at any time.

> **Documentation pending:** The specific spline type selected by each value (1–3) was not available in the source reference. Verify the mode codes against current firmware before relying on specific values.

## Examples

```text
ABuffSplineMod=3     ; default spline interpolation mode
```

## See also

- [BuffPos](BuffPos.md) — waypoint positions
- [BuffTime](BuffTime.md) — per-segment durations
- [BuffCalc](BuffCalc.md) — pre-compute the spline coefficients
