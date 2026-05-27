---
keyword: SpeedChgOn
summary: Enables the speed-change-on-the-fly feature for the axis.
availability:
  standalone:
  - v4
  central-i:
  - v4
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

## Examples

```text
SpeedChgOn=1        ; enable speed change on the fly
SpeedChgOn=0        ; disable
SpeedChgOn?         ; query state
```

## See also

- [SpeedChgPos](SpeedChgPos.md) — position that triggers the change
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
- [SpeedChgDir](SpeedChgDir.md) — direction in which the trigger is active
