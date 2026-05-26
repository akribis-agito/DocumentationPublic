---
keyword: RegenCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 349
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RegenCurr

**Definition:**

RegenCurr is a read-only parameter that reports the current flowing through the regeneration resistor. It allows monitoring of the power being dissipated by the regen circuit during braking. It is a non-axis status variable that is not saved to flash.

**See also:**

[RegenOn](RegenOn.md), [RegenOff](RegenOff.md), [RegenUsed](RegenUsed.md)
