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

Every control sample the firmware evaluates the stuck condition (firmware `CommonC/AG300_CTL01ControlInterrupt.c:4731`):

```c
if ((labs(Vel[3]) <= StuckVel) && (MotorCurrAbs >= StuckCurr) && (mode is eligible))
{
    StuckCounter++;
    if (StuckCounter >= StuckTime)
        MotorOffAndAddToErrorLog(axis, CON_FLT_MOTOR_STUCK, true);
}
else
    StuckCounter = 0;
```

![Motor-stuck detection logic](stuck-logic.svg)

- The two conditions are **AND**-ed: the absolute filtered velocity `Vel[3]` must be `<= StuckVel` **and** the absolute motor current `MotorCurrAbs` must be `>= StuckCurr`.
- While both hold, an internal `StuckCounter` increments once per sample; any sample that breaks the condition resets it to `0`. The fault therefore fires only on a *continuous* run of `StuckTime` samples.
- On trip, the axis is turned off and `CON_FLT_MOTOR_STUCK` (code `1007`) is recorded in [ConFlt](../../../07-status-and-faults/ConFlt.md).
- Detection is **bypassed** for stepper motors, and for Current-Control-Only, Force-control, commutation/auto-phasing in progress, and motor-learn modes — situations where high current at low speed is expected.

## Examples

```text
AStuckCurr[1]=4000    ; current above which a non-moving motor counts as stuck
AStuckCurr[1]         ; read back the threshold
```

## See also

- [StuckVel](StuckVel.md) — velocity threshold (the other half of the AND)
- [StuckTime](StuckTime.md) — how long the condition must persist
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records `CON_FLT_MOTOR_STUCK` (1007)
