---
keyword: MapErrOffRamp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 454
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
  - 1
  - 2147483647
  default: 16384
  scaling: 1.0
  implemented: final
overrides: {}
---
# MapErrOffRamp

**Definition:**

MapErrOffRamp sets the rate at which the map error offset (MapErrOffset) is ramped toward its target value when a map correction change is commanded. A higher value causes the offset to converge more quickly. It is an axis-related parameter saved to flash and can be changed at any time, including during motion.

**See also:**

[MapErrOffset](MapErrOffset.md), [MapErrOnStep](MapErrOnStep.md), [MapType](MapType.md)
