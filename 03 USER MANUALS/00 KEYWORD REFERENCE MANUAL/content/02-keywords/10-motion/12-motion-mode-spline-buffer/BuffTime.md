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

`BuffTime` stores the **time stamp of each waypoint**, expressed as a count of servo (control) samples measured from the start of the trajectory. Entry `[i]` is the time at which the matching position waypoint [BuffPos](BuffPos.md)`[i]` is reached, so the duration of a segment is the difference between consecutive entries. Together with [BuffPos](BuffPos.md) it defines the spline trajectory. The arrays are expanded into the interpolated reference by [BuffCalc](BuffCalc.md). `BuffTime` is not saved to flash and can be changed at any time, but the change only takes effect after [BuffCalc](BuffCalc.md) is run again.

## How it works

### Cumulative time stamps, not per-segment durations

Although `BuffTime` is often described as "time per segment", the values are **cumulative time stamps**. Index `[1]` is the time of the first waypoint, `[2]` the time of the second, and so on, all measured in servo samples from `t = 0`. The controller spends `BuffTime[i] − BuffTime[i-1]` samples interpolating from waypoint `i-1` to waypoint `i`. One servo sample equals one control cycle, so 100 samples is 100 control periods of motion.

At a 16 384 Hz control rate, `BuffTime[1] = 1638` corresponds to 100 ms and `BuffTime[2] = 4915` to 300 ms — so the first segment lasts about 100 ms and the second about 200 ms. The whole pre-expanded trajectory holds `BuffTime[last]` interpolated points, which is also reported as `BuffStatus[6]`.

### Validation performed by BuffCalc

When [BuffCalc](BuffCalc.md) runs it checks the `BuffTime` array and rejects the computation (returning an error) unless all of the following hold:

| Condition | Requirement |
|---|---|
| First entry | `BuffTime[1]` must be non-zero. |
| Ordering | Values must be **strictly increasing** (each entry greater than the previous); equal or decreasing values are rejected. |
| Terminator | The list must end with a **zero entry**: the first zero marks the end of the trajectory, and the last non-zero entry before it is the final waypoint. |
| Length | The last (largest) time stamp must not exceed the controller's internal interpolation-buffer capacity, because [BuffCalc](BuffCalc.md) expands one point per sample up to that time. |

Because the expanded trajectory holds one interpolated sample for every servo cycle between `t = 0` and the last time stamp, the last `BuffTime` value sets how much internal storage the trajectory consumes.

### Shared time base across axes

In a multi-axis spline move, `BuffTime` of the **primary axis** provides the single time base used for every member axis. Each member supplies its own [BuffPos](BuffPos.md) waypoints, but they all advance through the same time stamps, keeping the axes synchronized.

## Examples

```text
ABuffTime[1]=100     ; first waypoint reached at sample 100
ABuffTime[2]=300     ; second waypoint at sample 300 (segment lasts 200 samples)
ABuffTime[3]=600     ; third waypoint at sample 600
ABuffTime[4]=0       ; zero terminates the list (3 waypoints used)
```

## See also

- [BuffPos](BuffPos.md) — waypoint positions paired with these time stamps
- [BuffCalc](BuffCalc.md) — validates these time stamps and expands the trajectory
- [BuffStatus](BuffStatus.md) — reports the last time stamp and the live playback index
- [BuffCycles](BuffCycles.md) — number of times the time base is replayed
