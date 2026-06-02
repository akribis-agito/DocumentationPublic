---
keyword: VecAccel
summary: Vector acceleration rate (user units/s^2) ramping the resultant velocity up to VecSpeed.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 636
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
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range:
    - 100.0
    - 686700000000.0
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# VecAccel

Vector acceleration rate (user units/s^2) ramping the resultant velocity up to VecSpeed.

## Overview

`VecAccel` sets the acceleration rate for coordinated multi-axis vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), in user units per second squared. It defines how quickly the resultant (vector) velocity ramps up toward [VecSpeed](VecSpeed.md), applying to the path as a whole rather than to any single axis. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

`VecAccel` governs the ramp-up; [VecDecel](VecDecel.md) governs the controlled ramp-down. By default the path profile is trapezoidal, so the acceleration steps instantly to `VecAccel` at the start of the ramp; S-curve smoothing of the path is enabled separately by [VecJerkMode](VecJerkMode.md) = 1 and tuned by [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md).

## How it works

A vector move runs one velocity profile along the geometric path (see [VecSpeed](VecSpeed.md)); `VecAccel` is the rate at which that single path velocity is allowed to rise. With the default trapezoidal path profile the profiler increments the path velocity by `VecAccel × Ts` each control cycle (where `Ts` is the control-cycle time) until it reaches [VecSpeed](VecSpeed.md):

$$
v_k = v_{k-1} + \text{VecAccel} \cdot T_s ,\qquad v_k \le \text{VecSpeed}
$$

The deceleration side is handled separately: each cycle the profiler also computes, from the remaining path distance to [VecAbsTrgt](VecAbsTrgt.md), the speed from which it could still brake to rest in time using [VecDecel](VecDecel.md), and clamps the path velocity to it. `VecAccel` therefore sets the leading slope of the trapezoid and `VecDecel` the trailing slope. When S-curve smoothing is enabled ([VecJerkMode](VecJerkMode.md) = 1, central-i v5), `VecAccel` is passed instead as the acceleration constraint to the jerk-limited path profiler, with the jerk limits taken from [VecJerkInAcc](VecJerkInAcc.md) / [VecJerkInDec](VecJerkInDec.md).

Because the ramp shapes the **resultant** path velocity, the apparent acceleration seen on any one member axis is `VecAccel` scaled by that axis's share of the path (its direction cosine for a linear move). The value is re-read each cycle, so a change mid-move takes effect on the next cycle.

## Examples

```text
AVecAccel=100000     ; vector acceleration (user units/s^2, default)
AVecAccel           ; read the current value
```

## See also

- [VecDecel](VecDecel.md) — vector deceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
- [VecJerkMode](VecJerkMode.md) — enables S-curve smoothing of the vector path
