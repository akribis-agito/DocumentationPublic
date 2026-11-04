---
keyword: CurrLimFwd
summary: Positive current-command limit (used when CurrLimMode = 3).
availability:
- controller
- ci-master
can_code: 393
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 16000
  default: 16000
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 64000
    default: 64000
  agc300-et:
    range:
    - 0
    - 4000
    default: 4000
  agc301-et:
    range:
    - 0
    - 4000
    default: 4000
  agc301-et-bioxtreme:
    range:
    - 0
    - 4000
    default: 4000
  agd200-et-2d01:
    range:
    - 0
    - 4000
    default: 4000
  agd200-et-2d02:
    range:
    - 0
    - 8000
    default: 8000
  agd301-et-2d01:
    range:
    - 0
    - 4000
    default: 4000
  agd301-et-2d02:
    range:
    - 0
    - 8000
    default: 8000
  agd301-et-2d09:
    range:
    - 0
    - 25500
    default: 25500
  agd155-af-2a06:
    range:
    - 0
    - 25500
    default: 25500
  agd155-af-2a10:
    range:
    - 0
    - 28500
    default: 28500
  agd155-ec:
    range:
    - 0
    - 25500
    default: 25500
  agd155-ec-var34:
    range:
    - 0
    - 28500
    default: 28500
  agd155-ec-var34-3:
    range:
    - 0
    - 42500
    default: 42500
  agd156-ec:
    range:
    - 0
    - 12726
    default: 12726
  agd101-ec-34a:
    range:
    - 0
    - 28280
    default: 28280
  agd101-ec-17a:
    range:
    - 0
    - 14140
    default: 14140
last_updated: '2026-05-27'
doc_revision: '2026.06'
---
# CurrLimFwd

Positive current-command limit (used when CurrLimMode = 3).

## Overview

`CurrLimFwd` defines the **positive** current-command limit (in mA), used in place of the default [PeakCL](PeakCL.md) clamp. It applies only when [CurrLimMode](CurrLimMode.md) is `3`. Give it as a positive value.

## How it works

When `CurrLimMode = 3`, each control cycle the firmware clamps the current command to the asymmetric range `[−CurrLimRev, +CurrLimFwd]` (`CurrLimFwd` bounds the positive side). The absolute [PeakCL](PeakCL.md) clamp is then still applied afterwards, so neither directional limit can exceed `PeakCL`. When the command is clamped, [StatReg](../../07-status-and-faults/StatReg.md) bit 21 (current saturation) is set.

The directional limits can be temporarily cancelled by a digital input configured as a torque-limit-disable function, in which case the command falls back to the `PeakCL` clamp only.

## Changes between versions

In **v4** `CurrLimFwd` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The clamping mechanism is unchanged.

## Examples

```text
ACurrLimMode=3
ACurrLimFwd=40000    ; positive current limit (mA)
```

## See also

- [CurrLimRev](CurrLimRev.md) — negative current-command limit
- [CurrLimMode](CurrLimMode.md) — must be 3 for this to apply
- [PeakCL](PeakCL.md) — absolute clamp still applied on top
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 21 flags current saturation
