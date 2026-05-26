---
keyword: MapPosGap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 325
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
  - 8000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapPosGap

**Definition:**

MapPosGap is a per-segment array that sets the position spacing between consecutive correction entries within each error-mapping segment. A larger gap means fewer correction points are used to cover the segment's positional range. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapLength](MapLength.md), [MapStartPos](MapStartPos.md), [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)
