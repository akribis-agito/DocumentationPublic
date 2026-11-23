---
keyword: MotTorqConst
summary: Motor torque constant for rotary and DC-brush motors, in N.m per amp RMS.
availability:
- controller
- ci-master
can_code: 872
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0.0
  - 1000.0
  default: 1.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-07-30'
doc_revision: '2026.09'
---

# MotTorqConst

Motor torque constant for rotary and DC-brush motors, in N.m per amp RMS.

## Overview

`MotTorqConst` is the torque the motor produces per amp RMS of phase current, as the motor data sheet gives it (N.m/Arms). It is the **rotary** counterpart of [MotForceConst](MotForceConst.md); only one of the two applies to any given axis, selected by [MotorType](MotorType.md).

Three features read it:

- **Field weakening** derives the magnet flux linkage from it.
- **The enhanced PTP profiler** (Central-i master) uses it to bound the acceleration a rotary brushless motor can deliver.
- **The load estimator** (AGM800 / AGM800-EC) uses it to turn the motor's inertia into a current.

## How it works

The drive's phase currents are peak amplitudes, so on a 3-phase brushless motor it divides the RMS constant by √2 before use. A DC-brush motor carries DC, where RMS equals peak, and its constant is used as entered:

```text
Kt_peak = MotTorqConst / sqrt(2)     ; rotary brushless (MotorType 4)
Kt_peak = MotTorqConst               ; DC brush (MotorType 1)
psi_f   = (2/3) * Kt_peak / PolePairs
```

Every field-weakening constant — characteristic current, demagnetising limit, normalised gains — follows from `psi_f`.

> **Important:** [PolePrs](PolePrs.md) must be correct for this derivation to be right. An incorrect pole-pair count scales the flux linkage directly and every dependent constant with it.

### Edge cases

- **Units:** N.m per amp **RMS**, the usual data-sheet convention. Enter the data-sheet value as it stands. A value worked out for older firmware as per peak amp (the data-sheet value divided by √2) is now √2 too low on a brushless motor: re-enter the data-sheet value.
- **Motor type:** ignored unless [MotorType](MotorType.md) selects a rotary or DC-brush motor.
- **Neither set:** if the motor type matches neither arm, the flux linkage is zero and field weakening stays inactive by construction — no special-case handling is needed.
- **Zero:** a value of 0 leaves the enhanced PTP profiler disarmed and field weakening inactive. The default, 1.0, is not the motor's constant: set the real one.
- **Replaces TorqueConst:** the enhanced PTP profiler's separate `TorqueConst` (CAN 864) is retired; the profiler reads this keyword on a rotary motor. A `TorqueConst` value saved by older firmware is ignored.
- **Not settable in motion.**

## Examples

```text
AMotTorqConst=0.36    ; 0.36 N.m per amp RMS, from the data sheet
```

## See also

- [MotForceConst](MotForceConst.md) — the linear equivalent
