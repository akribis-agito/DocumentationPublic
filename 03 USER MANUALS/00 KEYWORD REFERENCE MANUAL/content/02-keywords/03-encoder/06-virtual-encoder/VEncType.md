---
keyword: VEncType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 615
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncType

**Definition:**

VEncType sets the output format or signal type for the virtual encoder. Different values select the unit convention or encoding mode used when the virtual encoder position is emitted. It is an axis-related parameter saved to flash.

**See also:**

[VEncOn](VEncOn.md), [VEncSrc](VEncSrc.md), [VEncFact](VEncFact.md), [VEncFactDen](VEncFactDen.md)
