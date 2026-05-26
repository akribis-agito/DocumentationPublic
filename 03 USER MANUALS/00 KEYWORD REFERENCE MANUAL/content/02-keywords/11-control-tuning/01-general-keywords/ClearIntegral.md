---
keyword: ClearIntegral
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 412
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ClearIntegral

**Definition:**

ClearIntegral is a command that zeroes the integrator state of the position and velocity control loops. It is used to eliminate any accumulated integral wind-up, typically before enabling the motor or after a large position disturbance. It is an axis-related command function that cannot be issued while the axis is in motion.

**See also:**

[PosKi](../03-position-control/PosKi.md), [VelKi](../04-velocity-control/VelKi.md)
