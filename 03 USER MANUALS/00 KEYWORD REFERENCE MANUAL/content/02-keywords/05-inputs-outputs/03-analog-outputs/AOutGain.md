---
keyword: AOutGain
summary: Not a current firmware keyword — analog-output scaling is done by AOutShifts.
availability:
  standalone: []
  central-i:
  - v5
can_code: 221
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AOutGain

Not a current firmware keyword — analog-output scaling is done by AOutShifts.

> **Not present in the firmware.** `AOutGain` does not exist in the controller's keyword
> table (`AG300_CTL01Params.c`) and cannot be used. Analog-output scaling is performed by
> [AOutShifts](AOutShifts.md) (a power-of-two scale) together with [AOutOffset](AOutOffset.md).
> This page is retained only to redirect readers who expected a gain keyword.

## See also

- [AOutShifts](AOutShifts.md) — power-of-two output scaling (the actual mechanism)
- [AOutMode](AOutMode.md) — direct vs monitoring mode
- [AOutOffset](AOutOffset.md) — output offset
