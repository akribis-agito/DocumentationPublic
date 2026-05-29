---
keyword: AuxPos
summary: Auxiliary-encoder position feedback, in auxiliary user units.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 3
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# AuxPos

Auxiliary-encoder position feedback, in auxiliary user units.

## Overview

`AuxPos` reports the auxiliary encoder feedback, expressed in auxiliary user units (configurable via [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md)). It is the auxiliary-loop counterpart of the main position feedback [Pos](Pos.md): it feeds dual-loop control, can act as a [MapEncoder](../../04-error-mapping/MapEncoder.md) source for error mapping, and is the value the auxiliary velocity [AuxVel](AuxVel.md) is derived from.

Although `AuxPos` is writable, it can only be set while the axis is disabled (it is declared `RW` with no-motion / no-motor-on flags). Its value resets to `0` on power-up.

## How it works

### Reading

Each control cycle the controller reads the auxiliary encoder, computes the per-cycle change and accumulates it into the auxiliary position; the per-cycle delta also drives [AuxVel](AuxVel.md). On the controller hardware the aux encoder is a physical input; on the central-i master the aux value is delivered per axis over the network. With an absolute auxiliary encoder it is initialised from the absolute reading at startup.

### Use in dual-loop and error mapping

- **Dual-loop:** when [DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) = 1, the auxiliary encoder is the load-side feedback. The velocity loop uses the auxiliary velocity scaled by [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) (see [Vel](Vel.md)`[1]`), and the commutation position and its delta are taken from the auxiliary encoder.
- **Error mapping:** an [error-map encoder](../../04-error-mapping/MapEncoder.md) selection can point the map source at the auxiliary position of an axis, so the auxiliary encoder can supply the mapping coordinate. By default, auxiliary error mapping is not enabled; contact Agito if required.

### Edge cases

- **Motor off:** `AuxPos` keeps tracking the auxiliary encoder reading regardless of motor state — it is a raw feedback value, not a closed-loop quantity. Only writes to `AuxPos` require the motor to be disabled.
- **Simulation mode (`MotorType` = 5):** there is no physical aux encoder, so `AuxPos` stays at its last written value (no auto-following of an aux reference).
- **Modulo (`ModRev`):** the modulo/continuous-rotation wrap applies only to the main feedback [Pos](Pos.md); `AuxPos` is **not** wrapped by [ModRev](../../03-encoder/04-modulo-mode/ModRev.md). For a rotary load through a gear, treat `AuxPos` as an unbounded accumulator.
- **Gantry:** auxiliary encoders are per-axis and are not combined into the gantry common-mode feedback; they are still useful for per-axis dual-loop on each gantry leg.
- **Out-of-range write:** the parameter system clamps writes to the declared range; values outside the range are rejected with an error rather than silently truncated.
- **Active fault:** `AuxPos` continues to update from the auxiliary encoder even while the axis is in fault; reading it during fault is the normal way to inspect the load-side stop position.

## Examples

```text
AAuxPos             ; read the auxiliary encoder position
AAuxPos=0           ; preset to zero (axis must be disabled)
```

## Changes between versions

In **v5 (central-i)** `AuxPos` is a 64-bit value; the reading, dual-loop and error-mapping uses are the same. The data-type/range difference is shown in the frontmatter. **v5 is central-i only**, so on standalone `AuxPos` remains the v4 32-bit value.

## See also

- [AuxVel](AuxVel.md) — auxiliary velocity, derived from `AuxPos`
- [Pos](Pos.md) — main encoder position feedback
- [AuxUsrUnits](../../03-encoder/01-general-settings/UsrUnits-AuxUsrUnits.md) — auxiliary user-unit scaling
- [DualLoopOn](../../11-control-tuning/02-dual-loop-control/DualLoopOn.md) / [DualLoopFact](../../11-control-tuning/02-dual-loop-control/DualLoopFact.md) — dual-loop use of the auxiliary encoder
