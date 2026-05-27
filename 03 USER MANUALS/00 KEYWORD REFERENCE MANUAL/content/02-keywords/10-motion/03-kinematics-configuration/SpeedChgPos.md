---
keyword: SpeedChgPos
summary: Axis position at which a speed-change-on-the-fly event is triggered.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 346
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
  - -2147483648
  - 2147483647
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# SpeedChgPos

Axis position at which a speed-change-on-the-fly event is triggered.

## Overview

`SpeedChgPos` sets the axis position, in user units, at which the speed-change-on-the-fly event is triggered when [SpeedChgOn](SpeedChgOn.md) is active. When the axis crosses this position in the direction selected by [SpeedChgDir](SpeedChgDir.md), the commanded speed is updated to [SpeedChgNew](SpeedChgNew.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

The crossing test compares `SpeedChgPos` against the **post-shaping position reference**, not the measured feedback. This is the same value that drives the position loop, so the change fires deterministically when the planned trajectory passes `SpeedChgPos`, slightly ahead of where the load physically arrives. With [SpeedChgDir](SpeedChgDir.md) `= 0` the event fires when the reference rises above `SpeedChgPos`; with `= 1` it fires when the reference falls below it. The value is in the same user units as [PosRef](../01-kinematics-status/PosRef.md). See [SpeedChgOn](SpeedChgOn.md) for the full mechanism.

## Examples

```text
ASpeedChgPos=50000   ; trigger position (user units)
ASpeedChgPos        ; query current value
```

## See also

- [SpeedChgOn](SpeedChgOn.md) — enables speed change on the fly
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
- [SpeedChgDir](SpeedChgDir.md) — direction in which the trigger is active
- [PosRef](../01-kinematics-status/PosRef.md) — the reference compared against `SpeedChgPos`
