---
keyword: MaxPosErr
summary: Maximum closed-loop position error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 84
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 80000000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
---
# MaxPosErr

Maximum closed-loop position error; exceeding it disables the axis.

## Overview

`MaxPosErr` is the maximum allowable absolute position error ([PosErr](../../../10-motion/01-kinematics-status/PosErr.md)) in closed-loop operation. It is the primary "following error" protection: if `|PosErr|` exceeds the active threshold, the axis is disabled in the same control sample and a fault is recorded in [ConFlt](../../../07-status-and-faults/ConFlt.md). For the open-loop equivalent used during injection/open-loop, see [MaxPosErrOL](MaxPosErrOL.md).

## How it works

The check runs every control sample in the position loop (firmware `CommonC/AG300_CTL01ControlLoops.c:434`):

```c
if (labs(PosErr) > MaxPosErrInternal)
{
    if (gsMaxErrStat & 0x01) MotorOffAndAddToErrorLog(axis, CON_FLT_HIGH_POS_ERR_OL, true);
    else                     MotorOffAndAddToErrorLog(axis, CON_FLT_HIGH_POS_ERR,    true);
}
```

Key points:

- The threshold actually used is **`MaxPosErrInternal`**, not `MaxPosErr` directly. `MaxPosErrInternal` is switched between `MaxPosErr` (closed loop) and [MaxPosErrOL](MaxPosErrOL.md) (open loop / injection) by the `SpOpenLoop()` handler (`CommonC/SpecialFuncs.c:5654`). In normal closed-loop operation `MaxPosErrInternal = MaxPosErr` and `gsMaxErrStat` bit 0 is clear, so a violation raises `CON_FLT_HIGH_POS_ERR` (code `1020`). In open loop, bit 0 of `gsMaxErrStat` is set and the same condition instead raises `CON_FLT_HIGH_POS_ERR_OL` (code `1055`).
- `PosErr` is forced to `0` (so this protection never trips) for an open-loop stepper, and whenever the axis is not in a position-control / force-over-PIV mode (`AG300_CTL01ControlLoops.c:427`). The protection is therefore effective only when a position loop is actually closed.
- On a violation the axis is turned off immediately (`MotorOffAndAddToErrorLog`), and the fault's configured stop behaviour applies.

## Examples

```text
AMaxPosErr[1]=5000    ; max following error (user units)
AMaxPosErr[1]         ; read back the limit
```

## See also

- [PosErr](../../../10-motion/01-kinematics-status/PosErr.md) — the measured position error this limit acts on
- [MaxPosErrOL](MaxPosErrOL.md) — open-loop position-error limit (the alternate threshold)
- [MaxVelErr](MaxVelErr.md) — companion velocity-following-error limit
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records `CON_FLT_HIGH_POS_ERR` (1020) / `..._OL` (1055)
