---
keyword: ForceFFW
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 589
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
  - 1000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceFFW

**Definition:**

ForceFFW is the current-wise force feedforward gain, acting on the filtered force reference. The result will form part of the current reference setpoint.
