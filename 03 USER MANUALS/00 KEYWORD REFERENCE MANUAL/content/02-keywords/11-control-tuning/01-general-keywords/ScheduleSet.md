---
keyword: ScheduleSet
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 261
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
  - 1
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ScheduleSet

The tuning-gain set number currently in use, in the range 1–5.

## Overview

`ScheduleSet` reports which of the five gain sets is active. The active set determines the values published in [ScheduleGains](ScheduleGains.md) and applied by the control loops. In manual scheduling it is also writable, so the user can select the set directly.

## How it works

How `ScheduleSet` is determined depends on [ScheduleMode](ScheduleMode.md):

- **No scheduling (`ScheduleMode = 0`):** held at 1.
- **Manual (`ScheduleMode = 1`):** set by the user — either by writing `ScheduleSet` over communication, or, if a digital input is assigned the control-set-change function, by the input level (low → 1, high → 2).
- **Automatic modes (`ScheduleMode` ≥ 2):** the controller updates it each scheduling cycle from the active rule (motion/time, in-target, velocity/position/temperature band, PD pulses, or CNC segment). In these modes the value reflects the rule and is not meant to be written by the user.

`ScheduleSet` is reset to 1 on power-up and whenever scheduling is disabled (`ScheduleMode = 0`). When the gantry pairing of the scheduling mode does not match the current gantry state, the default set 1 is used (see [ScheduleGntry](ScheduleGntry.md)).

In the interpolated velocity/position modes (`ScheduleMode = 9` or `10`), a value of `-1` indicates a configuration error: the four band thresholds are not strictly increasing, scheduling has been disabled, and set 1 is being used.

## Examples

```text
AScheduleMode[1]=1; AScheduleSet=3      ; manual mode, then select gain set 3
AScheduleSet                            ; read the active gain-set number
```

## See also

- [ScheduleMode](ScheduleMode.md) — how the set is chosen
- [ScheduleGains](ScheduleGains.md) — gain values for the active set
