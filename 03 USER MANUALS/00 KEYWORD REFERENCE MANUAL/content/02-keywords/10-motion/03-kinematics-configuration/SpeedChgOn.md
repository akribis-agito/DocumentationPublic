---
keyword: SpeedChgOn
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

**Definition:**

SpeedChgOn enables the speed-change-on-the-fly feature. When set to a non-zero value the controller monitors the axis position and, upon reaching SpeedChgPos, changes the commanded velocity to SpeedChgNew in the direction specified by SpeedChgDir. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[SpeedChgPos](SpeedChgPos.md), [SpeedChgNew](SpeedChgNew.md), [SpeedChgDir](SpeedChgDir.md)
