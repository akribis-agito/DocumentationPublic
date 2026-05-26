---
keyword: ProgStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 259
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 9
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 1
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgStat

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Inquires the status of the specified program thread:
         -1: No user program in the controller
         0: Not running
         1: Running
