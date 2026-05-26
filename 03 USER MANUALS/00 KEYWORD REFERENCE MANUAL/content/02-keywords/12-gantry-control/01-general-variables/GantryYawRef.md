---
keyword: GantryYawRef
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

**Definition:**

GantryYawRef sets the yaw correction reference applied to the gantry (beam) axis to compensate for angular misalignment between the two drive motors. A non-zero value commands a differential position correction that reduces the yaw error. It is an axis-related parameter in user units, not saved to flash, and can be changed at any time.

**See also:**

[GantryOn](GantryOn.md), [GantryPosGain](../03-gantry-tuning/GantryPosGain.md)
