---
summary: Read-only gantry velocity feedback — common (linear) on the master axis and differential (yaw) on the yaw axis.
keyword: GantryVel
availability:
  standalone: []
  central-i:
  - v5
can_code: 676
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int64
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2251799813685248
  - 2251799813685247
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryVel

Read-only gantry velocity feedback — common (linear) on the master axis and differential (yaw) on the yaw axis.

## Overview

`GantryVel` is a read-only variable that reports the gantry velocity feedback used by the gantry velocity loops while [GantryOn](../01-general-variables/GantryOn.md) is `1`. On the **master axis** it is the common-mode (linear) velocity — the mean of the two member-axis velocities; on the **yaw axis** it is the differential velocity (the difference between the two member-axis velocities). It is an axis-related status variable, valid while in motion and with the motor on, and is not saved to flash.

## How it works

Each control cycle, while gantry is on, the controller derives `GantryVel` per axis and uses it as the velocity term in the matching velocity PI loop:

$$
\text{VelErr} = \text{VelRef} - \text{GantryVel}
$$

- **Master axis (linear loop)** — `VelRef` is produced by the linear position loop; the error is acted on by the standard [VelGain](../../11-control-tuning/02-velocity-loop/VelGain.md) / [VelKi](../../11-control-tuning/02-velocity-loop/VelKi.md). In dual-loop mode the value is the auxiliary (motor-side) velocity scaled by the dual-loop factor — see [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md).
- **Yaw axis (yaw loop)** — `VelRef` is produced by the yaw position loop ([GantryPosGain](GantryPosGain.md) / [GantryPosKi](GantryPosKi.md)); the error is acted on by [GantryVelGain](GantryVelGain.md) and [GantryVelKi](GantryVelKi.md).

`GantryVel` is reported in user units. The [dual-loop gantry control overview](../04-dual-loop-gantry-control/00-overview.md) describes how `GantryVel` is computed under each control structure (including the `DualLoopFact` scaling) relative to [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md).

## Examples

```text
AGantryVel          ; on the master axis: common (linear) gantry velocity
BGantryVel          ; on the yaw axis:    differential (yaw) gantry velocity
```

### Edge cases

- **Gantry off** ([GantryOn](../01-general-variables/GantryOn.md) = 0) — not updated; the last value while gantry was on is held.
- **At gantry-on transition** — forced to `0` on both axes for one cycle while the velocity history primes.
- **Motor off** — the gantry calculation halts; a mid-flight loss of one member (`A` or `B`) on motor-off forces the other off with `CON_FLT_GANTRY_MEMBER_UNEXPECTED_MOTOR_OFF`.
- **Non-gantry axis** — reading on an axis that is neither master nor yaw returns `0`.
- **Platform** — v5 central-i only.

## See also

- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAuxVel](../02-gantry-kinematic-feedback/GantryAuxVel.md) — auxiliary-encoder velocity
- [Dual-loop gantry control](../04-dual-loop-gantry-control/00-overview.md) — how GantryVel is derived per mode
