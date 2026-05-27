---
keyword: IbErr
summary: Read-only phase B current error (IbRef − Ib), in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 21
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
# IbErr

Read-only phase B current error (IbRef − Ib), in milliamperes.

## Overview

`IbErr` is the calculated phase B current error, in milliamperes — the difference between the phase B reference [IbRef](IbRef.md) and the measured phase B current [Ib](Ib.md). It is used in three-phase abc-domain current control (when [ControlMode](ControlMode.md) bit 1 is set) and stepper phase current control. For single-phase (brush) motors phase B carries no current and `IbErr` stays at 0.

## How it works

$$
IbErr\ \lbrack mA\rbrack\  = \ IbRef\ \lbrack mA\rbrack\  - \ Ib\ \lbrack mA\rbrack
$$

Where the phase B current loop is active, `IbErr` is the input to the phase B PI controller: it is integrated with the integral gain ([CurrKi](../../11-control-tuning/06-current-control/CurrKi.md)) and summed with the proportional term scaled by the loop gain ([CurrGain](../../11-control-tuning/06-current-control/CurrGain.md)) to produce the phase B voltage command [Vb](Vb.md). For brushless motors run in dq0 (vector) mode the loop instead acts on [IqErr](IqErr.md)/[IdErr](IdErr.md), and `IbErr` is still computed for monitoring.

## Examples

```text
AIbErr              ; read phase B current error (mA)
```

## See also

- [IbRef](IbRef.md) — phase B current reference
- [Ib](Ib.md) — measured phase B current
- [IaErr](IaErr.md) — phase A current error
- [Vb](Vb.md) — phase B voltage command produced from this error by the PI loop
