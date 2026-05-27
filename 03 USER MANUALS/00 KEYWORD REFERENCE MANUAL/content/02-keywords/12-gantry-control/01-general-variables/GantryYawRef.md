---
keyword: GantryYawRef
summary: Yaw correction reference commanding a differential offset between the two gantry motors.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 679
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
  - -20000
  - 20000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryYawRef

Yaw correction reference commanding a differential offset between the two gantry motors.

## Overview

`GantryYawRef` is the position reference for the gantry's **differential (yaw) loop** — the virtual axis that controls the difference between the two beam ends (see the common/differential explanation under [GantryOn](GantryOn.md)). Setting it to `0` commands the beam to stay square; a non-zero value (in user units) commands a deliberate skew between the two ends, used to compensate for a mechanical misalignment so the load runs true. It is axis-scoped, not saved to flash, and can be changed at any time, including in motion. The allowed range is -20000 to 20000.

The yaw loop compares this reference against the differential feedback (the yaw-axis value of [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md)) and drives a differential current into the two motors — adding to one and subtracting from the other — to close the error. Its response is set by the yaw-axis gains [GantryPosGain](../03-gantry-tuning/GantryPosGain.md), [GantryVelGain](../03-gantry-tuning/GantryVelGain.md) and the associated feedforward/integral terms; the resulting differential current is reported by [GantryCurrRef](GantryCurrRef.md). The reference only takes effect while gantry mode is active ([GantryOn](GantryOn.md) = 1).

## How it works

Each control cycle the yaw loop forms its error from `GantryYawRef` and the differential feedback, runs the yaw position and velocity loops, and produces a yaw current command. That command is then combined with the common-mode (linear) current command when the controller recombines the two virtual-axis outputs into the two physical motor currents: one motor receives linear + yaw, the other linear − yaw. Because the loops are decoupled, commanding a yaw offset shifts the squareness of the beam without translating the stage.

## Examples

```text
AGantryYawRef=500   ; command a yaw correction offset (user units)
AGantryYawRef=0     ; remove the yaw correction
AGantryYawRef      ; read the current yaw reference
```

## See also

- [GantryOn](GantryOn.md) — must be enabled for the yaw correction to be applied; explains common vs differential mode
- [GantryFdbk](../02-gantry-kinematic-feedback/GantryFdbk.md) — differential (yaw) feedback this reference is compared against
- [GantryCurrRef](GantryCurrRef.md) — differential current the yaw loop produces
- [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) — proportional gain of the yaw position loop
- [GantryVelGain](../03-gantry-tuning/GantryVelGain.md) — proportional gain of the yaw velocity loop
