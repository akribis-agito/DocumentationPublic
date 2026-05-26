---
keyword: EventGap
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 182
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# EventGap

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

EventGap defines the position gap between event generations. Note that if Event Gap is small,
and the velocity is high, a high PulseWidth may cause events to overlap.
