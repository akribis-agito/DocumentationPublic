---
keyword: PeakCL
summary: Peak current limit, used for both current-command saturation and I²t protection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 52
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
  - 20
  - 64000
  default: 64000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# PeakCL

Peak current limit, used for both current-command saturation and I²t protection.

## Overview

`PeakCL` is the peak current limit (in mA). It serves two roles:

1. **Current-command saturation.** When the current-limit mode [CurrLimMode](CurrLimMode.md) is `0`, `PeakCL` caps the current command (`CurrRef`) symmetrically, so the absolute command never exceeds `PeakCL`. (In the other `CurrLimMode` values the directional limits are applied *first*, then this `PeakCL` bound is still applied as a final absolute clamp.)
2. **I²t upper bound.** It is the peak value in the I²t scheme together with [ContCL](ContCL.md) and [PeakTime](PeakTime.md).

## How it works

Every control cycle the firmware forms `gfLimitedPeakCL` — the effective absolute current-command limit — and applies it via `ControlLoopCurrentSaturateCurrRef()`. Normally `gfLimitedPeakCL = PeakCL`; while the [I²t](ContCL.md) limitation is engaged it drops to the effective continuous value. When the command is clamped, [StatReg](../../07-status-and-faults/StatReg.md) bit 21 (current saturation) is set.

`PeakCL` also seeds the multi-level current warnings reported in `StatReg`: the firmware precomputes 0.88·`PeakCL`, 0.92·`PeakCL` and 0.96·`PeakCL` as the low / medium / high warning thresholds.

`PeakCL` must be greater than [ContCL](ContCL.md); if `ContCL` ≥ `PeakCL` the firmware uses an effective continuous limit of `PeakCL / 2` (see [ContCL](ContCL.md)).

## Changes between versions

In **v4** `PeakCL` is a 32-bit integer; in **v5** (central-i only) it is a 32-bit float (`float32`). The saturation and I²t roles are unchanged.

## Examples

```text
APeakCL=64000        ; peak current limit (mA)
```

## See also

- [ContCL](ContCL.md) — continuous current limit (must be below PeakCL)
- [PeakTime](PeakTime.md) — time allowed at peak current
- [CurrLimMode](CurrLimMode.md) — selects how the current command is limited
- [StatReg](../../07-status-and-faults/StatReg.md) — bit 21 flags current-command saturation
