---
keyword: VecJerkInDec
summary: "Jerk limit (user units) for the deceleration phase of a jerk-limited vector move."
availability:
  standalone: []
  central-i:
  - v5
can_code: 757
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
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecJerkInDec

Jerk limit (user units) for the deceleration phase of a jerk-limited vector move.

> Available from v5 (central-i) only.

## Overview

`VecJerkInDec` sets the jerk limit used while the resultant velocity is **falling** during a jerk-limited vector move ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). Jerk is the rate of change of acceleration, so this value bounds how quickly the path deceleration is allowed to build up and bleed off as the move ramps down to rest. A lower value rounds the trailing corners of the velocity profile more gently (less shock, slightly longer stop); a higher value approaches a sharp trapezoidal corner.

It is an axis-related parameter saved to flash, given in user units, and can be changed at any time, including during motion. It applies to the path as a whole rather than to any single axis.

`VecJerkInDec` is only active when [VecJerkMode](VecJerkMode.md) = 1; with the mode off the vector move uses a trapezoidal profile and this value is ignored. The companion [VecJerkInAcc](VecJerkInAcc.md) sets the jerk limit for the acceleration phase.

## How it works

When [VecJerkMode](VecJerkMode.md) = 1, the path velocity is produced by an S-curve profiler that takes the acceleration limit [VecAccel](VecAccel.md), the deceleration limit [VecDecel](VecDecel.md), and two jerk limits — [VecJerkInAcc](VecJerkInAcc.md) for the acceleration phase and `VecJerkInDec` for the deceleration phase. `VecJerkInDec` governs the S-curve segments where the path acceleration ramps from zero down to the braking magnitude [VecDecel](VecDecel.md) and back to zero as the velocity falls to rest at the end of the path. Because it shapes the **resultant** path velocity, the smoothing is shared by every member axis along the coordinated path.

The value is read at `Begin` to initialise the profiler and is also re-applied each control cycle, so a change made mid-move takes effect on the following cycle.

There is an internal upper bound: if the requested jerk is so high that the deceleration would reach its limit within a single control cycle, the controller clamps the effective jerk to the largest value that still fits one cycle. Setting a very large `VecJerkInDec` therefore makes the deceleration ramp essentially immediate (close to a trapezoidal corner) rather than producing an out-of-range result.

The usable range and default are given in the frontmatter; the minimum is a small positive value, so jerk limiting in the deceleration phase is always finite when the mode is on.

## Examples

```text
AVecJerkInDec=100000000   ; jerk limit for the deceleration phase (user units, default)
AVecJerkInDec=20000000    ; gentler deceleration corners
AVecJerkInDec             ; read the current value
```

## See also

- [VecJerkMode](VecJerkMode.md) — selects whether jerk limiting is applied
- [VecJerkInAcc](VecJerkInAcc.md) — jerk limit during the acceleration phase
- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
