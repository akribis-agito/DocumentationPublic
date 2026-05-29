---
keyword: StuckCurr
summary: Current threshold for motor-stuck detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 86
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 64000
  default: 4000
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
---
# StuckCurr

Current threshold for motor-stuck detection.

## Overview

`StuckCurr` is the motor-current threshold for motor-stuck detection. A motor is "stuck" when the drive is pushing hard (current at or above `StuckCurr`) yet the motor barely moves (speed at or below [StuckVel](StuckVel.md)) — and that combination persists for [StuckTime](StuckTime.md). The default is the motor's 4 A current level. The maximum is clamped to the drive's maximum current command.

## How it works

Every control sample the firmware evaluates the stuck condition:

```text
if |Vel[3]| <= StuckVel  and  |MotorCurr| >= StuckCurr  and mode is eligible
    increment the stuck counter
    if the stuck counter has reached StuckTime
        turn the axis off and log the fault
else
    reset the stuck counter to 0
```

![Motor-stuck detection logic](stuck-logic.svg)

- The two conditions are **AND**-ed: the absolute filtered velocity `Vel[3]` must be `<= StuckVel` **and** the absolute motor current must be `>= StuckCurr`.
- While both hold, an internal counter increments once per sample; any sample that breaks the condition resets it to `0`. The fault therefore fires only on a *continuous* run of [StuckTime](StuckTime.md) samples.
- On trip, the axis is turned off and [ConFlt](../../../07-status-and-faults/ConFlt.md) records ConFlt code 1007 (motor stuck).
- Detection is **bypassed** for stepper motors, and for current-control-only ([OperationMode](../../../08-axis-operation/01-general-keywords/OperationMode.md) = current-only), force-control, commutation/auto-phasing in progress, and motor-learn modes — situations where high current at low speed is expected.
- The whole stuck check (together with the dual-stuck and overspeed checks) sits behind an outer amplifier/motor gate: it runs only when the motor is on ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1), the motor is a real motor (not a [simulation](../../../02-motor-and-amplifier/MotorType.md) motor), and the amplifier is a current-commanded amplifier — it does **not** run on a pulse-and-direction (step/direction) amplifier ([AmpType](../../../02-motor-and-amplifier/AmpType.md)). On central-i v5 the gate additionally excludes the pulse-and-direction-with-feedback amplifier. Outside this gate the internal counter is held reset.

### Edge cases

- **Motor off:** detection does not run; the internal counter is reset to `0` on motor-off, so the next motor-on starts from a clean state.
- **Mode dependency:** the bypass list (current-only, force-control, auto-phasing, motor-learn, any stepper) means stuck protection is effective only in position-control and velocity-control modes with a non-stepper motor.
- **Force over PIV:** the force-control bypass is checked against [OperationMode](../../../08-axis-operation/01-general-keywords/OperationMode.md) (force-control mode); a force-over-PIV configuration that runs in position-control mode still has stuck detection active.
- **Range overflow:** `StuckCurr` writes outside `0…64000` are clamped to the keyword `range`; on Central-i the maximum is additionally clamped to the remote amplifier's maximum current command.
- **Clearing the fault:** ConFlt code 1007 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the motor-stuck trip is not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

> **Worked example:** with `StuckCurr = 4000` (4 A), `StuckVel = 40000` (user units/s) and `StuckTime` of a few thousand samples, suppose the motor hits a hard endstop while jogging at 6 A. The current rises above 4 A and the filtered velocity collapses below 40 000; both AND conditions become true. The internal sample counter runs up, and when it reaches `StuckTime` the axis is disabled with `ConFlt = 1007`. If the obstruction releases (so the velocity rises above `StuckVel`) before the counter reaches `StuckTime`, the counter resets and no fault is raised.

## Examples

```text
AStuckCurr[1]=4000    ; current above which a non-moving motor counts as stuck
AStuckCurr[1]         ; read back the threshold
```

## See also

- [StuckVel](StuckVel.md) — velocity threshold (the other half of the AND)
- [StuckTime](StuckTime.md) — how long the condition must persist
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1007 (motor stuck)
