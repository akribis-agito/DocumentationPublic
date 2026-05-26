---
keyword: HomingStep
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 385
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
# HomingStep

**Definition:**

HomingStep is a read-only parameter that reports the index of the last completed step in the homing sequence. It can be monitored to track progress through a multi-step homing procedure. It is an axis-related, read-only status variable that is not saved to flash.

**See also:**

[HomeStat](HomeStat.md), [HomingOn](HomingOn.md), [HomingDef](HomingDef.md)
