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

## Examples

```text
ASpeedChgPos=50000   ; trigger position (user units)
ASpeedChgPos        ; query current value
```

## See also

- [SpeedChgOn](SpeedChgOn.md) — enables speed change on the fly
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
- [SpeedChgDir](SpeedChgDir.md) — direction in which the trigger is active
