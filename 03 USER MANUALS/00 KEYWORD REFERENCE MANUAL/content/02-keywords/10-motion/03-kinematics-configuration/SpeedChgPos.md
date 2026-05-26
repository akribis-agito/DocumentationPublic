---
keyword: SpeedChgPos
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Definition:**

SpeedChgPos sets the axis position at which the speed-change-on-the-fly event is triggered when SpeedChgOn is active. When the axis reaches this position, the commanded speed is updated to SpeedChgNew. It is an axis-related parameter in user units saved to flash and can be changed at any time.

**See also:**

[SpeedChgOn](SpeedChgOn.md), [SpeedChgNew](SpeedChgNew.md), [SpeedChgDir](SpeedChgDir.md)
