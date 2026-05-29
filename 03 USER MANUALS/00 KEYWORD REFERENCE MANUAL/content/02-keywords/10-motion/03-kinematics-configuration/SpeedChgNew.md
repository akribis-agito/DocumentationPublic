---
keyword: SpeedChgNew
summary: New velocity applied when the axis reaches SpeedChgPos during a speed change on the fly.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 344
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
  - -1300000000
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# SpeedChgNew

New velocity applied when the axis reaches `SpeedChgPos` during a speed change on the fly.

## Overview

`SpeedChgNew` sets the new velocity, in user units per second, applied when the axis reaches the position defined by [SpeedChgPos](SpeedChgPos.md) during a speed-change-on-the-fly event. The feature must be enabled with [SpeedChgOn](SpeedChgOn.md), and [SpeedChgDir](SpeedChgDir.md) selects the direction in which the trigger is active. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## How it works

When the trigger fires, the controller copies `SpeedChgNew` straight into the active [Speed](Speed.md) setting, and the profiler then ramps the velocity to this value under the normal [Accel](Accel.md)/[Decel](Decel.md) (and jerk) limits, so the speed changes smoothly rather than stepping. `SpeedChgNew` may be larger or smaller than the original [Speed](Speed.md); its sign is the new direction/magnitude in user units per second. Because the value is read only at the moment of the crossing, you may update it any time before then. See [SpeedChgOn](SpeedChgOn.md) for the full trigger mechanism.

## Examples

```text
ASpeedChgNew=200000  ; speed to switch to (user units/s)
ASpeedChgNew        ; query current value
```

### Edge cases

- **Motor off:** value is held; used at the next arming.
- **Out-of-range write:** the parameter system clamps to ±1.3 × 10⁹; values outside are rejected.
- **Simulation mode (`MotorType` = 5):** unchanged.
- **ModRev wrap:** `SpeedChgNew` is a rate, not a position; unaffected.
- **Active fault:** the axis is disabled; the value is preserved.
- **Other motion modes:** the trigger writes the new value into [Speed](Speed.md). Only modes that consume `Speed` (jog, PTP, repetitive PTP, indirect modes) react; direct modes ignore `Speed` and so ignore `SpeedChgNew`.
- **`SpeedChgNew > MaxVel`:** no `Begin`-time check fires (the trigger is mid-motion); the velocity loop will clamp the [VelRef](../01-kinematics-status/VelRef.md) to `MaxVel` and set the saturation flag.
- **`SpeedChgNew = 0`:** in jog mode, the axis decelerates to rest at `Decel`; in PTP, the move stalls.

## See also

- [SpeedChgOn](SpeedChgOn.md) — enables speed change on the fly
- [SpeedChgPos](SpeedChgPos.md) — position that triggers the change
- [SpeedChgDir](SpeedChgDir.md) — direction in which the trigger is active
