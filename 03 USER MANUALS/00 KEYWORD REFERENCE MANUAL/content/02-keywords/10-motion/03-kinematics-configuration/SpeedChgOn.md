---
keyword: SpeedChgOn
summary: Enables the speed-change-on-the-fly feature for the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 345
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# SpeedChgOn

Enables the speed-change-on-the-fly feature for the axis.

## Overview

`SpeedChgOn` enables the speed-change-on-the-fly feature. When set to `1`, the controller monitors the axis position and, upon reaching [SpeedChgPos](SpeedChgPos.md), changes the commanded velocity to [SpeedChgNew](SpeedChgNew.md) in the direction specified by [SpeedChgDir](SpeedChgDir.md). It is an axis-related parameter, not saved to flash, and can be changed at any time, including during motion.

## How it works

Each control cycle, while `SpeedChgOn != 0`, the controller compares the post-shaping position reference against [SpeedChgPos](SpeedChgPos.md):

- [SpeedChgDir](SpeedChgDir.md) `= 0` — wait for the reference to rise **above** `SpeedChgPos` (forward crossing).
- [SpeedChgDir](SpeedChgDir.md) `= 1` — wait for the reference to fall **below** `SpeedChgPos` (reverse crossing).

When the crossing is detected the controller writes [SpeedChgNew](SpeedChgNew.md) straight into the active [Speed](Speed.md) setting, and **clears `SpeedChgOn` to `0`** in the same step so the change happens exactly once. Because the new value is loaded into `Speed`, the profiler re-targets the velocity and ramps to it under the normal [Accel](Accel.md)/[Decel](Decel.md) (and jerk) limits — the speed does not step.

This is a **one-shot** trigger: to arm another change you must set `SpeedChgOn = 1` again (typically after also updating `SpeedChgPos`/`SpeedChgNew`). The trigger uses the *reference* position, not the feedback, so it fires deterministically with the planned trajectory rather than waiting for the load to physically arrive. The comparison behaves the same for single-axis moves and grouped (coordinated) motion.

![Speed change on the fly timeline](speedchg-timeline.svg)

### Worked example

To slow a forward jog from 500000 to 100000 user units/s when the axis crosses position 80000:

```text
ASpeedChgNew=100000  ; new cruise speed
ASpeedChgPos=80000   ; trigger position
ASpeedChgDir=0       ; fire on forward crossing
ASpeedChgOn=1        ; arm (auto-clears when it fires)
```

The axis decelerates from 500000 to 100000 at `Decel × AccelFact` and `SpeedChgOn` reads back as `0` after the change.

### Edge cases

- **Motor off:** the comparison runs but `Speed` has no effect; the trigger may fire if the reference happens to cross, leaving `SpeedChgOn = 0`. In practice, arm this only while in motion.
- **Out-of-range write:** the parameter system rejects values outside `0`–`1`.
- **Simulation mode (`MotorType` = 5):** the reference moves normally in simulation and the trigger fires normally.
- **ModRev wrap:** the comparison uses the post-shaping reference after the wrap shifts it, so trigger positions are interpreted in the same modulo frame as the current reference. A trigger position outside `[0, ModRev)` will not be reached unless the rotation accumulates enough to cross it.
- **Active fault:** the axis is disabled and the comparison continues, but with no motion the trigger usually does not fire; `SpeedChgOn` value is preserved across re-enable.
- **Already past trigger when armed:** the trigger fires on the next cycle (the comparison is "above" / "below", not "edge crossing").
- **Other motion modes:** the trigger overrides `Speed`, so it only has visible effect in modes that use `Speed` (jog, PTP, repetitive PTP, indirect modes). In direct modes `Speed` is not used, so the trigger writes a value that is ignored.
- **Live change in motion:** allowed; arming during a move is the intended use.
- **One-shot:** fires exactly once per arm; re-set `SpeedChgOn = 1` to re-arm.

## Examples

```text
ASpeedChgOn=1        ; enable speed change on the fly
ASpeedChgOn=0        ; disable
ASpeedChgOn         ; query state
```

## See also

- [SpeedChgPos](SpeedChgPos.md) — position that triggers the change
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
- [SpeedChgDir](SpeedChgDir.md) — direction in which the trigger is active
- [Speed](Speed.md) — the active speed setting that the trigger overwrites
