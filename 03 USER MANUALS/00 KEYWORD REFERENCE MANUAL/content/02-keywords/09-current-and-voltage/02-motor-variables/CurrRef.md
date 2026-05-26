---
keyword: CurrRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 26
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
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrRef

**Definition:**

CurrRef is the current reference value used as input to the current control loop. It is the final current command value for the motor after the sum of control efforts (feedback loops and feedforward), current related compensation and injection, whichever applicable.

Please refer to [Control tuning – Current control](../../../02-keywords/11-control-tuning/06-current-control/00-overview.md) for CurrRef location.
