---
keyword: RefOffsetStep
summary: Per-sample position offset magnitude applied during a reference offset correction.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 166
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range: null
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - -655360
    - 655360
---
# RefOffsetStep

Per-sample position offset magnitude applied during a reference offset correction.

## Overview

`RefOffsetStep` sets the magnitude of each incremental position offset applied per servo sample during a reference offset correction. Together with [RefOffsetSamp](RefOffsetSamp.md), which sets the number of samples, it controls the rate at which a position correction is introduced into the reference trajectory. It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## How it works

While a correction is armed ([RefOffsetSamp](RefOffsetSamp.md) `> 0`) and the axis is in motion, the firmware adds `RefOffsetStep` to the high-precision reference accumulator `gllPosRef` on **every** servo cycle (`AG300_CTL01ControlInterrupt.c:3780`). The total injected shift is therefore about `RefOffsetStep × RefOffsetSamp`.

The value is added at the **accumulator scaling** of `gllPosRef` (the 50.14 / `2^14` fixed-point reference). As the firmware comment notes, this means `RefOffsetStep` effectively behaves like a *velocity*: a value equal to `2^14` (16384) corresponds to one position count of shift per cycle, i.e. a constant velocity bias for the duration of the ramp. Use small values; because the offset bypasses the [Accel](Accel.md)/[Decel](Decel.md) profiler limits, a large step produces a sharp velocity jump in the reference.

A positive `RefOffsetStep` shifts the reference forward, a negative value backward. See [RefOffsetSamp](RefOffsetSamp.md) for arming and auto-clear behaviour.

## Examples

```text
ARefOffsetStep=16384 ; add ~1 position count per servo cycle while armed
ARefOffsetStep=-4096 ; small backward bias per cycle
ARefOffsetStep      ; query current value
```

## Changes between versions

In **v5 (central-i)** `RefOffsetStep` gains an explicit clamp of ±655360 (shown in the frontmatter range); the injection mechanism is otherwise unchanged. **v5 is central-i only.**

## See also

- [RefOffsetSamp](RefOffsetSamp.md) — number of samples over which the offset is applied
- [PosRef](../01-kinematics-status/PosRef.md) — the reference accumulator the step is added to
