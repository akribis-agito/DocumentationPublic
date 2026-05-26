---
keyword: AuxVel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 6
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AuxVel

**Definition:**

AuxVel reports the backward Euler derivative of auxiliary encoder feedback (AuxPos), in terms of auxiliary user unit per second (configurable by AuxUsrUnits).

$$
AuxVel\  = \ \frac{AuxPos\left( 1 - z^{- 1} \right)}{T_{s}}
$$
