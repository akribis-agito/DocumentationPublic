---
keyword: MaxVelErrOL
summary: Maximum open-loop (injection) velocity error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 389
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
  - 1300000000
  default: 20000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
---
# MaxVelErrOL

Maximum open-loop (injection) velocity error; exceeding it disables the axis.

## Overview

`MaxVelErrOL` is the maximum allowable absolute velocity error ([VelErr](../../../10-motion/01-kinematics-status/VelErr.md)) while the axis is in **open-loop** operation — open-loop mode or direct [injection](../../../13-injection/00-overview.md). It is the open-loop counterpart of [MaxVelErr](MaxVelErr.md), and is by default much larger because open-loop velocity error is naturally large.

## How it works

`MaxVelErrOL` and `MaxVelErr` feed the **same** velocity-error check (`CommonC/AG300_CTL01ControlLoops.c:670`). The `SpOpenLoop()` handler (`CommonC/SpecialFuncs.c:5654`) selects which one is active by copying it into the working variable `MaxVelErrInternal` and setting bit 1 of `gsMaxErrStat`:

| Condition | `MaxVelErrInternal` set to | `gsMaxErrStat` bit 1 |
|-----------|----------------------------|----------------------|
| Open-loop mode on (`OpenLoopOn`) | `MaxVelErrOL` | set |
| Injection at CurrRef / ForceRef point | `MaxVelErrOL` (CurrRef) | set (CurrRef) |
| Injection at VelRef / PosRef point | `MaxVelErr` | clear |
| Normal closed loop | `MaxVelErr` | clear |

When the loop finds `|VelErr| > MaxVelErrInternal`, bit 1 of `gsMaxErrStat` decides the fault: set → `CON_FLT_HIGH_VEL_ERR_OL` (code `1056`); clear → `CON_FLT_HIGH_VEL_ERR` (code `1021`). The axis is turned off immediately. As with the closed-loop check, the protection is active only in Position/Velocity/force-over-PIV operation and is bypassed for velocity-command (analog) amplifiers. On return to normal operation the internal threshold is restored to `MaxVelErr` (`AG300_CTL01ControlLoops.c:2648`).

## Examples

```text
AMaxVelErrOL[1]=20000000   ; max open-loop velocity error (user units/s)
AMaxVelErrOL[1]            ; read back the limit
```

## See also

- [MaxVelErr](MaxVelErr.md) — closed-loop velocity-error limit (the alternate threshold)
- [MaxPosErrOL](MaxPosErrOL.md) — open-loop position-error limit
- [VelErr](../../../10-motion/01-kinematics-status/VelErr.md) — the measured error this limit acts on
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records `CON_FLT_HIGH_VEL_ERR_OL` (1056)
