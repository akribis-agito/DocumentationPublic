---
keyword: VecArcCenter
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 633
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
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
# VecArcCenter

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

For ARC vector, defines the location of the arc center, so the controller can calculate the radius.
The VecArcCenter, like all other new keywords for the vector motion, is per axis. So, the
coordinate of the arc center are defined by the VecArcCenter of the two member axes.
Saved to Flash. Can't be modified while in motion.
