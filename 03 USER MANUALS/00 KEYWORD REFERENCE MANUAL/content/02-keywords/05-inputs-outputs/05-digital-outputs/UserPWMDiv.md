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
  scope: non-axis
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
overrides:
  central-i.v4:
    scope: axis
  central-i.v5:
    scope: axis
---
# UserPWMDiv

Period divisor setting the PWM frequency for all user PWM channels.

## Overview

`UserPWMDiv` sets the period divisor for the user PWM outputs, which fixes the PWM frequency shared by **both** channels defined in [UserPWM](UserPWM.md). A higher value lengthens the period, producing a **lower** PWM frequency; a lower value shortens it for a higher frequency. The range is `0`–`15` and the default is `9`. Saved to flash.

## How it works

The PWM timebase is generated in hardware. When you write `UserPWMDiv` (or [UserPWM](UserPWM.md)), the new divisor is applied — directly on a standalone controller, or by sending it to the remote unit on central-i. The hardware then divides its internal clock by this value to set the PWM period, so the divisor scales the period monotonically: larger divisor → longer period → lower frequency. The exact frequency for a given divisor is fixed by the hardware clock and is product-specific; consult the product manual for the resulting frequencies.

Because the divisor sets the shared timebase, it applies to both UserPWM channels at once — you cannot give the two channels different frequencies, only different duty cycles. Changing the divisor does not change the duty *fraction* (the 0–4095 [UserPWM](UserPWM.md) value), only the period over which that fraction is measured.

## Examples

```text
AUserPWMDiv=9        ; default period divisor
AUserPWMDiv=4        ; smaller divisor → shorter period → higher PWM frequency
AUserPWMDiv          ; read the present divisor
```

### Edge cases

- **Out of range** — values outside `0`–`15` are rejected.
- **Shared timebase** — applies to both [UserPWM](UserPWM.md) channels at once; no per-channel frequency.
- **Duty preserved** — changing the divisor preserves the `0–4095` duty fraction but rescales the on-time accordingly.
- **Motor on/off** — independent of `MotorOn`.
- **Save** — flash-saveable; reapplied at boot.

## See also

- [UserPWM](UserPWM.md) — per-channel duty cycle (the fraction this period applies to)
- [DOutSelect](DOutSelect.md) — route a PWM channel to an output
