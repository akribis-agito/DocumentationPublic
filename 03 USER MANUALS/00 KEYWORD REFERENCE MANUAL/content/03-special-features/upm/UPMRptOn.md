---
keyword: UPMRptOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 559
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
  - 2
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    range: null
    default: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# UPMRptOn

**Definition:**

UPMRptOn requests UPM repetitive (periodic) motion compensation for the next motion. When active, the controller adapts a feedforward correction to cancel position errors that repeat with each motion cycle. The request has three values: 0 = none, 1 = first (capture a single learning pass), and 2 = repetitive (apply repetitive compensation). The request is consumed at the start of the next motion: the controller sets the corresponding repetitive state and then clears UPMRptOn back to 0, so it must be set again before each motion that should use the feature. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

**See also:**

[UPMRptCalc](UPMRptCalc.md), [UPMRptLevel](UPMRptLevel.md), [UPMRptState](UPMRptState.md), [UPMRptTime](UPMRptTime.md)
