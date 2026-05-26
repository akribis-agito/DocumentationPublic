---
keyword: EventPulseWid
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 179
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
  - -10000000
  - 10000000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventPulseWid

**Definition:**

EventPulseWid sets the duration of the event output pulse in microseconds. It determines how long the output signal stays active after each event trigger. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[EventPulseRes](EventPulseRes.md), [EventTableWid](EventTableWid.md), [EventSelect](EventSelect.md)
