---
keyword: GantryPosGain
summary: Proportional position gain for the gantry yaw correction controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 654
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 100000
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryPosGain

Proportional position gain for the gantry yaw correction controller.

## Overview

`GantryPosGain` sets the proportional position gain for the gantry yaw correction controller. It scales the yaw position error to produce the differential current command that drives the two beam motors to eliminate misalignment. It is an axis-related parameter saved to flash and can be changed at any time. It works alongside the integral term [GantryPosKi](GantryPosKi.md) and the velocity-loop gain [GantryVelGain](GantryVelGain.md). The allowed range is 0 to 100000 (default 100).

## Examples

```text
AGantryPosGain=200  ; set yaw position proportional gain
AGantryPosGain?     ; read the current gain
```

## See also

- [GantryPosKi](GantryPosKi.md) — yaw position-loop integral gain
- [GantryVelGain](GantryVelGain.md) — yaw velocity-loop proportional gain
- [GantryAccFFW](GantryAccFFW.md) — acceleration feedforward gain
- [GantryYawRef](../01-general-variables/GantryYawRef.md) — yaw correction reference
