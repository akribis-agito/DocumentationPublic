---
keyword: PStatPort
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 481
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 3
  default: 1
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatPort

**Definition:**

PStatPort selects the communication port over which the parameter statistics data is transmitted when PStatOn is active. It is a non-axis parameter saved to flash.

**See also:**

[PStatOn](PStatOn.md), [PStatParams](PStatParams.md), [PStatInterval](PStatInterval.md)
