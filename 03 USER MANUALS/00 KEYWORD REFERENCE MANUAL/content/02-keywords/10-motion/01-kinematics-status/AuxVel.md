---
keyword: AuxVel
summary: Auxiliary-encoder velocity feedback (backward-Euler derivative of AuxPos).
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 6
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: aux_user_units
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# AuxVel

Auxiliary-encoder velocity feedback (backward-Euler derivative of AuxPos).

## Overview

`AuxVel` reports the velocity of the auxiliary encoder, computed as the backward-Euler derivative of the auxiliary position feedback [AuxPos](AuxPos.md). It is expressed in auxiliary user units per second (configurable via `AuxUsrUnits`). It is the auxiliary-loop counterpart of the main velocity feedback [Vel](Vel.md).

## How it works

$$
AuxVel\  = \ \frac{AuxPos\left( 1 - z^{- 1} \right)}{T_{s}}
$$

where $T_{s}$ is the controller sampling time.

## Examples

```text
AAuxVel             ; read the auxiliary velocity
```

## See also

- [AuxPos](AuxPos.md) — auxiliary position, the source of this derivative
- [Vel](Vel.md) — main velocity feedback array
