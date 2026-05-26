---
keyword: VelFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 121
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 21
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelFiltDef

**Definition:**

VelFiltDef is used to define the velocity filters parameters. Each filter can be described by up to 5 parameters.

Please refer to [customisable filter appendix](#_Customisable_filter_(FiltDef)), with index N denoting filter number, as shown.

| Index (N) | Descriptions      |
|-----------|-------------------|
| 1         | Velocity filter 1 |
| 2         | Velocity filter 2 |
| 3         | Velocity filter 3 |
| 4         | Velocity filter 4 |
