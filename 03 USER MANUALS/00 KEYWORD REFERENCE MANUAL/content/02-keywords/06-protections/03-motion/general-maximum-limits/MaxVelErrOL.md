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

`MaxVelErrOL` and [MaxVelErr](MaxVelErr.md) feed the **same** velocity-error check. The loop state selects which one is active by switching the threshold and recording whether open-loop limiting is in effect (internally, bit 1 of the open-loop-status flag corresponds to velocity-error open-loop):

| Condition | Active threshold | Open-loop limiting |
|-----------|------------------|--------------------|
| Open-loop mode on ([OpenLoopOn](../../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0) | `MaxVelErrOL` | yes |
| Direct injection at the current-reference point ([InjectPoint](../../../13-injection/InjectPoint.md) = `0`) | `MaxVelErrOL` | yes |
| Direct injection at the force-reference point ([InjectPoint](../../../13-injection/InjectPoint.md) = `3`) | `MaxVelErrOL` | yes |
| Direct injection at the velocity- or position-reference point ([InjectPoint](../../../13-injection/InjectPoint.md) = `1` / `2`) | [MaxVelErr](MaxVelErr.md) | no |
| Normal closed loop | [MaxVelErr](MaxVelErr.md) | no |

Important: force-reference injection swaps velocity to `MaxVelErrOL` (even though force itself stays closed-loop), because the closed velocity loop no longer generates `CurrRef`. Velocity-reference injection keeps velocity on `MaxVelErr` — only the position limit goes open-loop in that case.

When the loop finds the velocity error exceeds the active threshold, the open-loop flag decides the fault: open-loop → [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt code 1056 (open-loop velocity error too high); closed-loop → ConFlt code 1021 (velocity error too high). The axis is turned off immediately. As with the closed-loop check, the protection is active only in position-control, velocity-control, or force-over-PIV operation, and is bypassed for velocity-command (analog) amplifiers ([AmpType](../../../02-motor-and-amplifier/AmpType.md) = analog velocity command). On return to normal operation the active threshold is restored to [MaxVelErr](MaxVelErr.md).

### Edge cases

- **Motor off:** the velocity loop and the limit check do not run; `VelErr` is reset to `0`.
- **Mode dependency:** `VelErr` is forced to `0` outside position-control, velocity-control, and force-over-PIV operation, so the check cannot trip in those modes regardless of threshold.
- **AMP_TYPE bypass:** the trip is skipped entirely when the amplifier is configured as `AMP_TYPE_ANALOG_VEL_CMD` (the external drive closes its own velocity loop).
- **Range overflow:** writes outside the keyword `range` are clamped; the active internal limit is recomputed each time `MaxVelErrOL`/`MaxVelErr`/`OpenLoopOn`/`InjectType`/`InjectPoint` changes.
- **Clearing the fault:** ConFlt code 1056 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** open-loop following-error trips are not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

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
