---
keyword: EventCorrect
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 419
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventCorrect

**Definition:**

EventCorrect is a command that recalculates and corrects the event table positions based on the current axis position and mapping. It cannot be executed while the axis is in motion. It is an axis-related command and is not saved to flash.

**See also:**

[EventTable](EventTable.md), [EventTableCor](EventTableCor.md), [EventSelect](EventSelect.md)
