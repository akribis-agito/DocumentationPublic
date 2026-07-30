---
keyword: MotForceConst
summary: Motor force constant for linear and voice-coil motors, in N/A.
availability:
  standalone: []
  central-i:
  - v5
can_code: 871
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range: [0, 1000]
  default: 10
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# MotForceConst

Motor force constant for linear and voice-coil motors, in N/A.

## Overview

`MotForceConst` is the force the motor produces per amp of current, taken from the motor data sheet. It is the **linear-motor** counterpart of [MotTorqConst](MotTorqConst.md); only one of the two applies to any given axis, selected by [MotorType](MotorType.md).

The drive uses it, together with [MagneticPitch](MagneticPitch.md), to derive the magnet flux linkage that every field-weakening constant depends on.

## How it works

For a linear or voice-coil motor the flux linkage is derived as:

```text
psi_f = 1.061032954e-4 * MotForceConst * MagneticPitch
```

From `psi_f` the drive computes the characteristic current, the demagnetising current limit, and the normalised field-weakening gains.

> **Important:** this makes `MotForceConst` a **precondition** for field weakening on a linear motor, not an optional refinement. Left at its default, the product above is meaningless, the characteristic current collapses, and the field-weakening outer loop stays inactive no matter what [FieldWeakEn](../09-current-and-voltage/03-current-compensation/FieldWeakEn.md) is set to.

> **Worked example:** an AKM100-B1 has a data-sheet force constant of 76.5 N/A and an electrical cycle of 42 mm. Setting `MotForceConst=76.5` and `MagneticPitch=42` gives a flux linkage of 0.341 Wb and a characteristic current of 11.8 A. Compared against the motor's 14.4 A peak rating, the characteristic current being *below* the peak rating is the classic indication that a machine is worth field-weakening at all.

### Edge cases

- **Units:** N per amp **RMS**, matching the usual data-sheet convention.
- **Motor type:** ignored unless [MotorType](MotorType.md) selects a linear or voice-coil motor. Rotary machines use [MotTorqConst](MotTorqConst.md).
- **Not settable in motion:** changing it re-derives every dependent constant, so it is rejected while the axis is moving.

## Examples

```text
AMotForceConst=76.5   ; AKM100-B1
AMagneticPitch=42     ; must be set as well
```

## See also

- [MotTorqConst](MotTorqConst.md) — the rotary equivalent
- [MagneticPitch](MagneticPitch.md) — the other half of the flux-linkage derivation
