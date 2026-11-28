---
keyword: AutoGAccTh
summary: Sets the acceleration threshold in user units per second squared below which motion data is excluded from the auto-gain identification process.
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
can_code: 353
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 100
  - 2000000000
  default: 100000
  scaling: 1.0
  implemented: final
overrides:
  agm800-ec:
    units: scaling
    scaling: 1.048576
last_updated: '2026-05-25'
doc_revision: '2026.06'
---
# AutoGAccTh

**Definition:**

AutoGAccTh sets the acceleration threshold in user units per second squared below which motion data is excluded from the auto-gain identification process. It filters out low-excitation segments that may produce unreliable inertia estimates. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGVelTh](AutoGVelTh.md), [AutoGOn](AutoGOn.md), [AutoGMinLen](AutoGMinLen.md)
