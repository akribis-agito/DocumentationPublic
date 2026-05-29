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

### Edge cases

- **Motor off:** the overspeed trip and the saturation are both skipped (the velocity loop does not run). The validation gate at `Begin` is independent and still applies.
- **Mode dependency:** the overspeed trip operates whenever the motor is on; it does not depend on operation mode. The saturation in the velocity loop applies only when the velocity loop is running.
- **Feedback used:** the overspeed trip uses the instantaneous feedback `Vel[1]` (not the deeply filtered `Vel[3]` used by stuck detection).
- **25 % margin:** the trip threshold is `MaxVel × 10/8 = MaxVel × 1.25` (firmware uses `(MaxVel >> 3) * 10` to avoid overflow at high MaxVel values).
- **Range overflow:** writes outside `0…1300000000` (v4) are clamped; on v5 `MaxVel` is `int64` with no fixed upper bound.
- **Clearing the fault:** ConFlt code 1019 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the overspeed trip is not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

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
