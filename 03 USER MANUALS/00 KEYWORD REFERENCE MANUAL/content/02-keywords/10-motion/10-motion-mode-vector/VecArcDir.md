---
keyword: VecArcDir
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 634
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
# VecArcDir

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

For ARC vector, defines the direction of the ARC. "0" for CCW, "1" for CW.
The VecArcDir, like all other new keywords for the vector motion, is per axis. However, only the
VecArcCenter of the axis which was used for the Begin command will be used.
2 axes are defined for an ARC motion. The ARC is performed at the plain of these two axes, with
the third axis not moving.
The two axes are defined with an important order, meaning, for example: B, C is not like C, B.
The first axis is the X axis. The second is the Y axis. Then CCW motion is around the "Z" axis,
where X axis is moving toward Y axis.
**Note:**

need to check that this definition is aligned with the CNC definition of ARC.
Saved to Flash. Can't be modified while in motion.
