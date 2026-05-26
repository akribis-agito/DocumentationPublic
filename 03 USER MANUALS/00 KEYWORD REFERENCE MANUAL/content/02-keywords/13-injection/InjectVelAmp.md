---
keyword: InjectVelAmp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 115
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectVelAmp

**Condition:**

InjectVelAmp is only applicable for injection at velocity command (InjectPoint = 3).

**Definition:**

InjectVelAmp is the amplitude of the velocity injection, where its unit depends on the dual loop setting. Please refer to [Control tuning – Dual-loop control](../../02-keywords/11-control-tuning/02-dual-loop-control/00-overview.md) for more information.
