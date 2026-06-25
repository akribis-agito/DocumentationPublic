---
keyword: AutoGOn
summary: Enables the automatic gain tuning process.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 361
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGOn

**Definition:**

AutoGOn enables the automatic gain tuning process. When set to 1, the controller begins collecting motion data and computing optimal servo gains based on the configured AutoG parameters. When set back to 0 the process stops and its accumulated state and status are cleared; after re-enabling, the internal filter must re-stabilize over a number of calculation cycles before the reported results become valid again. It is an axis-related parameter and is not saved to flash.

**See also:**

[AutoGMode](AutoGMode.md), [AutoGStatus](AutoGStatus.md), [AutoGBW](AutoGBW.md), [AutoGCopy](AutoGCopy.md)
