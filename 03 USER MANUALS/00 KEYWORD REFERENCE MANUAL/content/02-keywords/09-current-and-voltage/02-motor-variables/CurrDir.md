---
keyword: CurrDir
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 76
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrDir

**Definition:**

CurrDir configures the direction of the motor excitation. If CurrDir = 0, motor direction is not flipped. If CurrDir = 1, motor direction is flipped.

It is normally used together with EncDir to flip the axis direction to the desired configuration.
