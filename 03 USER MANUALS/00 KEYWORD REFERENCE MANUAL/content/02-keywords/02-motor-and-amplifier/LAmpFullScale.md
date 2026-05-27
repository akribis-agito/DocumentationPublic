---
keyword: LAmpFullScale
summary: Reserved selection of the full-scale current range for a specific built-in linear amplifier product.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 229
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# LAmpFullScale

Reserved selection of the full-scale current range for a specific built-in linear amplifier product.

## Overview

`LAmpFullScale` selects the full-scale current-reference range of a specific built-in **linear amplifier** product, expressed as the current that corresponds to a 10 V output. It only applies when [AmpType](AmpType.md) = 4, which is itself a reserved (linear-amplifier) setting — so on standard products this keyword has no effect.

Being axis-scope and flash-saved, it is set during configuration and cannot be changed while the motor is on or in motion.

> [!note]
> `AmpType = 4` is a reserved setting for a specific linear-amplifier product. Use this keyword only on hardware that supports it; contact Agito if unsure.

## How it works

| LAmpFullScale | Full-scale current over 10 V |
|---------------|--------------------|
| 0             | 0.4 A over 10 V    |
| 1             | 1.2 A over 10 V    |
| 2             | 3.0 A over 10 V    |

## Examples

```text
ALAmpFullScale=1     ; 1.2 A corresponds to full-scale (10 V) output
ALAmpFullScale      ; query the current selection
```

## See also

- [AmpType](AmpType.md) — must be 4 (reserved linear amplifier) for this keyword to apply
- [AAmpFullScale](AAmpFullScale.md) — full-scale scaling for external amplifier modes
