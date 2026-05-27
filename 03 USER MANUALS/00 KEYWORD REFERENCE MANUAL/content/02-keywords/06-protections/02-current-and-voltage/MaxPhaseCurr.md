---
keyword: MaxPhaseCurr
summary: Hard limit on motor phase current; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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
overrides:
  central-i.v5:
    data_type: float32
---
# MaxPhaseCurr

Hard limit on motor phase current; exceeding it disables the axis.

## Overview

`MaxPhaseCurr` is the maximum allowable motor **phase** current, in mA. It catches faults — such as a stall — where the individual phase current is high even though the total motor current looks acceptable.

> **Note:** for a single-phase motor / voice coil, `MotorCurr` is monitored. For a three-phase motor, `Ia`, `Ib`, and `Ic` are monitored (`Ic` is inferred from `Ia` and `Ib`).

## How it works

Every control cycle the firmware checks each phase current against `MaxPhaseCurr`, each with its own debounce counter:

- For each phase, if `|Iphase| > MaxPhaseCurr` the phase counter increments; otherwise it resets to 0.
- When any phase counter reaches **4 consecutive samples (≈ 0.25 ms)**, the axis is disabled and [ConFlt](../../07-status-and-faults/ConFlt.md) is set to the matching phase code — `1013` (`CON_FLT_PHASE_A_CURRENT`), `1014` (phase B) or `1015` (phase C) — with a snapshot and an `ErrLog` entry.

This is the per-phase counterpart of [MaxMotorCurr](MaxMotorCurr.md), which trips on the total motor current using the same 4-sample / 0.25 ms debounce.

## Changes between versions

In **v4** `MaxPhaseCurr` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The over-current trip mechanism is unchanged.

## Examples

```text
AMaxPhaseCurr=50000  ; per-phase over-current trip (mA)
```

## See also

- [MaxMotorCurr](MaxMotorCurr.md) — total motor-current trip
- [PeakCL](PeakCL.md) — peak current limiting
- [ConFlt](../../07-status-and-faults/ConFlt.md) — faults 1013/1014/1015 raised on trip
