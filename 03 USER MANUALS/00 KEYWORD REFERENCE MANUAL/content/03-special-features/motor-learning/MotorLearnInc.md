---
keyword: MotorLearnInc
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 445
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
  - 1200
  default: 600
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range: null
    default: null
---
# MotorLearnInc

**Definition:**

MotorLearnInc sets the commutation-angle step size used by the motor-learning routine: the amount by which the commutation electrical angle is advanced on each step while the motor is driven open-loop during a learning pass. The default is approximately 90 electrical degrees, and the upper limit is approximately 180 electrical degrees. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnMod](MotorLearnMod.md), [MotorLearnPl](MotorLearnPl.md)
