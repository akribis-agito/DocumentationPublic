---
keyword: MaxMotorCurr
summary: Hard limit on motor current; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# MaxMotorCurr

Hard limit on motor current; exceeding it disables the axis.

## Overview

`MaxMotorCurr` is the maximum allowable motor current (`MotorCurr`), in mA. Unlike the I²t scheme (which *limits* sustained current), this is a fast over-current **trip**: if exceeded, the axis is disabled and a fault is raised.

> **Note:** for a three-phase motor, `MotorCurr` is the amplitude of the motor-current phasor.

## How it works

Every control cycle the drive compares `|MotorCurr|` against `MaxMotorCurr` and runs a debounce counter:

- If `|MotorCurr| > MaxMotorCurr`, an over-current counter increments; otherwise it resets to 0.
- When the counter reaches **4 consecutive samples (≈ 0.25 ms)**, the axis is disabled and [ConFlt](../../07-status-and-faults/ConFlt.md) shows fault code 1016 (motor current too high), with a snapshot and an [ErrLog](../../07-status-and-faults/ErrLog.md) entry.

The short 4-sample window rejects single-cycle measurement spikes while still tripping quickly on a genuine over-current. Because it monitors the total motor current, use [MaxPhaseCurr](MaxPhaseCurr.md) in addition to catch per-phase faults (e.g. stalls) where the total may look acceptable.

## Changes between versions

In **v4** `MaxMotorCurr` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The over-current trip mechanism is unchanged.

## Examples

```text
AMaxMotorCurr=50000  ; trip if motor current exceeds 50 A (mA units)
```

## See also

- [MaxPhaseCurr](MaxPhaseCurr.md) — per-phase over-current trip
- [PeakCL](PeakCL.md) / [ContCL](ContCL.md) — current limiting (vs tripping)
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault 1016 raised on trip
