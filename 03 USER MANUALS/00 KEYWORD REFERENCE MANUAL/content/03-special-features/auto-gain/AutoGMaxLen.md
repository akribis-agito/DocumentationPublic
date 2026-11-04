---
keyword: AutoGMaxLen
summary: Sets the per-region upper limit on the number of motion samples the auto-gain algorithm collects for inertia identification.
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
can_code: 356
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
  - 20
  - 100
  default: 30
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGMaxLen

**Definition:**

AutoGMaxLen sets the per-region upper limit on the number of motion samples the auto-gain algorithm collects for inertia identification. Samples are sorted into four regions by direction of motion and direction of command; once a region has accumulated AutoGMaxLen samples it stops collecting further samples for that region, while the other regions continue. AutoGMinLen sets the per-region count at which a region is considered to have enough data. Range 20 to 100; default 30. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGMinLen](AutoGMinLen.md), [AutoGAccTh](AutoGAccTh.md), [AutoGOn](AutoGOn.md)
