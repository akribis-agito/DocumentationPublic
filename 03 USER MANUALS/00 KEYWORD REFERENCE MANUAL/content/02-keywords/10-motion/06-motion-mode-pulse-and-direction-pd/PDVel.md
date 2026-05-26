---
keyword: PDVel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 7
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: pd_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDVel

**Definition:**

PDVel is the rate of change of scaled PD counter (PDPos), in terms of pulse-direction units per second. Please refer to [PDUsrUnits](../../../02-keywords/10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) for more information on query conversion.
