---
keyword: MapLength
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 324
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
  - 60000
  default: 10
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapLength

**Definition:**

MapLength is a per-segment array that specifies the number of correction entries in each error-mapping segment. It defines how many positions within the segment are covered by the corresponding MapTable entries. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapStartPos](MapStartPos.md), [MapPosGap](MapPosGap.md), [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)
