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
  range:
  - -655360
  - 655360
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RefOffsetStep

Per-sample position offset magnitude applied during a reference offset correction.

## Overview

`RefOffsetStep` sets the magnitude of each incremental position offset applied per servo sample during a reference offset correction. Together with [RefOffsetSamp](RefOffsetSamp.md), which sets the number of samples, it controls the rate at which a position correction is introduced into the reference trajectory. It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## How it works

While a correction is armed ([RefOffsetSamp](RefOffsetSamp.md) `> 0`) and the axis is in motion, the controller adds `RefOffsetStep` to the high-precision reference accumulator on **every** servo cycle. The total injected shift is therefore about `RefOffsetStep × RefOffsetSamp`.

The value is added at the **accumulator scaling** of the reference (the 50.14 / `2^14` fixed-point reference). This means `RefOffsetStep` effectively behaves like a *velocity*: a value equal to `2^14` (16384) corresponds to one position count of shift per cycle, i.e. a constant velocity bias for the duration of the ramp. Use small values; because the offset bypasses the [Accel](Accel.md)/[Decel](Decel.md) profiler limits, a large step produces a sharp velocity jump in the reference.

A positive `RefOffsetStep` shifts the reference forward, a negative value backward. See [RefOffsetSamp](RefOffsetSamp.md) for arming and auto-clear behaviour.

### Edge cases

- **Motor off / not in motion:** the value is held; no injection occurs (the countdown is also held).
- **Out-of-range write:** clamped to the ±(sample-rate × 10) range shown in the frontmatter (the same clamp in v4 and v5).
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** as for [RefOffsetSamp](RefOffsetSamp.md); the offset rides through the wrap.
- **Active fault:** the value is preserved but the countdown is cleared.
- **Large value (velocity-bias semantics):** because `RefOffsetStep` is added to the 50.14-scaled accumulator, a value of `16384` is one count of position bias per cycle (equivalent to ~16384 counts/sec at the standard sample rate). Set values larger than this carefully — they translate to large velocity steps in the reference and can saturate the velocity loop.
- **`RefOffsetStep = 0` with non-zero `RefOffsetSamp`:** the countdown still runs but injects nothing — a no-op.
- **Other motion modes:** runs in any mode that sets the in-motion bit.

## Examples

```text
ARefOffsetStep=16384 ; add ~1 position count per servo cycle while armed
ARefOffsetStep=-4096 ; small backward bias per cycle
ARefOffsetStep      ; query current value
```

## Changes between versions

The ±(sample-rate × 10) range clamp (shown in the frontmatter range) applies in both v4 and v5; the injection mechanism is unchanged. **v5 is central-i only.**

## See also

- [RefOffsetSamp](RefOffsetSamp.md) — number of samples over which the offset is applied
- [PosRef](../01-kinematics-status/PosRef.md) — the reference accumulator the step is added to
