---
keyword: IaErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 20
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# IaErr

**Definition:**

IaErr is the calculated current error of phase A, in milliamperes, defined as shown.

$$
IaErr\ \lbrack mA\rbrack\  = \ IaRef\ \lbrack mA\rbrack\  - \ Ia\ \lbrack mA\rbrack
$$

It is used in single-phase motor current control, three-phase motor abc-domain current control and stepper phase current control.
