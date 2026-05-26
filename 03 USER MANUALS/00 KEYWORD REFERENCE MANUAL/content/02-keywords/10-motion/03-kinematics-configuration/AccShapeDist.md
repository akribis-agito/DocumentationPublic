---
keyword: AccShapeDist
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 163
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AccShapeDist

**Definition:**

AccShapeDist is an array that defines the positional distances of each segment in the acceleration-shaping profile. Together with AccShapeFact it specifies how the acceleration magnitude is distributed over the move to reduce mechanical vibration. It is an axis-related array saved to flash and can be changed at any time.

**See also:**

[AccShapeOn](AccShapeOn.md), [AccShapeFact](AccShapeFact.md)
