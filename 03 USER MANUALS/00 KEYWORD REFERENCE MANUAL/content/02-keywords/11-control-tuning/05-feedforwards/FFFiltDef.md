---
keyword: FFFiltDef
availability:
  standalone: []
  central-i:
  - v5
can_code: 729
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FFFiltDef

**Definition:**

FFFiltDef is used to define the feedforward filters parameters. Each filter can be described by up to 5 parameters.

Please refer to [customisable filter appendix](#_Customisable_filter_(FiltDef)), with index N = 1 for feedforward filter.
