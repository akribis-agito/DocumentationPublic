---
keyword: PDPos
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 4
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
# PDPos

**Definition:**

PDPos is the pulse and direction counter that accumulates the number of pulses detected in each controller cycle, multiplied by the scaling factor (defined by PDFact and PDFactDen) and direction sign (defined by PDEncDir). The accumulation (integration) occurs at every controller cycle.

PDPos is represented in pulse-direction unit when queried (see [PDUsrUnits](../../../02-keywords/10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md)).
