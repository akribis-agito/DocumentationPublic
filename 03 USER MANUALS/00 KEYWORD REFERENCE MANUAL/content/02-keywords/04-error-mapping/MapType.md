---
keyword: MapType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 320
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 3
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapType

**Definition:**

MapType selects the error-mapping correction mode applied to the axis position feedback. Setting this to a non-zero value activates position error compensation using the correction values stored in the MapTable arrays. It is an axis-related parameter, not saved to flash, and cannot be changed while the axis is in motion.

**See also:**

[MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md), [MapEncoder](MapEncoder.md), [MapStartIndex](MapStartIndex.md), [PosBeforeMap](PosBeforeMap.md)
