---
keyword: PStatOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 480
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatOn

**Definition:**

PStatOn enables or disables the periodic parameter statistics streaming feature. When set to a non-zero value, the controller transmits the parameters listed in PStatParams over the port configured by PStatPort at the interval set by PStatInterval. It is a non-axis parameter and is not saved to flash.

**See also:**

[PStatParams](PStatParams.md), [PStatPort](PStatPort.md), [PStatInterval](PStatInterval.md)
