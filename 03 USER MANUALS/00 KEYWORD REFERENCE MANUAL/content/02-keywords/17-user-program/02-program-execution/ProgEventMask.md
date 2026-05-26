---
keyword: ProgEventMask
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 521
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
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# ProgEventMask

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Defines a bitwise mask to apply on the user defined event trigger parameter. The mask is also

applied on the trigger value.
