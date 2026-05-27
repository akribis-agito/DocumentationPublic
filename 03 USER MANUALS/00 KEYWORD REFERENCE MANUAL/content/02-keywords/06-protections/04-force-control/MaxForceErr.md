---
keyword: MaxForceErr
summary: Maximum allowable force error in closed-loop force control; exceeding it faults.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 585
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
  - 327680
  default: 2000
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxForceErr

Maximum allowable force error in closed-loop force control; exceeding it faults.

## Overview

`MaxForceErr` is the maximum allowable force error in **closed-loop** force-control mode. If the magnitude of the force error (commanded − measured force) exceeds this threshold, the controller disables the axis with a fault. It is axis-scoped, saved to flash, and may be changed at any time including during motion (range 0…327680, default 2000). For the open-loop equivalent, see [MaxForceErrOL](MaxForceErrOL.md).

## How it works

In the force control loop the firmware forms the force error from the filtered force reference and the measured force, then tests its absolute value against an **internal** limit:

```text
ForceErr = ForceRefFiltered − Force
if (|ForceErr| > MaxForceErrInternal)
    → disable axis, append to ErrLog
```

(Firmware: `AG300_CTL01ControlLoops.c:2812`–`:2824`, and the PIV-loop variant at `:2915`–`:2925`.) The fault code raised depends on whether the loop is currently closed or open (selected by the `gsMaxErrStat` flags):

| Situation | Internal limit used | ConFlt raised |
|-----------|---------------------|---------------|
| Closed-loop force control | `MaxForceErr` | **1045** — `CON_FLT_HIGH_FORCE_ERR` |
| Open-loop / injection at the force reference | [MaxForceErrOL](MaxForceErrOL.md) | 1057 — `CON_FLT_HIGH_FORCE_ERR_OL` |

The active value `MaxForceErrInternal` is set to `MaxForceErr` for normal closed-loop operation and switched to [MaxForceErrOL](MaxForceErrOL.md) when open-loop or signal injection is engaged at the force-reference point (`SpecialFuncs.c:5654` `SpOpenLoop`; `AG300_CTL01ControlLoops.c:2649`). Separately, if no analog force feedback is defined the loop faults with `1046` (`CON_FLT_NO_FORCE_FEEDBACK`).

## Examples

```text
AMaxForceErr[1]=2000   ; trip axis A if closed-loop force error exceeds 2000
AMaxForceErr           ; read the current limit
```

## See also

- [MaxForceErrOL](MaxForceErrOL.md) — open-loop force-error limit
- [ForceErr](../../08-axis-operation/04-force-operation-mode/ForceErr.md) — the live force error being limited
- [ConFlt](../../07-status-and-faults/ConFlt.md) — fault code 1045 (force error exceeds limit)
