---
keyword: MotorCurr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 8
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
# MotorCurr

**Definition:**

MotorCurr is the total feedback current vector amplitude of motor, in milliamperes.

| Motor type | Descriptions |
|----|----|
| Single-phase motor (MotorType = 1 or 2) | 
$$
MotorCurr\ \lbrack mA\rbrack\  = \ Ia\ \lbrack mA\rbrack
$$ |
| Three-phase motor (MotorType = 3 or 4) | 
$$
MotorCurr\ \lbrack mA\rbrack\  = \ sign(Iq) \bullet \sqrt{{Iq}^{2} + {Id}^{2}}\ \lbrack mA\rbrack
$$ |
| Two-phase stepper motor (MotorType = 6 or 7) | 
$$
MotorCurr\ \lbrack mA\rbrack\  = \ \sqrt{{Ia}^{2} + {Ib}^{2}}\ \lbrack mA\rbrack
$$ |
