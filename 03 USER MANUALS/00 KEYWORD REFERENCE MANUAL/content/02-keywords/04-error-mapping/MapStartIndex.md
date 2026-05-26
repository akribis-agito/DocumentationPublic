---
keyword: MapStartIndex
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 321
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 1
  - 300000
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapStartIndex

**Definition:**

MapStartIndex sets the index of the first active segment in the error-mapping configuration. Only map segments at or above this index are applied during position correction, allowing portions of the map table to be selectively disabled. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion or the motor is on.

**See also:**

[MapType](MapType.md), [MapStartPos](MapStartPos.md), [MapLength](MapLength.md), [MapEncoder](MapEncoder.md)
