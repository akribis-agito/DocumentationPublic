---
keyword: InjectFreq
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 117
attributes:
  access: rw
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
  - 800000
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InjectFreq

**Condition:**

InjectFreq is only applicable for sine and square wave injection (InjectType = 1, 2, 3 or 4).

**Definition:**

InjectFreq is the frequency of the sine/square wave, in terms of Hz/100.

For example, if the sine wave frequency is 11.2Hz, InjectFreq should be 1120. Please refer to InjectType for more information on the sine and square waves.
