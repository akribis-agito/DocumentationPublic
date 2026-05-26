---
keyword: MapStartPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 323
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapStartPos

**Definition:**

MapStartPos is a per-segment array that defines the starting position of each error-mapping segment in encoder counts. Together with MapLength and MapPosGap it fully describes the positional extent and resolution of each map segment. It is an axis-related array saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapLength](MapLength.md), [MapPosGap](MapPosGap.md), [MapEncoder](MapEncoder.md), [MapTable/MapTableB/MapTableC/MapTableD/MapTableE](MapTable-MapTableB-MapTableC-MapTableD-MapTableE.md)
