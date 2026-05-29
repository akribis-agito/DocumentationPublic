---
keyword: AAmpFullScale
summary: Full-scale command value for an external amplifier, scaling the axis command to the analog or SPI output.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

This keyword applies to the external/linear analog command modes of [AmpType](AmpType.md): 2 (analog current), 5 (analog velocity), and 7 (linear adapter). It has no effect with the built-in PWM amplifier; the built-in **linear** amplifier (mode 4) uses [LAmpFullScale](LAmpFullScale.md) instead. Set it together with [AmpType](AmpType.md) during axis configuration; being axis-scope and flash-saved, it cannot be changed while the motor is on or in motion.

## How it works

The firmware turns `AAmpFullScale` into a fixed scaling factor

$$
factor\ \left\lbrack \frac{mV}{mA\ or\ count/s} \right\rbrack = \frac{10000}{\text{AAmpFullScale}}
$$

so that a reference equal to `AAmpFullScale` produces exactly 10 000 mV (10 V) on the analog output. The factor is recomputed whenever [AmpType](AmpType.md) or `AAmpFullScale` changes. Each control cycle the analog output is `factor × reference`; when the motor is off the output is forced to 0.

The reference that gets scaled — and therefore the unit of `AAmpFullScale` — depends on the selected [AmpType](AmpType.md):

| AmpType | Reference scaled | AAmpFullScale unit |
|---|---|---|
| 2 (Analog current command) | Current reference ([CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md)), one channel | mA per 10 V |
| 5 (Analog velocity command) | Velocity reference ([VelRef](../10-motion/01-kinematics-status/VelRef.md)), one channel | count/s per 10 V |
| 7 (Linear adapter) | Both phase-current references ([IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)), two channels | mA per 10 V |

For example, with `AmpType = 2`, `AAmpFullScale = 5000` (mA), and a current reference of 3000 mA:

$$
AOutPort = \frac{\text{CurrRef}}{\text{AAmpFullScale}} \cdot 10000 = \frac{3000}{5000} \cdot 10000 = 6000\ \lbrack mV\rbrack
$$

producing 6000 mV on the [AOutPort](../05-inputs-outputs/03-analog-outputs/AOutPort.md). In linear-adapter mode (7) the same factor is applied independently to the two phase-current references, driving two analog channels.

### Digital SPI command (AmpType = 8, v5 central-i)

In v5, `AmpType = 8` drives a digital-SPI adapter. The controller still commutates internally and converts the same two phase-current references ([IaRef](../09-current-and-voltage/02-motor-variables/IaRef.md)/[IbRef](../09-current-and-voltage/02-motor-variables/IbRef.md)) as the linear adapter (mode 7), but emits each as a 16-bit SPI code (0…65535) instead of an analog voltage. The scaling factor uses a digital full code rather than 10 000 mV:

$$
factor\ \left\lbrack \frac{count}{mA} \right\rbrack = \frac{32768}{\text{AAmpFullScale}}
$$

The mid-code 32768 represents 0 A; a phase current is mapped to `32768 + factor × PhaseCurr` and saturated to the 0…65535 range. A phase current equal to `AAmpFullScale` therefore reaches the top of the range (a half-swing of 32768 counts above mid-code).

## Examples

```text
AAAmpFullScale=5000      ; 5000 mA corresponds to full-scale (10 V) analog output
AAAmpFullScale          ; query the current full-scale value
```

## See also

- [AmpType](AmpType.md) — selects the external amplifier command mode this scaling applies to
- [AOutPort](../05-inputs-outputs/03-analog-outputs/AOutPort.md) — analog output port driven by the scaled command
- [CurrRef](../09-current-and-voltage/02-motor-variables/CurrRef.md) — current reference scaled in modes 2 and 7
