---
keyword: VEncFactDen
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 618
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
  - 1
  - 500000000
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# VEncFactDen

**Definition:**

VEncFactDen is the denominator of the scaling ratio applied to the virtual encoder source signal. Together with VEncFact it defines the exact rational scale factor (VEncFact / VEncFactDen) used to convert the source position into the virtual encoder output. It is an axis-related parameter saved to flash.

**See also:**

[VEncFact](VEncFact.md), [VEncOn](VEncOn.md), [VEncSrc](VEncSrc.md)
