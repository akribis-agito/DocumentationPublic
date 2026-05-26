---
keyword: Vc
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 15
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Vc

**Definition:**

Vc is the phase C voltage reference for space vector modulation, in terms fraction of full PWM count times a factor of 1000. Phase C is defined in the hardware reference guide.
