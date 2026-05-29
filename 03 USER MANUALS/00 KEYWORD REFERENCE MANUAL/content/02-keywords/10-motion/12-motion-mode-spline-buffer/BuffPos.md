---
keyword: BuffPos
summary: Array of waypoint positions (user units) that define the spline buffer trajectory.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 543
attributes:
  access: rw
  scope: axis
  flash: false
  type: array
  array_size: 10001
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BuffPos

Array of waypoint positions (user units) that define the spline buffer trajectory.

## Overview

`BuffPos` stores the waypoint positions, in user units, for the spline-buffer motion profile. Each entry is one knot of the trajectory; together with the per-segment durations in [BuffTime](BuffTime.md) (one entry per waypoint, sharing the same index), it defines the shape of the move. The controller fits a spline through these waypoints and plays it back as a smooth position reference. The arrays are turned into a ready-to-run trajectory by [BuffCalc](BuffCalc.md) before motion begins. `BuffPos` is not saved to flash and can be changed at any time, but a change does not take effect until [BuffCalc](BuffCalc.md) is run again.

> **Product limit.** The usable length of `BuffPos` depends on the product (see the [section overview](00-overview.md#product-availability)): 5 entries on standalone AGD drives (effectively unusable), and 50 or 10 000 entries on Central-i AGM800 depending on the hardware variant. The frontmatter `array_size` shows the largest size.

## How it works

### Waypoints, indexing and the implicit origin

`BuffPos` is a paired array with [BuffTime](BuffTime.md): entry `[i]` is the commanded position at the time given by `BuffTime[i]`. Entries are used starting at index `[1]`; index `[0]` is not user-accessible. The list is terminated by the **first zero entry in [BuffTime](BuffTime.md)** — every waypoint before that terminator is part of the trajectory, so you do not need to clear old entries beyond the terminator.

Positions are interpreted as **relative to the position reference at the moment motion begins**. When the move starts, the controller captures the current reference as an origin and adds the buffered profile on top of it, so the first waypoint is effectively the offset from the start point rather than an absolute target. A waypoint of `0` therefore means "the start position".

Internally [BuffCalc](BuffCalc.md) prepends a hidden origin knot at *(time 0, position 0)* before `BuffPos[1]`/`BuffTime[1]`. The spline's first segment therefore runs from this buffer origin to the first user waypoint, which is why a list of *N* waypoints yields *N* interpolated segments and why `BuffPos[1]` is the position **reached at** `BuffTime[1]` rather than the start position. The buffered profile always begins at `0` (the hidden origin); during playback the controller adds the position reference captured at the moment motion begins, so a profile that starts at `0` starts from wherever the axis was. With linear interpolation, `BuffPos[1]=0` holds at the start position until `BuffTime[1]`; with a parabolic or cubic fit the curve between the origin and the first waypoint may bow away from `0` if the edge slope is non-zero.

### From waypoints to a position reference

[BuffCalc](BuffCalc.md) fits a spline (type chosen by [BuffSplineMod](BuffSplineMod.md), edges by [BuffEdgeMode](BuffEdgeMode.md)/[BuffSlopes](BuffSlopes.md)) through the waypoints and **pre-expands it into one interpolated point per servo sample**, stored internally. During motion the profiler does no curve math: each control cycle it simply reads the next pre-computed point, adds the captured origin, and feeds it to the position loop as [PosRef](../01-kinematics-status/PosRef.md). Because the whole curve is expanded ahead of time, the total number of stored samples per cycle equals the last [BuffTime](BuffTime.md) value, and that value is limited by the controller's internal capacity (see [BuffTime](BuffTime.md)).

![Five waypoints with the linear and cubic-spline curves fitted through them](spline-waypoints.svg)

For multi-axis spline moves the same time base ([BuffTime](BuffTime.md) of the primary axis) is shared by all member axes, while each member axis carries its own `BuffPos` waypoints — so all axes stay synchronized in time while tracing independent position profiles.

### The segment polynomial

Each segment between waypoint `i-1` and waypoint `i` is one polynomial in the *local sample offset* `k`, where `k` counts servo samples from the start of that segment (`k = 0` at waypoint `i-1`). [BuffCalc](BuffCalc.md) evaluates it once per sample:

$$P_i(k) = a_i + b_i\,k + c_i\,k^2 + d_i\,k^3, \qquad k = 0,1,\dots,\big(\text{BuffTime}[i]-\text{BuffTime}[i-1]\big)-1$$

The last sample of the segment, at `k = BuffTime[i] - BuffTime[i-1]`, is not evaluated here; it is the `k = 0` sample of the next segment, so adjacent segments meet exactly at each waypoint. The constant term is always the segment's start position, `a_i = BuffPos[i-1]`; the higher coefficients `b_i` (slope), `c_i` (curvature) and `d_i` are what [BuffSplineMod](BuffSplineMod.md) and [BuffEdgeMode](BuffEdgeMode.md)/[BuffSlopes](BuffSlopes.md) determine. Because the argument is the raw sample count, the [BuffTime](BuffTime.md) values are used directly as the polynomial's time axis — no rescaling. For linear interpolation `c_i = d_i = 0`; for the parabolic mode `d_i = 0`; the cubic mode uses all four coefficients.

## Examples

```text
ABuffPos[1]=0        ; first waypoint (0 = the start position)
ABuffPos[2]=10000    ; second waypoint, reached at time ABuffTime[2]
ABuffPos[3]=10000    ; third waypoint (dwell at 10000)
```

## See also

- [BuffTime](BuffTime.md) — per-segment time stamps paired with these waypoints (zero entry terminates the list)
- [BuffCalc](BuffCalc.md) — fits the spline and expands it into the interpolated reference
- [BuffSplineMod](BuffSplineMod.md) — spline interpolation mode (linear / parabolic / cubic)
- [BuffEdgeMode](BuffEdgeMode.md) — start/end boundary condition
- [PosRef](../01-kinematics-status/PosRef.md) — position reference the expanded buffer feeds during playback
