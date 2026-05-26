---
keyword: ProgEventPar
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 520
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventPar

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Defines (using Complex CAN Code) which controller parameter to use for the triggering of this

event. If ProgEventPar[EventNumber] is set to 0 (or to a non-valid Complex CAN code), this event

will not be sensed and will not be handled.
