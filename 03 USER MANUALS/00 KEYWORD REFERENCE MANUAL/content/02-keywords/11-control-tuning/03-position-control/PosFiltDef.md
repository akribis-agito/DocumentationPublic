---
keyword: PosFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 123
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 6
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
overrides:
  central-i.v5:
    ok_in_motion: true
    ok_motor_on: true
---
# PosFiltDef

**Definition:**

PosFiltDef is used to define the position filters parameters. Each filter can be described by up to 5 parameters.

Please refer to [Appendix – Customisable filter](#_Customisable_filter_(FiltDef)), with index N denoting filter number, as shown.

| Index (N) | Descriptions          |
|-----------|-----------------------|
| 1         | Post-profiler filter  |
| 2         | Position error filter |
