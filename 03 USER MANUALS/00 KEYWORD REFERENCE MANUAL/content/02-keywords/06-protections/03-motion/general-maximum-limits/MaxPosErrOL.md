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

`MaxPosErrOL` and [MaxPosErr](MaxPosErr.md) feed the **same** position-error check in the control loop. Which one is in force at any instant is selected by the loop state, which switches the active threshold and records whether open-loop limiting is in effect (the firmware uses an internal flag with bit 0 = position open-loop, bit 1 = velocity open-loop, bit 2 = force open-loop):

| Condition | Active threshold | Open-loop limiting |
|-----------|------------------|--------------------|
| Open-loop mode on ([OpenLoopOn](../../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0) | `MaxPosErrOL` | yes |
| Direct injection at current- or velocity- or force-reference point ([InjectType](../../../13-injection/InjectType.md) is a direct type; [InjectPoint](../../../13-injection/InjectPoint.md) = `0`/`1`/`3`) | `MaxPosErrOL` | yes |
| Direct injection at the position-reference point ([InjectPoint](../../../13-injection/InjectPoint.md) = `2`) | [MaxPosErr](MaxPosErr.md) | no |
| Normal closed loop | [MaxPosErr](MaxPosErr.md) | no |

Important: even a velocity-reference injection treats position as open-loop, because the closed position loop no longer drives `VelRef`. The position limit therefore swaps to `MaxPosErrOL` whenever injection runs at the current-, velocity-, **or** force-reference point — only position-reference injection (and pure closed-loop) keeps the position limit on `MaxPosErr`.

When the loop later finds the position error exceeds the active threshold, the open-loop flag decides which fault is logged: open-loop → [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt code 1055 (open-loop position error too high); closed-loop → ConFlt code 1020 (position error too high). Either way the axis is turned off immediately. On returning to normal operation (or when the motor goes off during injection), the active threshold is restored to [MaxPosErr](MaxPosErr.md) and the open-loop flag is cleared.

### Edge cases

- **Motor off:** the position loop and the limit check do not run; the error is forced to `0` on motor-off.
- **Mode dependency:** the underlying `PosErr` is forced to `0` for open-loop steppers, and in any mode that is not position-control or force-over-PIV. In those cases the check cannot trip regardless of the active threshold.
- **Requires commutation:** like the closed-loop check (see [MaxPosErr](MaxPosErr.md)), the position-error trip runs only once commutation is established ([StatReg](../../../07-status-and-faults/StatReg.md) bit 0 set), so it cannot fire on a brushless motor that has not yet completed auto-phasing.
- **Range overflow:** writes outside the keyword `range` are clamped to the range; the in-force internal limit is recomputed each time `MaxPosErrOL`/`MaxPosErr`/`OpenLoopOn`/`InjectType`/`InjectPoint` changes.
- **Clearing the fault:** ConFlt code 1055 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** open-loop following-error trips are not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

![Following-error trip threshold: the absolute error rises until it crosses the active limit; on that sample the axis is disabled and a ConFlt code is logged. The open-loop limits are higher to tolerate the larger natural error during injection or open-loop operation.](following-error-trip.svg)

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
