---
keyword: Ia
summary: Read-only measured phase A current, in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 9
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
# Ia

Read-only measured phase A current, in milliamperes.

## Overview

`Ia` reports the measured current of phase A, in milliamperes. Phase A is defined by the connection scheme in the hardware reference guide. It is the feedback counterpart of the phase A reference [IaRef](IaRef.md); their difference is the phase A current error [IaErr](IaErr.md).

## Examples

```text
AIa                 ; read measured phase A current (mA)
```

## See also

- [IaRef](IaRef.md) — phase A current reference
- [IaErr](IaErr.md) — phase A current error (IaRef − Ia)
- [Ib](Ib.md) — measured phase B current
- [MotorCurr](MotorCurr.md) — total feedback current amplitude
