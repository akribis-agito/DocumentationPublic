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

### Walk-through: define waypoints and play one cubic-spline cycle

Load four waypoints into [BuffPos](BuffPos.md) and [BuffTime](BuffTime.md) (with a zero terminator), fit a cubic spline, then run one cycle. Axis A is assumed to be the primary axis of a single-member group and is motor-on but not in motion.

```text
; --- 1) Load the waypoint positions (one entry per knot) ---
ABuffPos[1]=0
ABuffPos[2]=5000
ABuffPos[3]=8000
ABuffPos[4]=10000

; --- 2) Load the matching time stamps (strictly increasing, zero-terminated) ---
ABuffTime[1]=200              ; servo-sample index of waypoint 1
ABuffTime[2]=600              ; of waypoint 2
ABuffTime[3]=900              ; of waypoint 3
ABuffTime[4]=1200             ; of waypoint 4 (== samples per cycle, BuffStatus[6])
ABuffTime[5]=0                ; terminator -- required

; --- 3) Choose the curve shape and how many times the cycle repeats ---
ABuffSplineMod=3              ; 1 = linear, 2 = parabolic, 3 = cubic (default)
ABuffEdgeMode=0               ; start/end boundary condition (see BuffEdgeMode)
ABuffCycles=1                 ; play the cycle once

; --- 4) Pre-compute the trajectory on the primary axis ---
ABuffCalc=0                   ; rejected if BuffTime is not validly populated

; --- 5) Arm spline-buffer motion ---
AMotionMode=18                ; 18 = spline buffer
ABegin                        ; controller streams the stored points to PosRef

; --- 6) Observe the playback ---
ABuffStatus[4]                ; cycle currently playing (1..BuffCycles)
ABuffStatus[5]                ; in-cycle sample index (1..BuffStatus[6])
ABuffStatus[6]                ; samples per cycle (= last BuffTime value)
```

Changes to `BuffPos`, `BuffTime`, `BuffSplineMod`, `BuffEdgeMode` or `BuffSlopes` mark the trajectory "stale": the next `Begin` is rejected until `BuffCalc` is re-run. End the move at the next cycle boundary with [StopBuff](../04-motion-command/StopBuff.md).

## See also

- [BuffEdgeMode](BuffEdgeMode.md) — start/end boundary condition applied to the parabolic/cubic fit
- [BuffSlopes](BuffSlopes.md) — edge slope used when the boundary condition calls for it
- [BuffPos](BuffPos.md) — waypoint positions
- [BuffTime](BuffTime.md) — waypoint time stamps
- [BuffCalc](BuffCalc.md) — fits the selected curve and expands the trajectory
