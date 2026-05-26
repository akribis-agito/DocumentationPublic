---
keyword: MapEncoder
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 322
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 4
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 2
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapEncoder

**Definition:**

MapEncoder is a per-segment array that selects which encoder source is used as the position reference for that segment of the error-mapping table. Each element corresponds to a map segment defined by MapStartPos and MapLength. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapType](MapType.md), [MapStartPos](MapStartPos.md), [MapLength](MapLength.md), [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)
