---
keyword: ExtCurrFBSca
summary: Scale factor converting an external analog current-sense input into motor current feedback (applied to both phases).
availability:
  standalone: []
  central-i:
  - v5
can_code: 866
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -20.0
  - 20.0
  default: 0.4
  scaling: 1.0
  implemented: final
overrides: {}
---
# ExtCurrFBSca

Scale factor converting an external analog current-sense input into motor current feedback (applied to both phases).

## Overview

`ExtCurrFBSca` sets the scaling that turns an **external analog current-sense input** into the motor current feedback used by the current loop. It applies on remote products that measure motor current through an analog input, and the same factor is applied to both phase-current readings.

It is a per-axis parameter saved to flash. The value is a floating-point factor with a usable range of -20.0 to 20.0 and a default of 0.4; the sign sets the feedback polarity. Use it to match the gain (and direction) of the external current-sense path so the reported motor current matches the actual current.

> Available from v5 (Central-i) only. This is the v5 replacement for the integer [CurrFBFact](CurrFBFact.md).

## How it works

When the keyword is set, the controller loads `ExtCurrFBSca` as the current-sensing factor for the connected remote device (this applies on the remote analog-current-feedback amplifier products). The remote's raw analog current-feedback code is then multiplied by this factor to obtain the motor current feedback. A single factor is used for both phase currents, so it scales the whole external current-feedback channel uniformly. The motor current that results is what the current loop regulates and what [MotorCurr](../02-motor-variables/MotorCurr.md) reports.

The factor is applied to the relevant remote device only; products that do not use an external analog current-sense input are unaffected.

## Examples

```text
AExtCurrFBSca=0.4        ; default scaling
AExtCurrFBSca=-0.4       ; same magnitude, inverted feedback polarity
AExtCurrFBSca            ; read the configured scaling
```

## See also

- [CurrFBFact](CurrFBFact.md) — v4 integer equivalent of this scale
- [MotorCurr](../02-motor-variables/MotorCurr.md) — motor current produced from the scaled external feedback
- [AmpType](../../02-motor-and-amplifier/AmpType.md) — amplifier type of the connected remote
