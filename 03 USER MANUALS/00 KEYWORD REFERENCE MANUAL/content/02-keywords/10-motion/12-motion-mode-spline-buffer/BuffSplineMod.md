---
keyword: BuffSplineMod
summary: Selects the spline interpolation mode used when executing the buffer profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`BuffSplineMod` selects the type of curve fitted through the waypoints in [BuffPos](BuffPos.md) and [BuffTime](BuffTime.md) when the buffer profile is computed. The range is 1 to 3 with a default of 3 (cubic). The mode of the **primary axis** is applied to all member axes when [BuffCalc](BuffCalc.md) runs. `BuffSplineMod` is saved to flash and can be changed at any time, but the change only takes effect after [BuffCalc](BuffCalc.md) is run again.

## How it works

Each value selects a different interpolation order between waypoints. Higher orders produce smoother motion (more continuous derivatives) at the cost of more overshoot freedom between points; lower orders track the waypoints more literally.

| Value | Meaning |
|---|---|
| 1 | Linear interpolation. Straight-line segments between waypoints. Position is continuous, but velocity changes abruptly at every waypoint (the curve has a corner at each knot). |
| 2 | Parabolic spline. Each segment is a second-order (quadratic) curve. Position and velocity are continuous through the waypoints, giving smooth speed transitions; acceleration may step at the knots. |
| 3 | Cubic spline (default). Each segment is a third-order curve. Position, velocity and acceleration are continuous through the interior waypoints, producing the smoothest motion of the three modes. |

The boundary behaviour of the parabolic and cubic modes — what is enforced at the very first and very last waypoint — is set by [BuffEdgeMode](BuffEdgeMode.md), optionally using the edge slopes in [BuffSlopes](BuffSlopes.md). Linear interpolation ignores the edge settings because it has no free end derivatives to constrain.

After fitting, [BuffCalc](BuffCalc.md) expands the chosen curve into one interpolated point per servo sample, so the spline type affects only the shape of the stored profile, not how it is played back.

## Examples

```text
ABuffSplineMod=1     ; straight-line segments between waypoints
ABuffSplineMod=2     ; parabolic (continuous velocity)
ABuffSplineMod=3     ; cubic spline (default, smoothest)
```

## See also

- [BuffEdgeMode](BuffEdgeMode.md) — start/end boundary condition applied to the parabolic/cubic fit
- [BuffSlopes](BuffSlopes.md) — edge slope used when the boundary condition calls for it
- [BuffPos](BuffPos.md) — waypoint positions
- [BuffTime](BuffTime.md) — waypoint time stamps
- [BuffCalc](BuffCalc.md) — fits the selected curve and expands the trajectory
