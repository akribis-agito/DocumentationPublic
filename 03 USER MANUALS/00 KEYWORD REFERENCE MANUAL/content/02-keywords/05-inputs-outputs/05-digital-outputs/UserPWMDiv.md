---
keyword: UserPWMDiv
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 627
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 15
  default: 9
  scaling: 1.0
  implemented: final
overrides: {}
---
# UserPWMDiv

**Definition:**

UserPWMDiv sets the period divisor for the user PWM outputs, controlling the PWM frequency for all channels defined by UserPWM. A higher value produces a lower PWM frequency. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[UserPWM](UserPWM.md), [DOutMode](DOutMode.md)
