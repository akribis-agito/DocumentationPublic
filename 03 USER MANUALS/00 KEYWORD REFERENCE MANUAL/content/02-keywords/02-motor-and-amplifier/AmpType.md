---
keyword: AmpType
summary: Selects how the axis drives its motor — built-in amplifier or an external amplifier via analog/digital command.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 226
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
  - 7
  default: 0
  scaling: 1.0
  implemented: partial
overrides:
  central-i.v5:
    range:
    - 0
    - 8
---
# AmpType

Selects how the axis drives its motor — built-in amplifier or an external amplifier via analog/digital command.

## Overview

`AmpType` defines the amplifier mode used by the axis. Depending on the Agito product, an axis can drive its internal PWM amplifier directly or interface with an external amplifier through an analog or digital command. The choice determines which command signal the axis produces, and which related keywords apply — for example the external analog/SPI modes use [AAmpFullScale](AAmpFullScale.md) to scale the output. Contact Agito for the amplifier functionality available on each product.

Because `AmpType` is an axis-scope parameter saved to flash, it cannot be changed while the motor is on or in motion; set it during axis configuration (typically from the PCSuite setup page), then `Save`.

> [!note] Status: partial
> The frontmatter marks `AmpType` as `partial` (current firmware range is 0–7). Mode 8 (digital SPI phase-current command) is documented below for completeness but its support is still under review.

## How it works

| AmpType | Amplifier mode |
|----|----|
| 0 | Built-in PWM amplifier |
| 1 | Reserved |
| 2 | External amplifier — analog current reference ([CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md)) command |
| 3 | External amplifier — digital pulse-direction (PD) command |
| 4 | Reserved (built-in linear amplifier) |
| 5 | External amplifier — analog velocity reference ([VelRef](../10-motion/01-kinematics-status/VelRef.md)) command |
| 6 | External amplifier — digital pulse-direction (PD) command with position feedback |
| 7 | External amplifier — analog phase current reference ([IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)) command |
| 8 | External amplifier — digital SPI phase current reference (IaRef/IbRef) command |

## Examples

```text
AAmpType=0           ; use the built-in PWM amplifier
AAmpType=2           ; external amplifier, analog current-reference command
AAmpType            ; query the current amplifier mode
```

## See also

- [AAmpFullScale](AAmpFullScale.md) — full-scale output scaling for external analog/SPI modes (2, 5, 7, 8)
- [LAmpFullScale](LAmpFullScale.md) — full-scale selection for the built-in linear amplifier (mode 4)
- [MotorType](MotorType.md) — type of motor connected to the amplifier
