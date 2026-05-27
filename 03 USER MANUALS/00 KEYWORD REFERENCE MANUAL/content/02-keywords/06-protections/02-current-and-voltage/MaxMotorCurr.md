---
keyword: MaxMotorCurr
summary: Hard limit on motor current; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 99
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
# MaxMotorCurr

Hard limit on motor current; exceeding it disables the axis.

## Overview

`MaxMotorCurr` is the maximum allowable motor current (`MotorCurr`), in mA. If the absolute value of the motor current exceeds `MaxMotorCurr` for more than 0.25 ms, the axis is disabled and an error code is reported to the fault register `ConFlt`. Unlike the I²t scheme (which limits sustained current), this is an instantaneous over-current trip.

> **Note:** for a three-phase motor, `MotorCurr` is the amplitude of the motor-current phasor.

## Examples

```text
AMaxMotorCurr=50000  ; trip if motor current exceeds 50 A (mA units)
```

## See also

- [MaxPhaseCurr](MaxPhaseCurr.md) — per-phase over-current trip
- [PeakCL](PeakCL.md) / [ContCL](ContCL.md) — current limiting (vs tripping)
