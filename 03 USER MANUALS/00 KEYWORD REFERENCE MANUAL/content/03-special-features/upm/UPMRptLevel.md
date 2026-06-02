---
keyword: UPMRptLevel
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 554
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: none
  range:
  - 0
  - 100
  default: 20
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# UPMRptLevel

**Definition:**

UPMRptLevel sets the cutoff frequency of the model-range (Q) low-pass filter used by the UPM repetitive compensation algorithm. It is expressed as a percentage from 0 to 100%, which maps linearly to a filter frequency range of 30 Hz (at 0%) to 500 Hz (at 100%). It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

> **Version note:** This is the v4 name for this parameter. In v5 the same parameter was renamed [UPMRptRange](UPMRptRange.md) and is expressed as a frequency range in Hz. They are the same underlying parameter — use `UPMRptLevel` on v4 controllers and `UPMRptRange` on v5 controllers.

**See also:**

[UPMRptRange](UPMRptRange.md), [UPMRptOn](UPMRptOn.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptState](UPMRptState.md)
