---
keyword: PlantModel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 558
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 81
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# PlantModel

**Definition:**

PlantModel is an array that stores the identified plant model coefficients used by the auto-tuning and velocity filter design algorithms. The coefficients describe the mechanical transfer function of the axis as determined by the identification procedure. It is an axis-related array saved to flash and can be changed at any time.

**See also:**

[CalcIden](CalcIden.md), [IdenResults](IdenResults.md)
