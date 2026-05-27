---
keyword: SpeedChgDir
summary: Selects the direction in which the speed-change-on-the-fly trigger is active.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 347
attributes:
  access: rw
  scope: axis
  flash: true
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
# SpeedChgDir

Selects the direction in which the speed-change-on-the-fly trigger is active.

## Overview

`SpeedChgDir` specifies the direction of motion in which the speed-change-on-the-fly event is active. Only when the axis is moving in the selected direction will crossing [SpeedChgPos](SpeedChgPos.md) trigger a change to [SpeedChgNew](SpeedChgNew.md). The feature as a whole must be enabled with [SpeedChgOn](SpeedChgOn.md). It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

## Examples

```text
ASpeedChgDir=0       ; trigger active in one direction
ASpeedChgDir=1       ; trigger active in the other direction
ASpeedChgDir        ; query current value
```

## See also

- [SpeedChgOn](SpeedChgOn.md) — enables speed change on the fly
- [SpeedChgPos](SpeedChgPos.md) — position that triggers the change
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
