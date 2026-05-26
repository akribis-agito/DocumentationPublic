---
keyword: CISyncDef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 506
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
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
# CISyncDef

**Definition:**

CISyncDef is an axis-related array that defines the set of parameters exchanged synchronously over the Central-i link each control cycle. The definition is saved to flash and takes effect after [CIConnect](CIConnect.md) is executed.

**See also:**

[CILinkConfig](CILinkConfig.md), [CIOfflineDef](CIOfflineDef.md), [CIConnect](CIConnect.md)
