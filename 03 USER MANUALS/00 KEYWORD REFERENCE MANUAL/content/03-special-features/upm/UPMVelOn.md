---
keyword: UPMVelOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 407
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
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# UPMVelOn

**Definition:**

UPMVelOn enables the UPM anti-cogging compensation function, which applies an angle-indexed correction table (UPMVelTable) to the current reference to cancel cogging torque. The table is indexed by the commutation (electrical) angle in degrees, and the corresponding table entry is added to the current reference at each control cycle. This compensation applies only to brushless motors. UPMVelOn is a 0/1 enable. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

**See also:**

[UPMDistOn](UPMDistOn.md), [UPMRptOn](UPMRptOn.md)
