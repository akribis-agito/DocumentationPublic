---
keyword: VEncSrc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 614
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncSrc

**Definition:**

VEncSrc selects the source signal used to generate the virtual encoder output. The chosen source is scaled and delayed according to the other VEnc parameters to produce the virtual encoder position. It is an axis-related parameter saved to flash.

**See also:**

[VEncOn](VEncOn.md), [VEncType](VEncType.md), [VEncFact](VEncFact.md), [VEncFactDen](VEncFactDen.md)
