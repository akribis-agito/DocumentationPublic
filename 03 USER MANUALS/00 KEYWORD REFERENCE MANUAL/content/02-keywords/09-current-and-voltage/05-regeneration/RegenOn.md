---
keyword: RegenOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 95
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
  - 12000
  - 95000
  default: 95000
  scaling: 1.0
  implemented: final
overrides: {}
---
# RegenOn

**Definition:**

RegenOn sets the DC bus voltage threshold above which the regeneration (braking resistor) circuit is activated. When the bus voltage rises above this level during deceleration, the controller switches on the regen resistor to dissipate excess energy. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[RegenOff](RegenOff.md), [RegenCurr](RegenCurr.md), [RegenUsed](RegenUsed.md)
