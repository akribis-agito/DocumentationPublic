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

![Sample-by-sample over-current debounce: the counter increments on each consecutive over-limit sample and resets to 0 on any below-limit sample; only 4 unbroken over-limit samples cause a trip](overcurrent-debounce.svg)

The short 4-sample window rejects single-cycle measurement spikes while still tripping quickly on a genuine over-current. Because it monitors the total motor current, use [MaxPhaseCurr](MaxPhaseCurr.md) in addition to catch per-phase faults (e.g. stalls) where the total may look acceptable.

### Edge cases

- **Motor off / non-current modes:** the over-current check runs only while the motor is on **and** the current loop is actually driving the phases — it is skipped for the simulation motor type (see [MotorType](../../02-motor-and-amplifier/MotorType.md)) and for the position-detector (PD) amplifier type (see [AmpType](../../02-motor-and-amplifier/AmpType.md)), where the current loop is bypassed. Whenever the check is skipped (motor off, simulation, or PD), the firmware resets the over-current counter, so the next time the check resumes it starts from a clean state.
- **Mode dependency:** the trip runs regardless of operation mode (it is a hardware-safety check, not a closed-loop-state check).
- **Independence from `PeakCL`/I²t:** this is an instantaneous over-current trip, not a current limit — it is independent of the [PeakCL](PeakCL.md)/[ContCL](ContCL.md) I²t scheme. A current that is *limited* by `PeakCL` will not normally reach `MaxMotorCurr`; set `MaxMotorCurr` above `PeakCL` so the trip catches only true faults.
- **Range overflow:** a write outside `0…76000` (v4) is rejected with an out-of-range error and the stored value is unchanged.
- **Clearing the fault:** ConFlt code 1016 clears on re-enable ([MotorOn](../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the over-motor-current trip is not maskable through [ProtectMask](../01-general-protection/ProtectMask.md). The separate silicon-level over-current bits in [HWProtectBits](../01-general-protection/HWProtectBits.md) (raising ConFlt code 1025 / 1036 / 1059) are likewise non-maskable — they are forced on regardless of [ProtectMask](../01-general-protection/ProtectMask.md); only the main-encoder (bit 2) and auxiliary-encoder (bit 3) protections are maskable.

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
