---
keyword: MapErrOnStep
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 476
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
  - 16384
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapErrOnStep

**Definition:**

MapErrOnStep sets the incremental step size used when the error-mapping correction is applied on a step-by-step basis rather than in a single jump. It controls how quickly the map correction converges when the mapping feature is activated. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[MapErrOffset](MapErrOffset.md), [MapErrOffRamp](MapErrOffRamp.md), [MapType](MapType.md)
