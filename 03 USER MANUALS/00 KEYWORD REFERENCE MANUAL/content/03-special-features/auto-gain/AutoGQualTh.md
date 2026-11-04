---
keyword: AutoGQualTh
summary: Sets the maximum allowed value of the identification quality metric (an estimation-error figure expressed as a percentage, where lower is better).
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
can_code: 368
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
  - 1000
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGQualTh

**Definition:**

AutoGQualTh sets the maximum allowed value of the identification quality metric (an estimation-error figure expressed as a percentage, where lower is better). A calculation's result is accepted and folded into the estimate only when its quality metric is at or below this threshold and the estimated inertia ratio also falls within the AutoGMinRat to AutoGMaxRat range; results whose quality metric exceeds the threshold are discarded. The range is 1 to 1000, default 100. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGNumSet](AutoGNumSet.md), [AutoGMinRat](AutoGMinRat.md), [AutoGMaxRat](AutoGMaxRat.md)
