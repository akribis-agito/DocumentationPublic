---
keyword: VecDecel
summary: Vector deceleration rate (user units/s^2) ramping the resultant velocity down to rest.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 637
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
    range: null
    default: null
---
# VecDecel

Vector deceleration rate (user units/s^2) ramping the resultant velocity down to rest.

## Overview

`VecDecel` sets the deceleration rate for coordinated multi-axis vector motion ([MotionMode](../02-motion-configuration/MotionMode.md) = 16), in user units per second squared. It defines how quickly the resultant (vector) velocity ramps down from [VecSpeed](VecSpeed.md) to rest at the end of a controlled stop, applying to the path as a whole. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

`VecDecel` is the controlled (normal) deceleration; [VecEmrgDec](VecEmrgDec.md) is the faster emergency rate used on a stop or fault.

## How it works

A vector move runs one velocity profile along the geometric path (see [VecSpeed](VecSpeed.md)). `VecDecel` sets the trailing slope of that profile in two ways:

- **End-of-path braking.** Each control cycle the profiler computes, from the path distance still remaining to [VecAbsTrgt](VecAbsTrgt.md), the highest path speed from which it could still come to rest exactly at the end using `VecDecel`, and clamps the path velocity to that value. This is what curves the cruise phase down into the stop at the end of the move:

$$
v_{dec} = -\text{VecDecel} \cdot T_s + \sqrt{\text{VecDecel}^{2} \cdot T_s^{2} + 2 \cdot \text{VecDecel} \cdot (\text{VecAbsTrgt} - \text{VecPosRef})}
$$

- **Speed reductions.** When [VecSpeed](VecSpeed.md) is lowered mid-move, or a [VecPause](VecPause.md) is requested, the path velocity ramps down at `VecDecel`.

The deceleration shapes the **resultant** path velocity; the rate seen on any one member axis is `VecDecel` scaled by that axis's share of the path. `VecDecel` is the normal rate; a [StopVec](StopVec.md) command or a fault substitutes the faster [VecEmrgDec](VecEmrgDec.md) instead. With jerk smoothing on ([VecJerk](VecJerk.md) ≠ 0), `VecDecel` is passed as the deceleration constraint to the S-curve path profiler.

## Examples

```text
AVecDecel=100000     ; vector deceleration (user units/s^2, default)
AVecDecel           ; read the current value
```

## See also

- [VecAccel](VecAccel.md) — vector acceleration rate
- [VecSpeed](VecSpeed.md) — target resultant speed
- [VecEmrgDec](VecEmrgDec.md) — emergency deceleration rate
