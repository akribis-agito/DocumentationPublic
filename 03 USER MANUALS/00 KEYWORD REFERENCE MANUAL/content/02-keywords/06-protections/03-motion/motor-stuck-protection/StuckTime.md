---
keyword: StuckTime
summary: Duration the stuck condition must persist before the axis is flagged stuck.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 88
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 4096
  scaling: 1.0
  implemented: final
overrides: {}
---
# StuckTime

Duration the stuck condition must persist before the axis is flagged stuck.

## Overview

`StuckTime` is how long the stuck condition must hold continuously before the motor-stuck fault fires. The stuck condition is current at or above [StuckCurr](StuckCurr.md) **and** speed at or below [StuckVel](StuckVel.md). The keyword carries a samples-to-milliseconds scaling, so the value is expressed as a time; internally it is compared against a sample counter. The default is `4096`.

## How it works

The firmware keeps an internal sample counter:

```text
increment the stuck counter
if the stuck counter has reached StuckTime
    turn the axis off and log the fault
```

- The counter increments by one each control sample for as long as the AND-ed [StuckCurr](StuckCurr.md)/[StuckVel](StuckVel.md) condition is true.
- The instant any sample breaks the condition, the counter is reset to `0`. The fault therefore requires a single unbroken run of `StuckTime`; intermittent stalls do not accumulate.
- When the counter reaches `StuckTime`, the axis is turned off and [ConFlt](../../../07-status-and-faults/ConFlt.md) records ConFlt code 1007 (motor stuck).

### Edge cases

- **Motor off:** detection does not run; the counter is reset to `0` on motor-off.
- **Mode dependency:** same bypass list as [StuckCurr](StuckCurr.md) — effective only in position-control / velocity-control on non-stepper motors.
- **`StuckTime = 0`:** the counter reaches the limit on the first sample where the condition is true, so the protection trips immediately (no debouncing).
- **Range overflow:** writes outside `0…2147483647` are clamped to the keyword `range`.
- **Clearing the fault:** ConFlt code 1007 clears on re-enable ([MotorOn](../../../08-axis-operation/01-general-keywords/MotorOn.md) = 1) or by writing `AConFlt=0`; the [ErrLog](../../../07-status-and-faults/ErrLog.md) entry persists.
- **HWProtectBits / ProtectMask:** the motor-stuck trip is not maskable through [ProtectMask](../../01-general-protection/ProtectMask.md) (that mask covers hardware-protection bits only).

![Motor-stuck detection logic](stuck-logic.svg)

The control loop runs at a fixed sample rate, so larger `StuckTime` tolerates a longer momentary stall before tripping. Setting it small makes the protection react quickly but increases the chance of nuisance trips during legitimate high-load, low-speed phases.

## Examples

```text
AStuckTime[1]=4096    ; how long the stuck condition must hold continuously
AStuckTime[1]         ; read back
```

## See also

- [StuckCurr](StuckCurr.md) — current threshold; also lists the mode bypasses
- [StuckVel](StuckVel.md) — velocity threshold
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1007 (motor stuck)
