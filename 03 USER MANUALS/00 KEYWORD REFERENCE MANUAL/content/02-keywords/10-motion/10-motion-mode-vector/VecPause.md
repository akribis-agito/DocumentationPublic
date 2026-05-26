---
keyword: VecPause
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 640
attributes:
  access: rw
  scope: axis
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
# VecPause

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

A value of "1" pauses the vector motion by setting the speed to 0 (motion is decelerated till
stopping). A value of "0" continue the motion normally (if paused before, it will accelerate to the
VecSpeed again).

Not Saved to Flash. At power-up gets its default value: "0".
