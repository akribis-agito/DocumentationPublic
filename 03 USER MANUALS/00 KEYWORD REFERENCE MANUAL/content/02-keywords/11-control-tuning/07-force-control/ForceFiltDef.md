---
keyword: ForceFiltDef
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 740
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
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
# ForceFiltDef

**Condition:**

ForceFiltDef is only used when ForcePIVOn = 0.

**Definition:**

ForceFiltDef is used to define the force filters parameters. Each filter can be described by up to 5 parameters.

Please refer to [customisable filter appendix](#_Customisable_filter_(FiltDef)), with index N denoting filter number, as shown.

| Index (N) | Descriptions   |
|-----------|----------------|
| 1         | Force filter 1 |
| 2         | Force filter 2 |
