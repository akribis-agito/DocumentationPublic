---
keyword: MotTorqConst
summary: Motor torque constant for rotary and DC-brush motors.
availability:
  standalone: []
  central-i:
  - v5
can_code: 870
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
  default: 1
  scaling: 1
  implemented: final
last_updated: '2026-07-30'
doc_revision: '2026.07'
---

# MotTorqConst

Motor torque constant for rotary and DC-brush motors.

## Overview

`MotTorqConst` is the torque the motor produces per amp of current, taken from the motor data sheet. It is the **rotary** counterpart of [MotForceConst](MotForceConst.md); only one of the two applies to any given axis, selected by [MotorType](MotorType.md).

## How it works

For a rotary or DC-brush motor the magnet flux linkage is derived as:

```text
psi_f = (2/3) * MotTorqConst / PolePairs
```

Every field-weakening constant — characteristic current, demagnetising limit, normalised gains — follows from `psi_f`.

> **Important:** [PolePrs](PolePrs.md) must be correct for this derivation to be right. An incorrect pole-pair count scales the flux linkage directly and every dependent constant with it.

### Edge cases

- **Motor type:** ignored unless [MotorType](MotorType.md) selects a rotary or DC-brush motor.
- **Neither set:** if the motor type matches neither arm, the flux linkage is zero and field weakening stays inactive by construction — no special-case handling is needed.
- **Not settable in motion.**

## Examples

```text
AMotTorqConst=0.36    ; 0.36 N.m per amp
```

## See also

- [MotForceConst](MotForceConst.md) — the linear equivalent
