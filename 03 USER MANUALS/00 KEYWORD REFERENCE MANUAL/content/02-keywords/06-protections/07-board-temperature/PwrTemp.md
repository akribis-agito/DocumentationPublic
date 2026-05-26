---
keyword: PwrTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 38
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 25
  scaling: 1.0
  implemented: final
overrides: {}
---
# PwrTemp

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

`PwrTemp` returns the temperature in Celsius measured on the power-generating part of the product.
