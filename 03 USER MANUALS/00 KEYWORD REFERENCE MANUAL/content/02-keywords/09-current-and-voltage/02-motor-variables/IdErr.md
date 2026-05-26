---
keyword: IdErr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 22
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
# IdErr

**Condition:**

IdErr is only applicable for three-phase motor (MotorType = 3 or 4). Otherwise, IdErr is 0.

**Definition:**

IdErr is the calculated current error in the direct axis, in milliamperes, defined as shown.

$$
IdErr\ \lbrack mA\rbrack\  = \ IdRef\ \lbrack mA\rbrack\  - \ Id\ \lbrack mA\rbrack
$$

It is used in three-phase motor dq0-domain current control.
