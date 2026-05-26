---
keyword: MaxPWM
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 91
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 1470
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPWM

**Definition:**

For PWM amplifiers, MaxPWM is used to limit the maximum duty cycle of PWM drives, and effectively the maximum voltage output to the motor. The units for MaxPWM is 0.1%, where 1000 represents 100% duty cycle, and a 0 value represents maximum 0% duty cycle.

**Example:**

For example, an axis has default value of MaxPWM=900 and bus voltage is 48V. To limit to maximum 30% duty cycle, user should set MaxPWM=300 to limit maximum voltage output to 14.4V.
