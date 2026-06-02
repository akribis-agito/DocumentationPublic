---
keyword: UPMRptMotion
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 562
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 4
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# UPMRptMotion

**Definition:**

UPMRptMotion selects which learned-motion slot the UPM repetitive compensation function uses, choosing the stored feedforward correction table that matches the current motion. Its range is 0 to (number of learnable motions - 1); the number of available slots depends on the controller model. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

**See also:**

[UPMRptOn](UPMRptOn.md), [UPMRptTime](UPMRptTime.md), [UPMRptCalc](UPMRptCalc.md)
