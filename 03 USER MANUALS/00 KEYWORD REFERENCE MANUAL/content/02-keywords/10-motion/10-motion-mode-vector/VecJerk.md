---
keyword: VecJerk
summary: Jerk limit (0-9) for vector motion, smoothing the resultant velocity into an S-curve.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 639
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 9
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecJerk

Jerk limit (0-9) for vector motion, smoothing the resultant velocity into an S-curve.

## Overview

`VecJerk` is a legacy jerk-limit selector (`0`-`9`) for vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16). On current firmware it does **not** shape the vector path: S-curve smoothing along the path is enabled by [VecJerkMode](VecJerkMode.md) and tuned by [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md). `VecJerk` is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion.

## How it works

`VecJerk` is a legacy `0`-`9` selector and has **no effect on the vector path** on current firmware. The vector path profile is selected and shaped by other keywords:

- The vector path is trapezoidal by default — the path velocity ramps linearly up at [VecAccel](VecAccel.md), cruises at [VecSpeed](VecSpeed.md), and ramps linearly down at [VecDecel](VecDecel.md), so acceleration changes instantly at the corners.
- S-curve shaping along the path is enabled by [VecJerkMode](VecJerkMode.md) = 1 and tuned by [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md), which round the corners of the trapezoid so acceleration itself ramps in and out.

`VecJerk` is retained for compatibility; use [VecJerkMode](VecJerkMode.md) with [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) to shape the vector path. Verify behavior against your firmware before relying on `VecJerk` for vector motion.

## Examples

```text
AVecJerk=0           ; no jerk limiting (trapezoidal profile, default)
AVecJerk=9           ; maximum S-curve smoothing
```

## See also

- [VecJerkMode](VecJerkMode.md) — enables S-curve shaping of the vector path
- [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md) — tune the S-curve on the acceleration / deceleration ramps
- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
