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

The check runs every control sample in the velocity loop (firmware `CommonC/AG300_CTL01ControlLoops.c:670`):

```c
if (((OperationMode == POSITION_CONTROL) || (OperationMode == VELOCITY_CONTROL) || ForcePIVOn) &&
    (labs(VelErr) > MaxVelErrInternal))
{
    if (AmpType != AMP_TYPE_ANALOG_VEL_CMD)   // skipped for velocity-command amplifiers
    {
        errorCode = (gsMaxErrStat & 0x02) ? CON_FLT_HIGH_VEL_ERR_OL : CON_FLT_HIGH_VEL_ERR;
        MotorOffAndAddToErrorLog(axis, errorCode, true);
    }
}
```

Key points:

- The threshold actually used is **`MaxVelErrInternal`**, switched between `MaxVelErr` (closed loop) and [MaxVelErrOL](MaxVelErrOL.md) (open loop / injection) by the `SpOpenLoop()` handler (`CommonC/SpecialFuncs.c:5654`). In closed loop, `gsMaxErrStat` bit 1 is clear and a violation raises `CON_FLT_HIGH_VEL_ERR` (code `1021`); in open loop, bit 1 is set and it raises `CON_FLT_HIGH_VEL_ERR_OL` (code `1056`).
- The protection is active **only** in Position-control, Velocity-control, or force-over-PIV operation. In other modes `VelErr` is forced to `0`, so the check cannot trip (`AG300_CTL01ControlLoops.c:665`).
- It is **bypassed for velocity-command (analog) amplifiers** (`AmpType == AMP_TYPE_ANALOG_VEL_CMD`), because the drive closes its own velocity loop.
- On a violation the axis is turned off immediately.

## Examples

```text
AMaxVelErr[1]=100000   ; max velocity error (user units/s)
AMaxVelErr[1]          ; read back the limit
```

## See also

- [VelErr](../../../10-motion/01-kinematics-status/VelErr.md) — the measured velocity error this limit acts on
- [MaxVelErrOL](MaxVelErrOL.md) — open-loop velocity-error limit (the alternate threshold)
- [MaxPosErr](MaxPosErr.md) — companion position-following-error limit
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records `CON_FLT_HIGH_VEL_ERR` (1021) / `..._OL` (1056)
