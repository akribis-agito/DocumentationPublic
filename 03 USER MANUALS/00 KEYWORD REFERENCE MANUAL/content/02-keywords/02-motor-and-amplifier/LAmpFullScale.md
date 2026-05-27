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

Selecting a range does two things in firmware: it sets the analog scaling factor `10000 / FullScale[mA]` (mV per mA, so a current reference equal to full-scale gives 10 V), and it programs the linear-amplifier hardware gain bits so the amplifier's current sense matches the selected range. Lower full-scale ranges give finer current resolution; higher ranges allow more current.

| LAmpFullScale | Full-scale current over 10 V | Scaling factor |
|---------------|--------------------|----------------|
| 0             | 0.4 A over 10 V    | 10000 / 400 = 25 mV/mA |
| 1             | 1.2 A over 10 V    | 10000 / 1200 ≈ 8.33 mV/mA |
| 2             | 3.0 A over 10 V    | 10000 / 3000 ≈ 3.33 mV/mA |

The factor and gain bits are recomputed whenever `LAmpFullScale` or [AmpType](AmpType.md) changes (only while `AmpType = 4`). The linear amplifier serves two axes; the other axes' settings do not affect it.

## Examples

```text
ALAmpFullScale=1     ; 1.2 A corresponds to full-scale (10 V) output
ALAmpFullScale      ; query the current selection
```

## See also

- [AmpType](AmpType.md) — must be 4 (reserved linear amplifier) for this keyword to apply
- [AAmpFullScale](AAmpFullScale.md) — full-scale scaling for external amplifier modes
