---
keyword: MasterPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 44
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MasterPos

**Definition:**

MasterPos tracks the change of master variable after scaling, by accumulating the delta as shown.

$$
\mathrm{\Delta}_{MasterPos} = \frac{MasterFact}{MasterFactDen} \bullet \mathrm{\Delta}_{master\ variable}
$$
