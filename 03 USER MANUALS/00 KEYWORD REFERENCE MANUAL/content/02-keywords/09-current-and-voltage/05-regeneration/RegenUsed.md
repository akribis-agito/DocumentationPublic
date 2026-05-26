---
keyword: RegenUsed
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 378
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# RegenUsed

**Definition:**

RegenUsed selects whether an external or internal regeneration resistor is used by the controller. Setting this parameter configures the regen circuit to match the hardware configuration. It is a non-axis parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[RegenOn](RegenOn.md), [RegenOff](RegenOff.md), [RegenCurr](RegenCurr.md)
