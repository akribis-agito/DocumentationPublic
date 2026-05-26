---
keyword: GantryVelGain
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

**Definition:**

GantryVelGain sets the proportional velocity gain for the gantry yaw correction controller. It scales the differential velocity error to produce a corrective current that damps yaw oscillation. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[GantryPosGain](GantryPosGain.md), [GantryAccFFW](GantryAccFFW.md), [GantryVelFFW](GantryVelFFW.md)
