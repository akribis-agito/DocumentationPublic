---
keyword: UserPWM
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 626
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4095
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserPWM

**Definition:**

UserPWM is an array that sets the duty cycle of user-controlled PWM output channels. Each element corresponds to one PWM channel, and the value determines the on-time as a fraction of the period set by UserPWMDiv. It is a non-axis array saved to flash and can be changed at any time.

**See also:**

[UserPWMDiv](UserPWMDiv.md), [DOutMode](DOutMode.md)
