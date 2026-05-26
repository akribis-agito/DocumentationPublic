---
keyword: EventPulseRes
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 517
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
# EventPulseRes

**Definition:**

EventPulseRes sets the position resolution of the event output pulse generator, defining the minimum spacing between events in encoder counts. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventPulseWid](EventPulseWid.md), [EventSelect](EventSelect.md), [EventTableWid](EventTableWid.md)
