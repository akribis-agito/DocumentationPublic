---
keyword: AutoGCopy
summary: A command that applies the gains computed by the automatic gain tuning algorithm to the active servo controller parameters.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 350
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGCopy

**Definition:**

AutoGCopy is a command that applies the gains computed by the automatic gain tuning algorithm to the active servo controller parameters. The computed values are written into the gain set selected by AutoGNumSet, and only the individual gains enabled by AutoGMask (position gain, velocity gain, velocity integral gain, and acceleration feedforward gain) are copied. The copy is performed only when valid tuning results are present and only in the semi-automatic modes (AutoGMode 2 or 4), where gains are calculated on request but not applied automatically; in those modes AutoGCopy is the step that transfers them to the controller. It is an axis-related command and is not saved to flash.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGStatus](AutoGStatus.md), [AutoGBW](AutoGBW.md)
