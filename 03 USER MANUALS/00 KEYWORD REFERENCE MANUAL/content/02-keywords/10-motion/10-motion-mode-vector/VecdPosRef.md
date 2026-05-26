---
keyword: VecdPosRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 644
attributes:
  access: ro
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
# VecdPosRef

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

A status parameter that reports the derivative of the vector motion position reference

(derivative of VecPosRef). VecdPosRef is always positive.
