---
keyword: PTPKeepMoving
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 625
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
# PTPKeepMoving

**Definition:**

PTPKeepMoving controls whether the axis continues moving toward the last target position if a new Begin command is issued before the previous move has completed. When set to a non-zero value the axis blends smoothly into the new target without stopping. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[Begin](../04-motion-command/Begin.md), [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md), [RelTrgt](../13-motion-mode-ptp/RelTrgt.md)
