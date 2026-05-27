---
keyword: CurrLimRev
summary: Negative current-command limit (used when CurrLimMode = 3).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 394
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
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# CurrLimRev

Negative current-command limit (used when CurrLimMode = 3).

## Overview

`CurrLimRev` defines the **negative** current-command limit (in mA), used in place of the default [PeakCL](PeakCL.md) clamp. It applies only when [CurrLimMode](CurrLimMode.md) is `3`. Give it as a positive number — it bounds the negative side, so the command is limited to −`CurrLimRev`.

## How it works

When `CurrLimMode = 3`, each control cycle the firmware clamps the current command to the asymmetric range `[−CurrLimRev, +CurrLimFwd]`. The absolute [PeakCL](PeakCL.md) clamp is still applied afterwards, so the negative limit cannot exceed `PeakCL` in magnitude. When the command is clamped, [StatReg](../../07-status-and-faults/StatReg.md) bit 21 (current saturation) is set.

The directional limits can be temporarily cancelled by a digital input configured as a torque-limit-disable function, in which case the command falls back to the `PeakCL` clamp only.

## Changes between versions

In **v4** `CurrLimRev` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The clamping mechanism is unchanged.

## Examples

```text
ACurrLimMode=3
ACurrLimRev=40000    ; magnitude of the negative current limit (mA)
```

## See also

- [CurrLimFwd](CurrLimFwd.md) — positive current-command limit
- [CurrLimMode](CurrLimMode.md) — must be 3 for this to apply
- [PeakCL](PeakCL.md) — absolute clamp still applied on top
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 21 flags current saturation
