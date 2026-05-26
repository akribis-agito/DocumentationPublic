---
keyword: VecType
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 630
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecType

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

Defines if the requested vector motion is linear (VecType = 0) or ARC (VecType = 1).
Saved to Flash. Can't be modified while in motion.

Near future need: VecType = 2 for combined ARC (main motion) and linear (other axes).
