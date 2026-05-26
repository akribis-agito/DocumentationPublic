---
keyword: PStatInterval
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 482
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
  - 2
  - 10000
  default: 1000
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatInterval

**Definition:**

PStatInterval sets the time interval in milliseconds between successive parameter statistics transmissions when PStatOn is active. It is a non-axis parameter saved to flash.

**See also:**

[PStatOn](PStatOn.md), [PStatPort](PStatPort.md), [PStatParams](PStatParams.md)
