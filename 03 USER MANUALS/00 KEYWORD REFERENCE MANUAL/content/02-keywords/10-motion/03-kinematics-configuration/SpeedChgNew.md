---
keyword: SpeedChgNew
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 344
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
  - -1300000000
  - 1300000000
  default: 10000
  scaling: 1.0
  implemented: final
overrides: {}
---
# SpeedChgNew

**Definition:**

SpeedChgNew sets the new speed in user units per second that is applied when the axis reaches the position defined by SpeedChgPos during a speed-change-on-the-fly event. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[SpeedChgOn](SpeedChgOn.md), [SpeedChgPos](SpeedChgPos.md), [SpeedChgDir](SpeedChgDir.md)
