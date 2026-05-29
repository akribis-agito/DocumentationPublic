---
keyword: VecJerkMode
summary: 'Selects how jerk limiting is applied to vector motion: 0 trapezoidal, 1 jerk-limited S-curve.'
availability:
  standalone: []
  central-i:
  - v5
can_code: 755
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecJerkMode

Selects how jerk limiting is applied to vector motion: 0 trapezoidal, 1 jerk-limited S-curve.

> Available from v5 (central-i) only.

## Overview

`VecJerkMode` chooses which path-velocity profiler a vector move ([MotionMode](../02-motion-configuration/MotionMode.md) = 16) uses. With the mode off, the path velocity follows a trapezoidal profile in which acceleration can change instantly at the corners. With the mode on, the path velocity follows a jerk-limited S-curve whose acceleration is ramped in and out at the rates given by [VecJerkInAcc](VecJerkInAcc.md) and [VecJerkInDec](VecJerkInDec.md), reducing mechanical shock at the start and end of the ramps.

It is an axis-related parameter saved to flash. Because the controller reads it when the move starts to select the profiler, it cannot be changed while the axis is in motion.

This is the v5 jerk-control scheme for vector motion, expressed as an explicit jerk limit in user units. It is separate from the legacy [VecJerk](VecJerk.md) (0-9) smoothing selector.

## How it works

`VecJerkMode` is read at `Begin` and applies to the single path velocity that drives every member axis (see [VecSpeed](VecSpeed.md)):

| Value | Path profile |
|----|----|
| 0 | Trapezoidal (default). The path velocity ramps linearly up at [VecAccel](VecAccel.md), cruises at [VecSpeed](VecSpeed.md), and ramps linearly down at [VecDecel](VecDecel.md). Acceleration changes abruptly at the corners. [VecJerkInAcc](VecJerkInAcc.md) and [VecJerkInDec](VecJerkInDec.md) have no effect. |
| 1 | Jerk-limited S-curve. The path velocity is run through a profiler that limits the rate of change of acceleration, so the corners of the trapezoid are rounded. The acceleration is ramped up at the jerk limit [VecJerkInAcc](VecJerkInAcc.md) and ramped down at [VecJerkInDec](VecJerkInDec.md), while [VecAccel](VecAccel.md) and [VecDecel](VecDecel.md) still cap the acceleration and deceleration magnitudes. |

Because the profile shapes the **resultant** path velocity, jerk limiting benefits all member axes along the coordinated path at once. With the mode on, the move is considered finished when the S-curve profiler reaches its completed segment; with the mode off, it finishes when the path reference reaches the target with a low enough path velocity.

The mode is fixed for the duration of a move. To switch profilers, change `VecJerkMode` before issuing `Begin`.

## Examples

```text
AVecJerkMode=0       ; trapezoidal path profile (default)
AVecJerkMode=1       ; jerk-limited S-curve path profile
AVecJerkMode         ; read the current value
```

## See also

- [VecJerkInAcc](VecJerkInAcc.md) — jerk limit during the acceleration phase
- [VecJerkInDec](VecJerkInDec.md) — jerk limit during the deceleration phase
- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecJerk](VecJerk.md) — legacy 0-9 jerk-smoothing selector
