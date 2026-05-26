---
keyword: StepBits
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 256
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
  - 2
  - 16
  default: 2
  scaling: 1.0
  implemented: final
overrides: {}
---
# StepBits

**Condition:**

This keyword is only used when MotorType = 6 or 7.

**Definition:**

StepBits is used to define the number of steps per electrical cycle, where

$$
Steps\ per\ electrical\ cycle = 2^{StepBits}\ \lbrack step\ count\rbrack
$$

StepBits = 2 and StepBits = 3 correspond to full-stepping (4 steps per electrical cycle) and half-stepping (8 steps per electrical cycle) respectively.

Microstepping can be achieved by increasing StepBits above value of 2.
