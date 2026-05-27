---
keyword: MaxPhaseCurr
summary: Hard limit on motor phase current; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 98
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
  - 0
  - 76000
  default: 76000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPhaseCurr

Hard limit on motor phase current; exceeding it disables the axis.

## Overview

`MaxPhaseCurr` is the maximum allowable motor **phase** current, in mA. If the absolute value of any phase current exceeds `MaxPhaseCurr` for more than 0.25 ms, the axis is disabled and an error code is reported to the fault register `ConFlt`.

> **Note:** for a single-phase motor / voice coil, `MotorCurr` is monitored. For a three-phase motor, `Ia`, `Ib`, and `Ic` are monitored (`Ic` is inferred from `Ia` and `Ib`).

## Examples

```text
AMaxPhaseCurr=50000  ; per-phase over-current trip (mA)
```

## See also

- [MaxMotorCurr](MaxMotorCurr.md) — total motor-current trip
- [PeakCL](PeakCL.md) — peak current limiting
