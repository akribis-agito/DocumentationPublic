---
keyword: VelTrackFact
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 107
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1228
  default: 1024
  scaling: 1.0
  implemented: final
overrides: {}
---
# VelTrackFact

**Definition:**

VelTrackFact is used to scale the filtered position derivative before entering velocity loop. Scaling factor in use is VelTrackFact/1024.
