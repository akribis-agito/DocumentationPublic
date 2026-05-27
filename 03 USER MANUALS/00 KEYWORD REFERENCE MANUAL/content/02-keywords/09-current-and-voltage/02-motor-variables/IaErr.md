---
keyword: IaErr
summary: Read-only phase A current error (IaRef − Ia), in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 20
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
---
# IaErr

Read-only phase A current error (IaRef − Ia), in milliamperes.

## Overview

`IaErr` is the calculated phase A current error, in milliamperes — the difference between the phase A reference [IaRef](IaRef.md) and the measured phase A current [Ia](Ia.md). It is used in single-phase (brush) motor current control, three-phase abc-domain current control (when [ControlMode](ControlMode.md) bit 1 is set) and stepper phase current control.

## How it works

$$
IaErr\ \lbrack mA\rbrack\  = \ IaRef\ \lbrack mA\rbrack\  - \ Ia\ \lbrack mA\rbrack
$$

Where the phase A current loop is active, `IaErr` is the input to the phase A PI controller: it is integrated with the integral gain ([CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)) and summed with the proportional term scaled by the loop gain ([CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)) to produce the phase A voltage command [Va](Va.md). For brushless motors run in dq0 (vector) mode the loop instead acts on [IqErr](IqErr.md)/[IdErr](IdErr.md), and `IaErr` is still computed for monitoring.

## Examples

```text
AIaErr              ; read phase A current error (mA)
```

## See also

- [IaRef](IaRef.md) — phase A current reference
- [Ia](Ia.md) — measured phase A current
- [IbErr](IbErr.md) — phase B current error
- [Va](Va.md) — phase A voltage command produced from this error by the PI loop
