---
keyword: AAmpFullScale
summary: Full-scale command value for an external amplifier, scaling the axis command to the analog or SPI output.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 228
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
  - 100
  - 10000000
  default: 5000
  scaling: 1.0
  implemented: final
overrides: {}
---
# AAmpFullScale

Full-scale command value for an external amplifier, scaling the axis command to the analog or SPI output.

## Overview

`AAmpFullScale` sets the full-scale value used when the axis drives an **external amplifier**. It defines what command magnitude corresponds to the maximum output level, so the controller can scale its internal reference (current, velocity, or phase current) onto the physical output that the external amplifier expects.

This keyword only applies when [AmpType](AmpType.md) is 2, 5, 7, or 8 (the external analog and digital-SPI command modes). It has no effect with the built-in amplifier. Set it together with [AmpType](AmpType.md) during axis configuration; being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion.

> [!note]
> Behaviour for `AmpType = 8` is still under review (see the source marker on this keyword); the formula below is documented for the analog modes.

## How it works

The meaning and unit of `AAmpFullScale` depend on the selected [AmpType](AmpType.md):

| AmpType | AAmpFullScale meaning |
|---|---|
| 2 (Analog CurrRef command) | Full-scale current reference ([CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md)) output, in milliampere over 10 V analog output. Unit: [mA/10 V] |
| 5 (Analog VelRef command) | Full-scale velocity reference ([VelRef](../10-motion/01-kinematics-status/VelRef.md)) output, in count/s over 10 V analog output. Unit: [count/s/10 V] |
| 7 (Analog IaRef/IbRef command) | Full-scale phase current reference ([IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)) output, in milliampere over 10 V analog output. Unit: [mA/10 V] |
| 8 (Digital SPI IaRef/IbRef command) | Full-scale current reference (IaRef/IbRef) output, in milliampere over a value of 32768. Unit: [mA/32768] |

For the analog modes, the analog output port voltage is scaled from the reference value. For example, with `AmpType = 2`:

$$
AOutPort\lbrack x\rbrack = \ \frac{CurrRef}{AAmpFullScale} \bullet 10000 = \ \frac{3000}{5000} \bullet 10000 = 6000\ \lbrack mV\rbrack
$$

(here `AAmpFullScale = 5000` and `CurrRef = 3000` mA, producing 6000 mV on the [AOutPort](../05-inputs-outputs/03-analog-outputs/AOutPort.md)).

## Examples

```text
AAmpFullScale=5000      ; 5000 mA corresponds to full-scale (10 V) analog output
AAmpFullScale?          ; query the current full-scale value
```

## See also

- [AmpType](AmpType.md) — selects the external amplifier command mode this scaling applies to
- [AOutPort](../05-inputs-outputs/03-analog-outputs/AOutPort.md) — analog output port driven by the scaled command
- [CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md) — current reference scaled in modes 2 and 7
