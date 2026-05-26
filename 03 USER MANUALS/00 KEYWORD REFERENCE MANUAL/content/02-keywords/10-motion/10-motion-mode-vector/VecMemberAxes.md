---
keyword: VecMemberAxes
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 631
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecMemberAxes

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Used (bitwise) to define the axes participating in the vector motion.

Saved to Flash. Can't be modified while in motion.
