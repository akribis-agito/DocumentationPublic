---
keyword: UserPWM
summary: Duty cycle of each user-controlled PWM output channel.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Duty cycle of each user-controlled PWM output channel.

## Overview

`UserPWM` sets the duty cycle of the user PWM output channels — one element per channel. The value is the on-time as a fraction of the PWM period (0–4095), where the period is set by [UserPWMDiv](UserPWMDiv.md). To drive a PWM signal on a physical output, route the channel to that output with [DOutSelect](DOutSelect.md) (UserPWM 1 / UserPWM 2 options). Saved to flash.

## Examples

```text
AUserPWM[1]=2048     ; ~50% duty cycle on PWM channel 1
```

## See also

- [UserPWMDiv](UserPWMDiv.md) — PWM period / frequency
- [DOutSelect](DOutSelect.md) — route a PWM channel to an output
