---
keyword: StuckVel
summary: Velocity threshold for motor-stuck detection.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 87
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
  default: 40000
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckVel

Velocity threshold for motor-stuck detection.

## Overview

`StuckVel` is the velocity threshold for motor-stuck detection, in user units/s (default `40000`). It is the "barely moving" half of the stuck condition: the motor is treated as not-moving when the absolute filtered velocity is at or below `StuckVel`, while the current is at or above [StuckCurr](StuckCurr.md), continuously for [StuckTime](StuckTime.md).

## How it works

Each control sample, the firmware checks `|Vel[3]| <= StuckVel` **AND** absolute motor current `>= StuckCurr`. `Vel[3]` is the deeply filtered velocity, so brief jitter does not defeat the "stuck" test. While both conditions hold, an internal counter increments; when it reaches [StuckTime](StuckTime.md) the axis is turned off and [ConFlt](../../../07-status-and-faults/ConFlt.md) records ConFlt code 1007 (motor stuck). Any sample that breaks the condition resets the counter to zero.

![Motor-stuck detection logic](stuck-logic.svg)

Setting `StuckVel` higher makes the "not moving" test more permissive (the motor can be creeping and still count as stuck); setting it to `0` requires the motor to be essentially stationary. Detection is bypassed for stepper motors and for current-only / force-control / auto-phasing / motor-learn modes (see [StuckCurr](StuckCurr.md)).

### Edge cases

- **Motor off:** detection does not run; the internal counter is reset to `0` on motor-off.
- **Mode dependency:** same bypass list as [StuckCurr](StuckCurr.md) — effective only in position-control / velocity-control on non-stepper motors.
- **Range overflow:** writes outside `0…1300000000` are clamped to the keyword `range`.
- **Clearing the fault:** ConFlt code 1007 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the motor-stuck trip is not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

## Examples

```text
AStuckVel[1]=40000    ; stuck if velocity stays at/below this (user units/s)
AStuckVel[1]          ; read back the threshold
```

## See also

- [StuckCurr](StuckCurr.md) — current threshold (the other half of the AND); also lists the mode bypasses
- [StuckTime](StuckTime.md) — how long the condition must persist
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1007 (motor stuck)
