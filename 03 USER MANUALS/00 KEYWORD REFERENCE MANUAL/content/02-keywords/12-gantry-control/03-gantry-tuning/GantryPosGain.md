---
keyword: GantryPosGain
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

**Definition:**

GantryPosGain sets the proportional position gain for the gantry yaw correction controller. It scales the yaw position error to produce the differential current command that drives the two beam motors to eliminate misalignment. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[GantryVelGain](GantryVelGain.md), [GantryAccFFW](GantryAccFFW.md), [GantryYawRef](../01-general-variables/GantryYawRef.md)
