---
keyword: RelTrgt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 135
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RelTrgt

**Definition:**

RelTrgt sets the relative target distance in user units for the next point-to-point move. When a Begin command is issued in relative PTP mode, the axis moves by this distance from its current position. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[AbsTrgt](AbsTrgt.md), [Begin](../04-motion-command/Begin.md), [Targets](Targets.md)
