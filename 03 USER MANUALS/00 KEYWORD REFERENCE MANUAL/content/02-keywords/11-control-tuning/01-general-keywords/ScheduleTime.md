---
keyword: ScheduleTime
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 262
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
  range: null
  default: null
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range:
    - 0
    - 655360
---
# ScheduleTime

The dwell time, in milliseconds, used by the time-based gain-scheduling modes to delay the switch back to the steady-state gain set.

## Overview

`ScheduleTime` sets the hold-off interval used by the gain-scheduling modes that switch sets based on a timer after a triggering condition clears. It applies to [ScheduleMode](ScheduleMode.md) values `2`, `6`, `7`, `11` and `12`. The value is in milliseconds.

## How it works

In each of the time-based modes, the controller runs a timer that resets while the triggering condition is active and accumulates once it clears. The active gain set is held at an intermediate value until the timer reaches `ScheduleTime`, after which the controller switches to the steady-state set:

- **Optimal settling by time (2):** while in motion, set 1; after motion stops, set 2 is held for `ScheduleTime`, then set 3.
- **Quiet standing (6):** set 2 while in motion and for `ScheduleTime` after motion stops, then set 1 once stationary longer than `ScheduleTime`.
- **By PD pulses (7):** set 2 while pulse-and-direction velocity is non-zero; set 1 resumes once pulses have been absent continuously for `ScheduleTime`.
- **CNC motions (11, 12):** after a non-linear (corner/arc) segment is followed by a linear segment, an intermediate settling set is held for `ScheduleTime` before reverting to the linear-segment set.

## Examples

```text
AScheduleTime=50             ; 50 ms hold-off for the time-based schedule modes
AScheduleMode[1]=2           ; optimal settling by time, using ScheduleTime
```

## See also

- [ScheduleMode](ScheduleMode.md) — modes 2, 6, 7, 11 and 12 use this timing
- [ScheduleSet](ScheduleSet.md) — set currently selected
- [InTargetStat](../../10-motion/05-motion-status/InTargetStat.md) — in-target/in-motion state used by the settling modes
- [PDVel](../../10-motion/06-motion-mode-pulse-and-direction-pd/PDVel.md) — pulse-and-direction velocity used by mode 7
