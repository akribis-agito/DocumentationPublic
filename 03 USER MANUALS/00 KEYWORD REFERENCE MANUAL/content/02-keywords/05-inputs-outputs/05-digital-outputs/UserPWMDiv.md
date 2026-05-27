---
keyword: UserPWMDiv
summary: Period divisor setting the PWM frequency for all user PWM channels.
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

Period divisor setting the PWM frequency for all user PWM channels.

## Overview

`UserPWMDiv` sets the period divisor for the user PWM outputs, which fixes the PWM frequency shared by all channels defined in [UserPWM](UserPWM.md). A higher value lengthens the period, producing a **lower** PWM frequency. Saved to flash.

## Examples

```text
AUserPWMDiv=9        ; default period divisor
```

## See also

- [UserPWM](UserPWM.md) — per-channel duty cycle
- [DOutSelect](DOutSelect.md) — route a PWM channel to an output
