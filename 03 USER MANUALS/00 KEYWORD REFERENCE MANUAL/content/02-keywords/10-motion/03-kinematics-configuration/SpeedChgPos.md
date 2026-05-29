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

The crossing test compares `SpeedChgPos` against the **post-shaping position reference**, not the measured feedback. This is the same value that drives the position loop, so the change fires deterministically when the planned trajectory passes `SpeedChgPos`, slightly ahead of where the load physically arrives. With [SpeedChgDir](SpeedChgDir.md) `= 0` the event fires when the reference rises above `SpeedChgPos`; with `= 1` it fires when the reference falls below it. The value is in the same user units as [PosRef](../01-kinematics-status/PosRef.md). See [SpeedChgOn](SpeedChgOn.md) for the full mechanism and the timeline diagram.

## Examples

```text
ASpeedChgPos=50000   ; trigger position (user units)
ASpeedChgPos        ; query current value
```

### Edge cases

- **Motor off:** value is held; no trigger fires.
- **Out-of-range write:** the parameter system rejects values outside ±2³¹−1.
- **Simulation mode (`MotorType` = 5):** trigger fires normally; the simulated reference advances through `SpeedChgPos` just as a real one would.
- **ModRev wrap:** because the wrap shifts both the reference and `SpeedChgPos` would need to be in the modulo frame, set `SpeedChgPos` inside `[0, ModRev)`. A trigger at, say, `2 × ModRev` is unreachable.
- **Active fault:** value is preserved; with motion stopped, the trigger does not fire.
- **Already past trigger when armed:** the trigger fires on the next cycle (the comparison is level-based, not edge-based).
- **Other motion modes:** trigger fires in any mode that updates [PosRefShapedFilt](../01-kinematics-status/PosRef.md); however the consequent write to [Speed](Speed.md) only matters in modes that use `Speed`.

## See also

- [SpeedChgOn](SpeedChgOn.md) — enables speed change on the fly
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
- [SpeedChgDir](SpeedChgDir.md) — direction in which the trigger is active
- [PosRef](../01-kinematics-status/PosRef.md) — the reference compared against `SpeedChgPos`
