---
keyword: GantryAccFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 655
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
  - 500000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GantryAccFFW

**Definition:**

GantryAccFFW sets the acceleration feedforward gain for the gantry yaw correction controller. It scales the acceleration reference to produce a feedforward current that reduces yaw lag during dynamic moves. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[GantryPosGain](GantryPosGain.md), [GantryVelGain](GantryVelGain.md), [GantryYawRef](../01-general-variables/GantryYawRef.md)
