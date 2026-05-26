---
keyword: HomeStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 111
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HomeStat

**Definition:**

HomeStat is a read-only parameter that reports the current status of the homing procedure. Its bit-field indicates whether the axis has been homed, whether a homing sequence is in progress, and any homing error conditions. It is an axis-related, read-only status variable that is not saved to flash.

**See also:**

[HomingStep](HomingStep.md), [HomingOn](HomingOn.md), [HomingStat](HomingStat.md)
