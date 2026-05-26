---
keyword: ProgEventGEn
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 526
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
# ProgEventGEn

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Globally enables ("1") or disables ("0") the servicing of all events. ProgEventGEn, when "0", does

not disable the sensing of events, and events are still sensed and possibly pending, to be serviced

when enabled.

Please refer to the User Program Language Manual for more information.
