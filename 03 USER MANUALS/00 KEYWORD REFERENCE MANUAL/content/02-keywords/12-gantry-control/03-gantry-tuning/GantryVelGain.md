---
keyword: GantryVelGain
summary: Proportional velocity gain for the gantry yaw correction controller.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 656
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
# GantryVelGain

Proportional velocity gain for the gantry yaw correction controller.

## Overview

`GantryVelGain` sets the proportional velocity gain for the gantry yaw correction controller. It scales the differential velocity error to produce a corrective current that damps yaw oscillation. It is an axis-related parameter saved to flash and can be changed at any time. It works alongside the integral term [GantryVelKi](GantryVelKi.md) and the position-loop gain [GantryPosGain](GantryPosGain.md). The allowed range is 0 to 100000 (default 100).

## Examples

```text
AGantryVelGain=150  ; set yaw velocity proportional gain
AGantryVelGain?     ; read the current gain
```

## See also

- [GantryVelKi](GantryVelKi.md) — yaw velocity-loop integral gain
- [GantryPosGain](GantryPosGain.md) — yaw position-loop proportional gain
- [GantryAccFFW](GantryAccFFW.md) — acceleration feedforward gain
- [GantryVelFFW](GantryVelFFW.md) — velocity feedforward gain
