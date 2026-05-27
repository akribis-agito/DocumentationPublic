---
keyword: ForceErr
summary: Difference between force reference and force feedback.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 583
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
---
# ForceErr

Difference between force reference and force feedback.

## Overview

`ForceErr` is the difference between the (filtered) force reference [ForceRef](ForceRef.md) and the force feedback [Force](Force.md). It is the error signal the force control loop drives toward zero.

## How it works

`ForceErr` is recomputed every control cycle as the filtered reference minus the feedback:

$$
ForceErr\ \lbrack unit\rbrack\  = \ ForceRef\ \lbrack unit\rbrack\  - \ Force\ \lbrack unit\rbrack
$$

`ForceErr` serves two roles beyond closing the loop:

- **In-target detection.** The force in-target check compares `|ForceErr|` against [ForceInTTol](ForceInTTol.md); the axis is settled ([ForceInTStat](ForceInTStat.md) = 4) once it stays inside that window for [ForceInTTime](ForceInTTime.md).
- **High-error protection.** If `|ForceErr|` exceeds the internal maximum-force-error limit, [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1045 (force error exceeds limit) and the motor is turned off.

While the axis is not in force mode, `ForceErr` is forced to `0`.

## Examples

```text
AForceErr           ; read the current force error
```

## See also

- [ForceRef](ForceRef.md) — filtered force reference (minuend)
- [Force](Force.md) — force feedback (subtrahend)
- [ForceInTTol](ForceInTTol.md) — settling window applied to this error
- [ForceInTStat](ForceInTStat.md) — in-target status driven by this error
