---
keyword: ComtAng
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 73
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
  - 0
  - 35999
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ComtAng

**Definition:**

ComtAng is the instantaneous commutation angle of motor, in degrees scaled by 100. The value is wrapped between lower limit of 0 and upper limit of 35999.

<span class="mark">For single-phase motor, ….</span>
