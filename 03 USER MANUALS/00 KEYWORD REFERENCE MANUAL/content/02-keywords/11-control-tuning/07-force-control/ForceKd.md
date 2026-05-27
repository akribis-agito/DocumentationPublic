---
keyword: ForceKd
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 588
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
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# ForceKd

**Definition:**

ForceKd is the derivative gain for standard form PID control in the force loop. Please refer to the block diagram for gain scaling information.
