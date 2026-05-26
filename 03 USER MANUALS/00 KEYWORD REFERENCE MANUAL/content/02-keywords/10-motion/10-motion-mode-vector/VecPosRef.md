---
keyword: VecPosRef
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 643
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
# VecPosRef

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

The VecPosRef is a status parameter that reports the current position reference of the vector
motion profile (along the vector path). It starts from a value of 0 and upon end of motion,
reaches the value of VecAbsTrgt.
VecPosRef is always positive.
