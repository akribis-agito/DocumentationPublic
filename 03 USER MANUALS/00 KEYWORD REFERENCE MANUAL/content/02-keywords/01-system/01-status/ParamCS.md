---
keyword: ParamCS
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 428
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ParamCS

**Definition:**

ParamCS is a read-only array (indices 0–3) that holds a checksum computed over the controller's parameter set. The host can read this value to verify that the parameters stored on the device match an expected configuration without downloading the full parameter list.

**See also:**

[ParamAbout](ParamAbout.md), [Save](../02-operation/Save.md)
