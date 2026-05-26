---
keyword: PosBeforeMap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 160
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: false
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosBeforeMap

**Definition:**

PosBeforeMap reports the raw axis position in user units before any error-mapping correction has been applied. It is useful for diagnostics and for verifying the map correction that is being added to the feedback position. It is a read-only, axis-related status variable that is not saved to flash.

**See also:**

[MapType](MapType.md), [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)
