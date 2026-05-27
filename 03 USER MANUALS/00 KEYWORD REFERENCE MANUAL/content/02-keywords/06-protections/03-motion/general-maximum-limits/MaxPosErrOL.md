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

`MaxPosErrOL` and `MaxPosErr` feed the **same** position-error check in the control loop. Which one is in force at any instant is selected by the loop state, which switches the active threshold and records whether open-loop limiting is in effect:

| Condition | Active threshold | Open-loop limiting |
|-----------|------------------|--------------------|
| Open-loop mode on (`OpenLoopOn`) | `MaxPosErrOL` | yes |
| Injection at CurrRef or ForceRef point | `MaxPosErrOL` | yes |
| Injection at VelRef / PosRef point | `MaxPosErr` | no (PosRef) / per case |
| Normal closed loop | `MaxPosErr` | no |

When the loop later finds the position error exceeds the active threshold, the open-loop flag decides which fault is logged: open-loop → [ConFlt](../../../07-status-and-faults/ConFlt.md) fault code 1055 (open-loop position error too high); closed-loop → fault code 1020 (position error too high). Either way the axis is turned off immediately. On returning to normal operation (or when the motor goes off during injection), the active threshold is restored to `MaxPosErr` and the open-loop flag is cleared.

## Examples

```text
AMaxPosErrOL[1]=1000000   ; max open-loop position error (user units)
AMaxPosErrOL[1]           ; read back the limit
```

## See also

- [MaxPosErr](MaxPosErr.md) — closed-loop position-error limit (the alternate threshold)
- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit
- [PosErr](../../../10-motion/01-kinematics-status/PosErr.md) — the measured error this limit acts on
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1055 (open-loop position error too high)
