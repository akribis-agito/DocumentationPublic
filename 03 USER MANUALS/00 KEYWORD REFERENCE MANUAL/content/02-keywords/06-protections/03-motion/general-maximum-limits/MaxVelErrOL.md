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

`MaxVelErrOL` and `MaxVelErr` feed the **same** velocity-error check. The loop state selects which one is active by switching the threshold and recording whether open-loop limiting is in effect:

| Condition | Active threshold | Open-loop limiting |
|-----------|------------------|--------------------|
| Open-loop mode on (`OpenLoopOn`) | `MaxVelErrOL` | yes |
| Injection at CurrRef / ForceRef point | `MaxVelErrOL` (CurrRef) | yes (CurrRef) |
| Injection at VelRef / PosRef point | `MaxVelErr` | no |
| Normal closed loop | `MaxVelErr` | no |

When the loop finds the velocity error exceeds the active threshold, the open-loop flag decides the fault: open-loop → [ConFlt](../../../07-status-and-faults/ConFlt.md) fault code 1056 (open-loop velocity error too high); closed-loop → fault code 1021 (velocity error too high). The axis is turned off immediately. As with the closed-loop check, the protection is active only in Position/Velocity/force-over-PIV operation and is bypassed for velocity-command (analog) amplifiers. On return to normal operation the active threshold is restored to `MaxVelErr`.

![Following-error trip threshold: the absolute error rises until it crosses the active limit; on that sample the axis is disabled and a ConFlt code is logged. The open-loop limits are higher to tolerate the larger natural error during injection or open-loop operation.](following-error-trip.svg)

## Examples

```text
AMaxVelErrOL[1]=20000000   ; max open-loop velocity error (user units/s)
AMaxVelErrOL[1]            ; read back the limit
```

## See also

- [MaxVelErr](MaxVelErr.md) — closed-loop velocity-error limit (the alternate threshold)
- [MaxPosErrOL](MaxPosErrOL.md) — open-loop position-error limit
- [VelErr](../../../10-motion/01-kinematics-status/VelErr.md) — the measured error this limit acts on
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1056 (open-loop velocity error too high)
