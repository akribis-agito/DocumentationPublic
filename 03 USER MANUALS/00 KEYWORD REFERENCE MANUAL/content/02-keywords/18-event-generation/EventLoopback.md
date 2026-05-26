---
keyword: EventLoopback
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 565
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
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventLoopback

**Definition:**

EventLoopback is a read-only parameter that reflects the current state of the event output signal as seen by the controller's input circuitry, providing a hardware loopback confirmation. It is an axis-related status variable and is not saved to flash.

**See also:**

[EventAlwaysOn](EventAlwaysOn.md), [EventSelect](EventSelect.md), [EventOn](EventOn.md)
