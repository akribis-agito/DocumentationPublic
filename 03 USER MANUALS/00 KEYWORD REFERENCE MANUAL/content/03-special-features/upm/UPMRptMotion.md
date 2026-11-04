---
keyword: UPMRptMotion
summary: Selects which learned-motion slot the UPM repetitive compensation function uses, choosing the stored feedforward correction table that matches the current motion.
availability:
- controller
- ci-master
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
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - 0
    - 4
  agd155-ec:
    range:
    - 0
    - 4
  agd155-ec-var34:
    range:
    - 0
    - 4
  agd155-ec-var34-3:
    range:
    - 0
    - 4
  agd156-ec:
    range:
    - 0
    - 4
  agd101-ec-34a:
    range:
    - 0
    - 4
  agd101-ec-17a:
    range:
    - 0
    - 4
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# UPMRptMotion

**Definition:**

UPMRptMotion selects which learned-motion slot the UPM repetitive compensation function uses, choosing the stored feedforward correction table that matches the current motion. Its range is 0 to (number of learnable motions - 1); the number of available slots depends on the controller model. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

**See also:**

[UPMRptOn](UPMRptOn.md), [UPMRptTime](UPMRptTime.md), [UPMRptCalc](UPMRptCalc.md)
