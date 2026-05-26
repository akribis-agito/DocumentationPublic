---
keyword: ProgEventOn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 527
attributes:
  access: rw
  scope: non-axis
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
# ProgEventOn

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Activate ("1") or disables ("0") the handling of user program events. When disabled ("0") all

pending events are cleared and events are not handled/processed at all. This includes also the

sensing of events.
