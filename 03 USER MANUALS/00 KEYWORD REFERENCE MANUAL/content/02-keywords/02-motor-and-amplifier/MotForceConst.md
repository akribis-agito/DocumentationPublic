---
keyword: MotForceConst
summary: Motor force constant for linear and voice-coil motors, in N per amp RMS.
availability:
- controller
- ci-master
can_code: 871
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
  default: 10.0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-07-30'
doc_revision: '2026.09'
---

# MotForceConst

Motor force constant for linear and voice-coil motors, in N per amp RMS.

## Overview

`MotForceConst` is the force the motor produces per amp RMS of phase current, as the motor data sheet gives it (N/Arms). It is the **linear-motor** counterpart of [MotTorqConst](MotTorqConst.md); only one of the two applies to any given axis, selected by [MotorType](MotorType.md).

The drive uses it, together with [MagneticPitch](MagneticPitch.md), to derive the magnet flux linkage that every field-weakening constant depends on. The enhanced PTP profiler (Central-i master) uses it to bound the acceleration a linear brushless motor can deliver, and the load estimator (AGM800 / AGM800-EC) uses it to turn the moving mass into a current.

## How it works

The drive's phase currents are peak amplitudes, so on a 3-phase linear brushless motor it divides the RMS constant by √2 before use. A voice coil carries DC, where RMS equals peak, and its constant is used as entered:

```text
Kf_peak = MotForceConst / sqrt(2)    ; linear brushless (MotorType 3)
Kf_peak = MotForceConst              ; voice coil (MotorType 2)
psi_f   = 1.061032954e-4 * Kf_peak * MagneticPitch
```

From `psi_f` the drive computes the characteristic current, the demagnetising current limit, and the normalised field-weakening gains.

> **Important:** this makes `MotForceConst` a **precondition** for field weakening on a linear motor, not an optional refinement. Left at its default, the product above is meaningless, the characteristic current collapses, and the field-weakening outer loop stays inactive no matter what [FieldWeakEn](../09-current-and-voltage/03-current-compensation/FieldWeakEn.md) is set to.

> **Worked example:** an AKM100-B1 has a data-sheet force constant of 76.5 N/Arms and an electrical cycle of 42 mm. Setting `MotForceConst=76.5` and `MagneticPitch=42` gives a flux linkage of 0.241 Wb, which agrees with the data sheet's back-EMF constant of 62.5 Vpeak/(m/s). With the 29 mH phase inductance the characteristic current is 8.3 A peak. The characteristic current being *below* the motor's 14.4 Arms peak rating (20.4 A peak) is the classic indication that a machine is worth field-weakening at all.

### Edge cases

- **Units:** N per amp **RMS**, the usual data-sheet convention. Enter the data-sheet value as it stands. A value worked out for older firmware as per peak amp (the data-sheet value divided by √2) is now √2 too low on a linear brushless motor: re-enter the data-sheet value.
- **Motor type:** ignored unless [MotorType](MotorType.md) selects a linear or voice-coil motor. Rotary machines use [MotTorqConst](MotTorqConst.md).
- **Zero:** a value of 0 leaves the enhanced PTP profiler disarmed and field weakening inactive. The default, 10.0, is not the motor's constant: set the real one.
- **Replaces TorqueConst:** the enhanced PTP profiler's separate `TorqueConst` (CAN 864) is retired; the profiler reads this keyword on a linear motor. A `TorqueConst` value saved by older firmware is ignored.
- **Not settable in motion:** changing it re-derives every dependent constant, so it is rejected while the axis is moving.

## Examples

```text
AMotForceConst=76.5   ; AKM100-B1, N per amp RMS from the data sheet
AMagneticPitch=42     ; must be set as well
```

## See also

- [MotTorqConst](MotTorqConst.md) — the rotary equivalent
- [MagneticPitch](MagneticPitch.md) — the other half of the flux-linkage derivation
