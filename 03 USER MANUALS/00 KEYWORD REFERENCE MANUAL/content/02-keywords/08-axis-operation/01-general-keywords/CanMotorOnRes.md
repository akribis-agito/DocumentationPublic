---
keyword: CanMotorOnRes
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 413
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CanMotorOnRes

**Definition:**

CanMotorOnRes is a read-only parameter that holds the result code from the last CanMotorOn command. A zero value indicates the motor was enabled successfully; non-zero values indicate the reason the enable attempt was rejected. It is an axis-related status variable that is not saved to flash.

**See also:**

[CanMotorOn](CanMotorOn.md), [MotorOn](MotorOn.md)
