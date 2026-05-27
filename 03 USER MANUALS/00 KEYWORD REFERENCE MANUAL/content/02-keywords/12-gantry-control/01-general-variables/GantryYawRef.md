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

`GantryYawRef` sets the yaw correction reference applied to the gantry to compensate for angular misalignment between the two drive motors. A non-zero value commands a differential position correction (in user units) that drives the gantry yaw controller to reduce the yaw error. It is an axis-related parameter, not saved to flash, and can be changed at any time while gantry mode is active (see [GantryOn](GantryOn.md)). The correction is applied through the gantry tuning loop, whose response is set by gains such as [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) and [GantryVelGain](../03-gantry-tuning/GantryVelGain.md). The allowed range is -20000 to 20000.

## Examples

```text
AGantryYawRef=500   ; command a yaw correction offset (user units)
AGantryYawRef=0     ; remove the yaw correction
AGantryYawRef?      ; read the current yaw reference
```

## See also

- [GantryOn](GantryOn.md) — must be enabled for the yaw correction to be applied
- [GantryPosGain](../03-gantry-tuning/GantryPosGain.md) — proportional gain of the yaw position loop
- [GantryVelGain](../03-gantry-tuning/GantryVelGain.md) — proportional gain of the yaw velocity loop
