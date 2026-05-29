---
keyword: BuffCalc
summary: Command that pre-computes the spline coefficients from the buffer waypoints.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 547
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffCalc

Command that pre-computes the spline coefficients from the buffer waypoints.

## Overview

`BuffCalc` fits the spline through the waypoints in [BuffPos](BuffPos.md) / [BuffTime](BuffTime.md) and expands it into a ready-to-play interpolated trajectory. It must be issued on the **primary axis**, after the waypoint arrays and shape settings are loaded and before a `Begin` is issued in spline-buffer mode, so the controller has a prepared trajectory to execute. It cannot be issued while the axis is in motion.

## How it works

### What the command does

For every member axis of the group `BuffCalc`:

1. **Validates [BuffTime](BuffTime.md)** — first entry non-zero, values strictly increasing, a zero terminator present, and the last time stamp within the controller's interpolation capacity.
2. **Fits the curve** selected by [BuffSplineMod](BuffSplineMod.md) (linear / parabolic / cubic) using the edge condition from [BuffEdgeMode](BuffEdgeMode.md) and, when that mode calls for it, the slope from [BuffSlopes](BuffSlopes.md). The primary axis's shape settings and time base are applied to all members; each member uses its own positions.
3. **Expands the curve** into one interpolated position per servo sample, from the start to the last time stamp, and stores it internally for playback.
4. **Records group facts** into [BuffStatus](BuffStatus.md): the primary axis, the member-axis set, the per-axis peak speed and acceleration of the computed profile, and the index of the last point. It then clears the "needs recompute" flag for each member.

### Why it must be re-run after changes

The controller tracks whether any spline parameter has been modified since the last `BuffCalc`. Writing [BuffPos](BuffPos.md), [BuffTime](BuffTime.md), [BuffSplineMod](BuffSplineMod.md), [BuffEdgeMode](BuffEdgeMode.md) or [BuffSlopes](BuffSlopes.md) sets this flag. If `Begin` is issued while the flag is set on any member, the command is **rejected** so a stale trajectory is never run — issue `BuffCalc` again to clear it.

### Conditions that make BuffCalc fail

`BuffCalc` returns an error (and computes nothing) if:

| Condition | Cause |
|---|---|
| First time stamp is zero | `BuffTime[1]` = 0. |
| Time stamps not strictly increasing | A `BuffTime` entry is equal to or less than the previous one. |
| No terminating zero | The `BuffTime` list never reaches a zero entry. |
| Trajectory too long | The last time stamp exceeds the internal interpolation capacity. |
| Primary not a member | The axis issuing `BuffCalc` is not included in its own group's member set. |
| A member is already running a spline-buffer move | Recomputation is not allowed while a member is in spline-buffer motion. |

## Examples

```text
ABuffPos[1]=0
ABuffPos[2]=10000
ABuffTime[1]=100
ABuffTime[2]=300
ABuffTime[3]=0       ; terminator
ABuffCalc            ; fit and expand the trajectory (run before Begin)
```

## See also

- [BuffPos](BuffPos.md) — waypoint positions consumed by the fit
- [BuffTime](BuffTime.md) — waypoint time stamps (validated here)
- [BuffSplineMod](BuffSplineMod.md) — curve type applied during the fit
- [BuffEdgeMode](BuffEdgeMode.md) / [BuffSlopes](BuffSlopes.md) — edge conditions applied during the fit
- [BuffStatus](BuffStatus.md) — group facts and peak speed/acceleration written by this command
