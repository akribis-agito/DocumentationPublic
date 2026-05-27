---
keyword: Ib
summary: Read-only measured phase B current, in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 10
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
overrides: {}
---
# Ib

Read-only measured phase B current, in milliamperes.

## Overview

`Ib` reports the measured current of phase B, in milliamperes. Phase B is defined by the connection scheme in the hardware reference guide. It is the feedback counterpart of the phase B reference [IbRef](IbRef.md); their difference is the phase B current error [IbErr](IbErr.md).

## Examples

```text
AIb                 ; read measured phase B current (mA)
```

## See also

- [IbRef](IbRef.md) — phase B current reference
- [IbErr](IbErr.md) — phase B current error (IbRef − Ib)
- [Ia](Ia.md) — measured phase A current
- [MotorCurr](MotorCurr.md) — total feedback current amplitude
