---
keyword: VelRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 25
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
  - -1300000000
  - 1300000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelRef

**Definition:**

VelRef is the velocity loop reference/input, in terms of main user unit per second. It is different from velocity reference (dPosRef) and is generally the sum of position controller output and velocity reference.

Please refer to [Control tuning – Velocity control](../../../02-keywords/11-control-tuning/04-velocity-control/00-overview.md) (if normal control is used) and [Control tuning – Dual-loop control](../../../02-keywords/11-control-tuning/02-dual-loop-control/00-overview.md) (if dual-loop control is used) for its signal path/derivation.
