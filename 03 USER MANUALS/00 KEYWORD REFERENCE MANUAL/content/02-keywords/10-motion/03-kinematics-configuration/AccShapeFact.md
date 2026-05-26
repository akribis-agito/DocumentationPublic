---
keyword: AccShapeFact
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 164
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeFact

**Definition:**

AccShapeFact is an array that defines the acceleration scaling factors for each segment of the acceleration-shaping profile. Each element specifies the fraction of the maximum acceleration applied during the corresponding segment defined by AccShapeDist. It is an axis-related array saved to flash and can be changed at any time.

**See also:**

[AccShapeOn](AccShapeOn.md), [AccShapeDist](AccShapeDist.md)
