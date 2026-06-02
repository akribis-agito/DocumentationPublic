---
keyword: UPMRptRange
availability:
  standalone: []
  central-i:
  - v5
can_code: 554
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 30
  - 500
  default: 124
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# UPMRptRange

**Definition:**

UPMRptRange sets the frequency range, in Hz, of the UPM repetitive compensation filter. It defines the bandwidth over which the learned correction is shaped: error content within the range is corrected, while content above it is attenuated, so a higher value lets the compensation act on faster error features and a lower value keeps the correction smoother and more conservative. The value is the cut-off frequency of the shaping (Q) filter applied when the correction is computed, with a usable range of 30 Hz to 500 Hz and a default of 124 Hz. UPMRptRange is the renamed successor of the older UPMRptLevel parameter (which expressed the same setting as a percentage); it is now specified directly as a frequency in Hz. It is an axis-related parameter saved to flash, and can be changed in motion and with the motor on.

Changing UPMRptRange (like changing the plant model) does not take effect immediately: it marks the UPM repetitive coefficients as needing recalculation by setting [StatReg] bit 26 (the filters/plant-model-modified indication). Run UPMCalcCoeff afterward to recompute the coefficients from the new range before the next UPMRptCalc; a successful UPMCalcCoeff clears [StatReg] bit 26. This pending state is surfaced only as an indication; it does not block enabling the motor.

This keyword name is used from v5 (central-i); on v4 the same setting is UPMRptLevel (expressed as a percentage).

**See also:**

[UPMCalcCoeff](UPMCalcCoeff.md), [UPMRptOn](UPMRptOn.md), [UPMRptCalc](UPMRptCalc.md), [UPMRptLevel](UPMRptLevel.md), [UPMRptState](UPMRptState.md)
