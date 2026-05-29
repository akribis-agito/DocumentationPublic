---
keyword: CurrFBFact
summary: Scale factor (micro-units) mapping a remote analog current-sense input to motor current, for the linear-adapter remote amplifier.
availability:
  standalone: []
  central-i:
  - v4
can_code: 649
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
  - -2147483648
  - 2147483647
  default: -1907500
  scaling: 1.0
  implemented: final
overrides: {}
---
# CurrFBFact

Scale factor (micro-units) mapping a remote analog current-sense input to motor current, for the linear-adapter remote amplifier.

## Overview

`CurrFBFact` sets the current-feedback scaling used when a Central-i master drives a remote **linear-adapter** amplifier that reports motor current through an analog current-sense input. It converts the raw analog current-feedback reading from that remote into the motor current the control loop works with, and includes the sign so the feedback polarity is correct.

It is a per-axis parameter saved to flash. The value is interpreted with a fixed scaling of 10⁻⁶ (six decimal places), so the stored integer is one millionth of the applied factor; for example the default `-1907500` applies a factor of about `-1.9075`. The negative sign reflects the feedback polarity of the supported hardware.

> This is the v4 form of the external current-feedback scale. On v5 the equivalent setting is the floating-point [ExtCurrFBSca](ExtCurrFBSca.md).

## How it works

When the Central-i master identifies a connected linear-adapter remote amplifier ([AmpType](../../02-motor-and-amplifier/AmpType.md) set to the linear-adapter type), it loads `CurrFBFact × 10⁻⁶` as that device's current-sensing factor. From then on the remote's raw analog current reading is multiplied by this factor to produce the motor current feedback used by the current loop and reported by [MotorCurr](../02-motor-variables/MotorCurr.md).

The setting takes effect when the remote device is identified/connected, so change it before connecting the remote (or reconnect for a new value to apply). It is only used for the linear-adapter remote amplifier; other remote amplifier types report current through their own path and ignore it.

## Examples

```text
ACurrFBFact=-1907500     ; default scaling for the supported linear-adapter remote
ACurrFBFact              ; read the configured current-feedback factor
```

## See also

- [ExtCurrFBSca](ExtCurrFBSca.md) — v5 floating-point equivalent of this scale
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — amplifier type; this applies to the linear-adapter remote
- [MotorCurr](../02-motor-variables/MotorCurr.md) — motor current produced from the scaled feedback
