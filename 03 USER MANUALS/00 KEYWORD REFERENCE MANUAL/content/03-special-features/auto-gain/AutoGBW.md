---
keyword: AutoGBW
summary: Sets the target closed-loop bandwidth in Hz for the automatic gain tuning algorithm.
availability:
- controller
- ci-master
products:
- agc300-et
- agc301-et
- agc301-et-bioxtreme
- agd155-af-2a06
- agd155-af-2a10
- agd200-et-2d01
- agd200-et-2d02
- agd200-et-2d05
- agd200-et-2d05-71
- agd301-et-2d01
- agd301-et-2d02
- agd301-et-2d05
- agd301-et-2d09
can_code: 358
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
  - 2000
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-25'
doc_revision: '2026.06'
---
# AutoGBW

**Definition:**

AutoGBW sets the target closed-loop bandwidth in Hz for the automatic gain tuning algorithm. The tuner uses this value to compute the desired servo gains that achieve the specified bandwidth. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGMode](AutoGMode.md), [AutoGJm](AutoGJm.md), [AutoGKt](AutoGKt.md)
