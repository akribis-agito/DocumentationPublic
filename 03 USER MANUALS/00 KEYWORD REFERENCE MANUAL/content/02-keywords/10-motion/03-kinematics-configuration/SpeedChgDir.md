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

## How it works

`SpeedChgDir` selects which side of the comparison against [SpeedChgPos](SpeedChgPos.md) arms the trigger:

| SpeedChgDir | Condition that fires the change |
|---|---|
| 0 | Reference rises **above** `SpeedChgPos` (waiting for a higher position). Use for a forward-moving axis. |
| 1 | Reference falls **below** `SpeedChgPos` (waiting for a lower position). Use for a reverse-moving axis. |

Set `SpeedChgDir` to match the direction the axis will be travelling when it passes `SpeedChgPos`; if it is set to the wrong side the crossing condition is never met and no change occurs. See [SpeedChgOn](SpeedChgOn.md) for the full mechanism.

## Examples

```text
ASpeedChgDir=0       ; fire when reference rises above SpeedChgPos (forward)
ASpeedChgDir=1       ; fire when reference falls below SpeedChgPos (reverse)
ASpeedChgDir        ; query current value
```

## See also

- [SpeedChgOn](SpeedChgOn.md) — enables speed change on the fly
- [SpeedChgPos](SpeedChgPos.md) — position that triggers the change
- [SpeedChgNew](SpeedChgNew.md) — new speed applied at the trigger
