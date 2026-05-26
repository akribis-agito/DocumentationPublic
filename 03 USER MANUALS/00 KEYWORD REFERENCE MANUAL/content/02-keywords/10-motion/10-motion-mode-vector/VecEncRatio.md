---
keyword: VecEncRatio
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 632
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
  - 256
  - 25600
  default: 256
  scaling: 1.0
  implemented: final
overrides: {}
---
# VecEncRatio

Used to compensate for different encoder resolutions. Each axis is scaled according to its
resolution.

The actual ratio inside the controller is scaled by /256. So VecEncRatio=256 means a ratio of 1. A
value of 260 means ratio of 260/256.

Details about how to use the EncRatio: TBD (during implementation).

Implementation must be done in a way not to cause accumulated position errors and final target
position must be reached accurately.

Saved to Flash. Can't be modified while in motion. Range 256 (ratio of 1) to 25600 (ratio of 100).
