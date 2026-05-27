---
keyword: GantryOn
summary: Enables gantry MIMO control on the A axis, slaving the A and B axes together.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 650
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryOn

Enables gantry MIMO control on the A axis, slaving the A and B axes together.

## Overview

`GantryOn` controls operation of the gantry mode. With `AGantryOn=0` the gantry mode is disabled and each axis can be moved and controlled independently. With `AGantryOn=1` the gantry mode is enabled and the control scheme is automatically changed to gantry MIMO (multi-input multi-output) control, so that the two parallel drive motors are coordinated as a single mechanism.

When gantry mode is on, motion of the gantry stage is commanded by moving the A axis. The gantry feedbacks reported by [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) and the initial offset captured in [GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.md) are referenced to this mode, and the yaw correction set by [GantryYawRef](GantryYawRef.md) is applied while it is active.

`GantryOn` can be set only on the A axis: `?GantryOn` with `?` not equal to `A` returns an error. The A and B axes must always be used together for gantry control. `AGantryOn` is automatically cleared to `0` whenever `AMotorOn` or `BMotorOn` becomes `0`, so the gantry mode is typically enabled only after both motors have been turned on.

## Examples

```text
AGantryOn=1         ; enable gantry MIMO control (A and B coordinated)
AGantryOn=0         ; disable gantry mode; axes controlled independently
AGantryOn          ; read whether gantry mode is active
```

## See also

- [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) — MIMO gantry control feedbacks
- [GantryOffset](../02-gantry-kinematic-feedback/GantryOffset.md) — initial A/B offset captured when gantry is switched on
- [GantryYawRef](GantryYawRef.md) — yaw correction reference applied in gantry mode
- [MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) — both A and B motors must be on to keep gantry mode active
