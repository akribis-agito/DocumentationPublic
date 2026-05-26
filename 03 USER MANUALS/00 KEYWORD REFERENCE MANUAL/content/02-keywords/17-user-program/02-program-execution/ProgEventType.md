---
keyword: ProgEventType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 522
attributes:
  access: rw
  scope: non-axis
  flash: true
  type: array
  array_size: 6
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 8
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventType

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Defines the type of the trigger (rising edge, equal, not equal...). Note that the four parameters to

define a trigger for an event are very like the definition of a trigger for data recording.
