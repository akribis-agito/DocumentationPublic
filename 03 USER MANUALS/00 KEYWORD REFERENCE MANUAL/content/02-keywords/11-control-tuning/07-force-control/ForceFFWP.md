---
keyword: ForceFFWP
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 599
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceFFWP

**Condition:**

ForceFFWP is only used when ForcePIVOn = 1.

**Definition:**

ForceFFWP is the position-wise force feedforward gain, acting on the filtered force reference. The result will form part of the position reference setpoint.
