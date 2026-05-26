---
keyword: PStatParams
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 483
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: partial
overrides: {}
---
# PStatParams

**Definition:**

PStatParams is an array parameter that specifies which controller parameters are included in each periodic statistics transmission. Each element identifies one parameter to be sampled and sent at the interval configured by PStatInterval. It is a non-axis parameter saved to flash.

**See also:**

[PStatOn](PStatOn.md), [PStatPort](PStatPort.md), [PStatInterval](PStatInterval.md)
