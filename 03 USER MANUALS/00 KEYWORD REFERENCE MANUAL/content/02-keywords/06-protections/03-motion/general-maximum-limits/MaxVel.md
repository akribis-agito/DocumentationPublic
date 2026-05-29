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

**1. Velocity-reference saturation (every control sample).** In the velocity loop the generated velocity reference is clamped to ±`MaxVel`. When clamping occurs the velocity-saturation bit of [StatReg](../../../07-status-and-faults/StatReg.md) (bit 23, `0x00800000`) is set to flag that the velocity reference was saturated.

**2. Overspeed fault trip (every control sample).** The measured feedback velocity is checked against `MaxVel` plus a 25% margin:

```text
if |Vel| > MaxVel × 1.25
    turn the axis off and log the fault
```

When exceeded, the axis is turned off immediately and [ConFlt](../../../07-status-and-faults/ConFlt.md) records fault code 1019 (velocity too high).

**3. Command-time validation.** A motion cannot be *started* in the indirect/profiled modes (Jog, PTP, PD/Gear/eCam indirect, position joystick indirect) if the commanded `Speed` exceeds `MaxVel` — `Begin` is rejected (error 271). Likewise, setting `Speed` larger than `MaxVel` while already in motion is rejected (error 269). Direct modes (e.g. pulse-and-direction direct) are not gated this way because the user drives the reference directly; for those, mechanisms 1 and 2 still apply.

## Examples

```text
AMaxVel[1]=500000     ; maximum velocity (user units/s)
AMaxVel[1]            ; read back the limit
```

## See also

- [Speed](../../../10-motion/03-kinematics-configuration/Speed.md) — commanded cruise velocity; `Begin` rejects `Speed > MaxVel` in indirect modes
- [MaxVelErr](MaxVelErr.md) — velocity-following-error trip (a different fault)
- [MaxAcc](MaxAcc.md) — acceleration limit
- [VelRef](../../../10-motion/01-kinematics-status/VelRef.md) — the signal that is saturated against `MaxVel`
- [StatReg](../../../07-status-and-faults/StatReg.md) — velocity-saturation bit (bit 23) set when the velocity reference is clamped to `MaxVel`
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1019 (velocity too high) on overspeed trip
