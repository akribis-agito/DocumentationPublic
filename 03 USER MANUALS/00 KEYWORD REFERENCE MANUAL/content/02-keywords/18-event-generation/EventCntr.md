---
keyword: EventCntr
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 186
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventCntr

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

EventCntr count the events that occurred since the last EventOn. Toggling EventOn will reset the
counter. This counter can also be reset by the user.
