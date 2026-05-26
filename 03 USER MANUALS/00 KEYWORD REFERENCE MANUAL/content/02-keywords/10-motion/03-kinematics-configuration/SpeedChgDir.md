---
keyword: SpeedChgDir
availability:
  standalone:
  - v4
  central-i:
  - v4
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

**Definition:**

SpeedChgDir specifies the direction of motion in which the speed-change-on-the-fly event (SpeedChgPos) is active. Only when the axis is moving in the selected direction will passing SpeedChgPos trigger a speed change to SpeedChgNew. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[SpeedChgOn](SpeedChgOn.md), [SpeedChgPos](SpeedChgPos.md), [SpeedChgNew](SpeedChgNew.md)
