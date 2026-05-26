---
keyword: MaxPwrTemp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 90
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
  - 20
  - 80
  default: 65
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPwrTemp

MaxPwrTemp is the maximum allowed temperature in Celsius for the power generating
components of the product.
