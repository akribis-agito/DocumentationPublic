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

Each control cycle, while `SpeedChgOn != 0`, the controller compares the post-shaping position reference (`glPosRefShapedFilt`) against [SpeedChgPos](SpeedChgPos.md) (`AG300_CTL01ControlInterrupt.c:3733`):

- [SpeedChgDir](SpeedChgDir.md) `= 0` — wait for the reference to rise **above** `SpeedChgPos` (forward crossing).
- [SpeedChgDir](SpeedChgDir.md) `= 1` — wait for the reference to fall **below** `SpeedChgPos` (reverse crossing).

When the crossing is detected the firmware writes the new speed straight into the active speed setting, `glSpeed = SpeedChgNew`, and **clears `SpeedChgOn` to `0`** in the same step so the change happens exactly once (`:3740`–`:3741`). Because the new value is loaded into `Speed`, the profiler re-targets the velocity and ramps to it under the normal [Accel](Accel.md)/[Decel](Decel.md) (and jerk) limits — the speed does not step.

This is a **one-shot** trigger: to arm another change you must set `SpeedChgOn = 1` again (typically after also updating `SpeedChgPos`/`SpeedChgNew`). The trigger uses the *reference* position, not the feedback, so it fires deterministically with the planned trajectory rather than waiting for the load to physically arrive. The comparison is the same in the per-axis path and the grouped-motion path (`AG300_CTL01ControlInterrupt.c:14448`).

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
