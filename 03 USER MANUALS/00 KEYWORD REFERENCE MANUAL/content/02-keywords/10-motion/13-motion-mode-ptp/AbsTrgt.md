---
keyword: AbsTrgt
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 134
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
# AbsTrgt

**Definition:**

AbsTrgt sets the absolute target position in user units for the next point-to-point move. When a Begin command is issued in absolute PTP mode, the axis moves to this position. It is an axis-related parameter, not saved to flash, and can be changed at any time.

**See also:**

[RelTrgt](RelTrgt.md), [Begin](../04-motion-command/Begin.md), [Targets](Targets.md)
