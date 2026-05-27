---
keyword: IbErr
summary: Read-only phase B current error (IbRef − Ib), in milliamperes.
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# IbErr

Read-only phase B current error (IbRef − Ib), in milliamperes.

## Overview

`IbErr` is the calculated phase B current error, in milliamperes — the difference between the phase B reference [IbRef](IbRef.md) and the measured phase B current [Ib](Ib.md). It is used in three-phase abc-domain current control and stepper phase current control.

## How it works

$$
IbErr\ \lbrack mA\rbrack\  = \ IbRef\ \lbrack mA\rbrack\  - \ Ib\ \lbrack mA\rbrack
$$

## Examples

```text
IbErr?              ; read phase B current error (mA)
```

## See also

- [IbRef](IbRef.md) — phase B current reference
- [Ib](Ib.md) — measured phase B current
- [IaErr](IaErr.md) — phase A current error
