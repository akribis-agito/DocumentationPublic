---
keyword: MaxVel
summary: Maximum closed-loop velocity; exceeding it (+25% buffer) disables the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 80
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
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
    range: null
    default: 1000000
---
# MaxVel

Maximum closed-loop velocity; exceeding it (+25% buffer) disables the axis.

## Overview

`MaxVel` is the maximum allowable velocity, in user units/s. It acts at three different points: it saturates the internally generated velocity reference, it trips an overspeed fault if the measured feedback runs away, and it is a validation gate that rejects motion commands whose planned speed would exceed it.

## How it works

**1. Velocity-reference saturation (every control sample).** In the velocity loop the generated reference `VelRef` is clamped to ±`MaxVel` (firmware `CommonC/AG300_CTL01ControlLoops.c:642`). When clamping occurs the `STAT_REG_VEL_SAT` bit (`0x00800000`) is set in [StatReg](../../../07-status-and-faults/StatReg.md) to flag that the velocity reference was saturated.

**2. Overspeed fault trip (every control sample).** The measured feedback velocity `Vel[1]` is checked against `MaxVel` plus a 25% margin (firmware `CommonC/AG300_CTL01ControlInterrupt.c:4812`):

```c
if (labs(Vel[1]) > ((MaxVel >> 3) * 10))   // (MaxVel/8)*10 = MaxVel x 1.25
    MotorOffAndAddToErrorLog(axis, CON_FLT_HIGH_VELOCITY, true);
```

`(MaxVel >> 3) * 10` is `MaxVel × 1.25` (the shift-then-multiply form avoids 32-bit overflow at very high `MaxVel`). When exceeded, the axis is turned off immediately and `CON_FLT_HIGH_VELOCITY` (code `1019`) is recorded in [ConFlt](../../../07-status-and-faults/ConFlt.md).

**3. Command-time validation.** A motion cannot be *started* in the indirect/profiled modes (Jog, PTP, PD/Gear/eCam indirect, position joystick indirect) if the commanded `Speed` exceeds `MaxVel` — `Begin` returns `MAXVEL_PROTECTION` (error 271) (firmware `CommonC/AG300_CTL01Funcs.c:959`). Likewise, setting `Speed` larger than `MaxVel` while already in motion is rejected with `SPEED_HIGHER_THAN_MAXVEL` (error 269) (`CommonC/AG300_CTL01Interpreter.c:2379`). Direct modes (e.g. pulse-and-direction direct) are not gated this way because the user drives the reference directly; for those, mechanisms 1 and 2 still apply.

## Examples

```text
AMaxVel[1]=500000     ; maximum velocity (user units/s)
AMaxVel[1]            ; read back the limit
```

## See also

- [MaxVelErr](MaxVelErr.md) — velocity-following-error trip (a different fault)
- [MaxAcc](MaxAcc.md) — acceleration limit
- [StatReg](../../../07-status-and-faults/StatReg.md) — `VEL_SAT` bit set when `VelRef` is clamped to `MaxVel`
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records `CON_FLT_HIGH_VELOCITY` (1019) on overspeed trip
