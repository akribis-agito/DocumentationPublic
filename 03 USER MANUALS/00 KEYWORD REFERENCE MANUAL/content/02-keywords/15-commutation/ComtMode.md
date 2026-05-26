---
keyword: ComtMode
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 72
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 25
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ComtMode

**Definition:**

ComtMode stores the commutation settings.

**Note:**

1. Position loop will be closed temporarily and an additional user-defined, non-zero constant current command is applied. Additional control loop on commutation offset is formed.
2. The motor will only move slightly until the correct commutation offset is found and the motor returns to its starting position.

**Example:**

![image73.emf](../../assets/image73.emf)
