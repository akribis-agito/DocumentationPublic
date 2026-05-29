---
keyword: VecJerkInAcc
summary: Jerk limit (user units) for the acceleration phase of a jerk-limited vector move.
availability:
  standalone: []
  central-i:
  - v5
can_code: 756
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 10000.0
  - 1.0e+20
  default: 100000000.0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecJerkInAcc

Jerk limit (user units) for the acceleration phase of a jerk-limited vector move.

> Available from v5 (central-i) only.

## Overview

`VecJerkInAcc` sets the jerk limit used while the resultant velocity is **rising** during a jerk-limited vector move ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). Jerk is the rate of change of acceleration, so this value bounds how quickly the path acceleration is allowed to build up and bleed off as the move ramps up toward [VecSpeed](VecSpeed.md). A lower value rounds the leading corners of the velocity profile more gently (less shock, slightly longer move); a higher value approaches a sharp trapezoidal corner.

It is an axis-related parameter saved to flash, given in user units, and can be changed at any time, including during motion. It applies to the path as a whole rather than to any single axis.

`VecJerkInAcc` is only active when [VecJerkMode](VecJerkMode.md) = 1; with the mode off the vector move uses a trapezoidal profile and this value is ignored. The companion [VecJerkInDec](VecJerkInDec.md) sets the jerk limit for the deceleration phase.

## How it works

When [VecJerkMode](VecJerkMode.md) = 1, the path velocity is produced by an S-curve profiler that takes the acceleration limit [VecAccel](VecAccel.md), the deceleration limit [VecDecel](VecDecel.md), and two jerk limits — `VecJerkInAcc` for the acceleration phase and [VecJerkInDec](VecJerkInDec.md) for the deceleration phase. `VecJerkInAcc` governs the S-curve segments where the path acceleration ramps from zero up to [VecAccel](VecAccel.md) and back down to zero as the velocity climbs to [VecSpeed](VecSpeed.md). Because it shapes the **resultant** path velocity, the smoothing is shared by every member axis along the coordinated path.

The value is read at `Begin` to initialise the profiler and is also re-applied each control cycle, so a change made mid-move takes effect on the following cycle.

There is an internal upper bound: if the requested jerk is so high that the acceleration would reach its limit within a single control cycle, the controller clamps the effective jerk to the largest value that still fits one cycle. Setting a very large `VecJerkInAcc` therefore makes the acceleration ramp essentially immediate (close to a trapezoidal corner) rather than producing an out-of-range result.

The usable range and default are given in the frontmatter; the minimum is a small positive value, so jerk limiting in the acceleration phase is always finite when the mode is on.

## Examples

```text
AVecJerkInAcc=100000000   ; jerk limit for the acceleration phase (user units, default)
AVecJerkInAcc=20000000    ; gentler acceleration corners
AVecJerkInAcc             ; read the current value
```

## See also

- [VecJerkMode](VecJerkMode.md) — selects whether jerk limiting is applied
- [VecJerkInDec](VecJerkInDec.md) — jerk limit during the deceleration phase
- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
