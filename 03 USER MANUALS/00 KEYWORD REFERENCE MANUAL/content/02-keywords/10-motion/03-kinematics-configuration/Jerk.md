---
keyword: Jerk
summary: Rate of change of acceleration; a finite value produces an S-curve motion profile.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 139
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 9
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Jerk

Rate of change of acceleration; a finite value produces an S-curve motion profile.

## Overview

`Jerk` sets the rate of change of acceleration (the third derivative of position) for point-to-point motion. A finite jerk value produces an S-curve profile that smooths the transitions in and out of the [Accel](Accel.md) and [Decel](Decel.md) ramps, reducing mechanical vibration at the start and end of a move. Whether jerk limiting is used at all, and to what order, is governed by [JerkMode](../02-motion-configuration/JerkMode.md). Unlike most kinematic parameters, `Jerk` cannot be changed while the axis is in motion. It is an axis-related parameter saved to flash.

## Examples

```text
AJerk=5              ; jerk setting (S-curve smoothing)
AJerk               ; query current value
```

## See also

- [Accel](Accel.md) — acceleration rate that jerk smooths into
- [Decel](Decel.md) — deceleration rate that jerk smooths into
- [JerkInAcc](JerkInAcc.md) — jerk during the acceleration phase (third-order profile)
- [JerkInDec](JerkInDec.md) — jerk during the deceleration phase (third-order profile)
- [JerkMode](../02-motion-configuration/JerkMode.md) — selects the profiler order
