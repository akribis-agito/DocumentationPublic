---
keyword: UserPWMDiv
summary: Period divisor setting the PWM frequency for all user PWM channels.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

`UserPWMDiv` sets the period divisor for the user PWM outputs, which fixes the PWM frequency shared by **both** channels defined in [UserPWM](UserPWM.md). A higher value lengthens the period, producing a **lower** PWM frequency; a lower value shortens it for a higher frequency. The range is `0`–`15` and the default is `9`. Saved to flash.

## How it works

The PWM timebase is generated in the FPGA. When you write `UserPWMDiv` (or [UserPWM](UserPWM.md)), the firmware writes the new divisor to the FPGA's PWM-divider register — directly on a standalone controller, or by sending it to the remote unit on central-i. The FPGA then divides its internal clock by this value to set the PWM period, so the divisor scales the period monotonically: larger divisor → longer period → lower frequency. The exact frequency for a given divisor is fixed by the FPGA clock and is product-specific; consult the product manual for the resulting frequencies.

Because the divisor sets the shared timebase, it applies to both UserPWM channels at once — you cannot give the two channels different frequencies, only different duty cycles. Changing the divisor does not change the duty *fraction* (the 0–4095 [UserPWM](UserPWM.md) value), only the period over which that fraction is measured.

## Examples

```text
AUserPWMDiv=9        ; default period divisor
AUserPWMDiv=4        ; smaller divisor → shorter period → higher PWM frequency
AUserPWMDiv          ; read the present divisor
```

## See also

- [UserPWM](UserPWM.md) — per-channel duty cycle (the fraction this period applies to)
- [DOutSelect](DOutSelect.md) — route a PWM channel to an output
