---
keyword: VecSpeed
summary: Maximum vector (resultant) speed in user units/s for coordinated multi-axis motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 635
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# VecSpeed

Maximum vector (resultant) speed in user units/s for coordinated multi-axis motion.

## Overview

`VecSpeed` sets the maximum vector (resultant) speed for coordinated multi-axis vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), in user units per second. The individual axis velocities are scaled so that the vector magnitude does not exceed this value, which is what keeps a multi-axis path moving at a controlled feed rate. The ramps to and from this speed are governed by [VecAccel](VecAccel.md) and [VecDecel](VecDecel.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

A vector move runs a single velocity profile **along the path** rather than per axis. Each control cycle the controller advances one scalar path velocity and adds it to the path position [VecPosRef](VecPosRef.md); `VecSpeed` is the cruise ceiling of that path velocity (always treated as a positive magnitude — direction comes from the geometry, not from the sign).

The same profiler logic used for point-to-point motion is applied to the path scalar:

- In the trapezoidal case (jerk off, [VecJerk](VecJerk.md) = 0) the path velocity is incremented by `VecAccel × Ts` each cycle until it reaches `VecSpeed`, held there, and then forced down by a deceleration-distance lookahead computed from the remaining path distance and `VecDecel`, producing a trapezoidal (or, on a short path, triangular) profile.
- With jerk smoothing the same `VecSpeed` is passed as the peak path speed to the S-curve profiler.

Because the profile is generated for the resultant path and then split across the member axes by the geometry ([VecType](VecType.md)), no single member axis necessarily moves at `VecSpeed` — only the geometric resultant does. For example, a linear vector move with `3000` travel on one axis and `4000` travel on a second has a path length of `5000`; with `VecSpeed = 1000` user units/s the resultant feed rate cruises at 1000 user units/s, while the two member axes individually cruise at `1000 × 3/5 = 600` and `1000 × 4/5 = 800` user units/s. The controller re-reads `VecSpeed` every cycle, so raising or lowering it mid-move re-targets the path velocity on the next cycle. [VecPause](VecPause.md) temporarily forces the path-velocity target to 0; [StopVec](StopVec.md) does the same but ends the move.

The reported path velocity is [VecdPosRef](VecdPosRef.md); the cruise value `VecSpeed` is the ceiling it ramps toward.

## Examples

```text
AVecSpeed=10000      ; maximum resultant speed (user units/s, default)
AVecSpeed           ; read the current value
```

## See also

- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecJerk](VecJerk.md) — jerk limit for S-curve smoothing
- [VecdPosRef](VecdPosRef.md) — reported path velocity (ramps toward `VecSpeed`)
- [VecPosRef](VecPosRef.md) — path position the profile advances
