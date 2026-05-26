---
keyword: RegenOff
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 96
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
# RegenOff

**Definition:**

RegenOff sets the DC bus voltage threshold below which the regeneration circuit is deactivated. Once the bus voltage drops below this level the controller switches off the regen resistor. Setting RegenOff lower than RegenOn provides hysteresis to prevent rapid switching. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[RegenOn](RegenOn.md), [RegenCurr](RegenCurr.md), [RegenUsed](RegenUsed.md)
