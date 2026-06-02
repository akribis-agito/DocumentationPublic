---
keyword: AutoGNumSet
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 369
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
  - 5
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGNumSet

**Definition:**

AutoGNumSet selects which gain (control) set the auto-gain algorithm writes its calculated parameters into. The four tuned parameters (position gain, velocity gain, velocity integral gain, and acceleration feed-forward gain) are saved into the selected set, either automatically in the full-auto modes or when the results are applied with the AutoGCopy keyword. Of those four, only the parameters enabled in AutoGMask are actually written. Range 1 to 5; default 1. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGQualTh](AutoGQualTh.md), [AutoGOn](AutoGOn.md), [AutoGStatus](AutoGStatus.md)
