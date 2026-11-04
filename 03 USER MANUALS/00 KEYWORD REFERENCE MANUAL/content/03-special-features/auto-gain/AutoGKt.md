---
keyword: AutoGKt
summary: Stores the motor torque constant (Kt) used by the automatic gain tuning algorithm to relate current command to force or torque when computing bandwidth-based gains.
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
can_code: 362
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
  default: 38231
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGKt

**Definition:**

AutoGKt stores the motor torque constant (Kt) used by the automatic gain tuning algorithm to relate current command to force or torque when computing bandwidth-based gains. It works together with the motor inertia value in AutoGJm to estimate the load-to-motor inertia ratio. The valid range is 1 to 2147483647, with a default of 38231. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGBW](AutoGBW.md), [AutoGJm](AutoGJm.md), [AutoGOn](AutoGOn.md)
