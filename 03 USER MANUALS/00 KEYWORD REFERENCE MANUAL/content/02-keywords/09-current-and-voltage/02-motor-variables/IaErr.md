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

`IaErr` is the calculated phase A current error, in milliamperes — the difference between the phase A reference [IaRef](IaRef.md) and the measured phase A current [Ia](Ia.md). It is used in single-phase motor current control, three-phase abc-domain current control and stepper phase current control.

## How it works

$$
IaErr\ \lbrack mA\rbrack\  = \ IaRef\ \lbrack mA\rbrack\  - \ Ia\ \lbrack mA\rbrack
$$

## Examples

```text
AIaErr              ; read phase A current error (mA)
```

## See also

- [IaRef](IaRef.md) — phase A current reference
- [Ia](Ia.md) — measured phase A current
- [IbErr](IbErr.md) — phase B current error
