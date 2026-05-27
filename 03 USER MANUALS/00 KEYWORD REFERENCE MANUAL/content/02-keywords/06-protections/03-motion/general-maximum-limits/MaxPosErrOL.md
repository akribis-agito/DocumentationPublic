---
keyword: MaxPosErrOL
summary: Maximum open-loop (injection) position error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 388
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
  - 1500000000
  default: 1000000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MaxPosErrOL

Maximum open-loop (injection) position error; exceeding it disables the axis.

## Overview

`MaxPosErrOL` is the maximum allowable absolute position error ([PosErr](../../../10-motion/01-kinematics-status/PosErr.md)) while the axis is in **open-loop** operation — either open-loop mode or during direct [injection](../../../13-injection/00-overview.md). It is the open-loop counterpart of [MaxPosErr](MaxPosErr.md); open-loop position error is naturally much larger, which is why a separate (and by default much larger) limit exists.

## How it works

`MaxPosErrOL` and `MaxPosErr` feed the **same** position-error check in the control loop (`CommonC/AG300_CTL01ControlLoops.c:434`). Which one is in force at any instant is selected by the `SpOpenLoop()` handler (`CommonC/SpecialFuncs.c:5654`), which copies the chosen limit into the internal working variable `MaxPosErrInternal` and sets a flag bit in `gsMaxErrStat`:

| Condition | `MaxPosErrInternal` set to | `gsMaxErrStat` bit 0 |
|-----------|----------------------------|----------------------|
| Open-loop mode on (`OpenLoopOn`) | `MaxPosErrOL` | set |
| Injection at CurrRef or ForceRef point | `MaxPosErrOL` | set |
| Injection at VelRef / PosRef point | `MaxPosErr` | not set (PosRef) / set per case |
| Normal closed loop | `MaxPosErr` | clear |

When the loop later finds `|PosErr| > MaxPosErrInternal`, bit 0 of `gsMaxErrStat` decides which fault is logged: set → `CON_FLT_HIGH_POS_ERR_OL` (code `1055`); clear → `CON_FLT_HIGH_POS_ERR` (code `1020`). Either way the axis is turned off immediately. On returning to normal operation (or when the motor goes off during injection), `MaxPosErrInternal` is restored to `MaxPosErr` and `gsMaxErrStat` is cleared (`AG300_CTL01ControlLoops.c:2647`).

## Examples

```text
AMaxPosErrOL[1]=1000000   ; max open-loop position error (user units)
AMaxPosErrOL[1]           ; read back the limit
```

## See also

- [MaxPosErr](MaxPosErr.md) — closed-loop position-error limit (the alternate threshold)
- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit
- [PosErr](../../../10-motion/01-kinematics-status/PosErr.md) — the measured error this limit acts on
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records `CON_FLT_HIGH_POS_ERR_OL` (1055)
