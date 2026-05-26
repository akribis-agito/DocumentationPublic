---
keyword: EventAlwaysOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 619
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
# EventAlwaysOn

**Definition:**

EventAlwaysOn forces the event output to be permanently active regardless of position or table conditions. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventSelect](EventSelect.md), [EventOn](EventOn.md), [EventLoopback](EventLoopback.md)
