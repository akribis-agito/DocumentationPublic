---
keyword: UPMRptCalc
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 560
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    array_size: 1
---
# UPMRptCalc

**Definition:**

UPMRptCalc is a command that triggers the calculation of the UPM repetitive compensation table based on accumulated position error data. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related command and is not saved to flash.

The calculation returns error 236 if there is no valid plant model available for the UPM repetitive calculation, and error 150 if the captured motion length plus the extended UPMRptTime tail exceeds the space available in the UPM repetitive arrays.

**See also:**

[UPMRptOn](UPMRptOn.md), [UPMRptState](UPMRptState.md), [UPMRptLevel](UPMRptLevel.md)
