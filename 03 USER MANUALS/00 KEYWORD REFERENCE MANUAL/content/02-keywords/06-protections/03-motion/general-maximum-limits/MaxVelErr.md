---
keyword: MaxVelErr
summary: Maximum closed-loop velocity error; exceeding it disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 85
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
  default: 32768
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MaxVelErr

Maximum closed-loop velocity error; exceeding it disables the axis.

## Overview

`MaxVelErr` is the maximum allowable absolute velocity error ([VelErr](../../../10-motion/01-kinematics-status/VelErr.md)) in closed-loop operation. If `|VelErr|` exceeds the active threshold, the axis is disabled in the same control sample and a fault is recorded in [ConFlt](../../../07-status-and-faults/ConFlt.md). For the open-loop equivalent used during injection/open-loop, see [MaxVelErrOL](MaxVelErrOL.md).

## How it works

The check runs every control sample in the velocity loop:

```text
if (mode is position-control, velocity-control, or force-over-PIV)
   and |VelErr| > active threshold
    turn the axis off and log the fault   (skipped for velocity-command amplifiers)
```

![Following-error trip threshold: the absolute error rises until it crosses the active limit; on that sample the axis is disabled and a ConFlt code is logged. The open-loop limits are higher to tolerate the larger natural error during injection or open-loop operation.](following-error-trip.svg)

Key points:

- The threshold actually used is switched between `MaxVelErr` (closed loop) and [MaxVelErrOL](MaxVelErrOL.md) (open loop / injection) depending on the loop state. In closed loop, a violation records [ConFlt](../../../07-status-and-faults/ConFlt.md) ConFlt code 1021 (velocity error too high); in open loop, it records ConFlt code 1056 (open-loop velocity error too high). See [MaxVelErrOL](MaxVelErrOL.md) for the full table of which condition selects which threshold.
- The protection is active **only** in position-control, velocity-control, or force-over-PIV operation. In other modes the velocity error is forced to `0`, so the check cannot trip.
- It is **bypassed for velocity-command (analog) amplifiers** ([AmpType](../../../02-motor-and-amplifier/AmpType.md) = analog velocity command), because the external drive closes its own velocity loop.
- On a violation the axis is turned off immediately.

### Edge cases

- **Motor off:** the velocity loop and the limit check do not run; `VelErr` is reset to `0` on motor-off.
- **Mode dependency:** `VelErr` is forced to `0` outside position-control, velocity-control, and force-over-PIV operation, so the trip cannot fire in those modes — including current-control-only and force-control-only.
- **AMP_TYPE bypass:** the trip is skipped entirely when [AmpType](../../../02-motor-and-amplifier/AmpType.md) is the analog-velocity-command (external velocity-loop) amplifier — the drive does not check its own follower's velocity error.
- **Stepper open loop:** `VelErr` is forced to `0` for [MotorType](../../../02-motor-and-amplifier/MotorType.md) = stepper open-loop.
- **Open-loop / injection:** during [OpenLoopOn](../../../08-axis-operation/01-general-keywords/OpenLoopOn.md) ≠ 0, or direct injection at the current-reference or force-reference point, the active limit becomes [MaxVelErrOL](MaxVelErrOL.md) and the fault becomes ConFlt code 1056. Injection at the velocity- or position-reference point keeps the limit on `MaxVelErr`.
- **Range overflow:** writes outside `0…1300000000` (v4) are clamped; the internal limit in force is updated on the next change to `MaxVelErr`/`MaxVelErrOL`/`OpenLoopOn`/`InjectType`/`InjectPoint`.
- **Clearing the fault:** ConFlt code 1021 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the following-error trip is not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

## Examples

```text
AMaxVelErr[1]=100000   ; max velocity error (user units/s)
AMaxVelErr[1]          ; read back the limit
```

## See also

- [VelErr](../../../10-motion/01-kinematics-status/VelErr.md) — the measured velocity error this limit acts on
- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit (the alternate threshold)
- [MaxPosErr](MaxPosErr.md) — companion position-following-error limit (see its walk-through; same trip pattern)
- [VelRef](../../../10-motion/01-kinematics-status/VelRef.md) / [Vel](../../../10-motion/01-kinematics-status/Vel.md) — operands of `VelErr`
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1021 (closed loop) / 1056 (open loop)
- [MotionReason](../../../10-motion/05-motion-status/MotionReason.md) — records reason 8 (motor disabled) when this trip fires
