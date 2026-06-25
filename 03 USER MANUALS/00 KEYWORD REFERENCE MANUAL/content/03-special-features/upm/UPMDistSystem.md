---
keyword: UPMDistSystem
summary: Sets the scalar plant-gain estimate used by the UPM disturbance rejection algorithm.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 604
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
  - 1
  - 100000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# UPMDistSystem

**Definition:**

UPMDistSystem sets the scalar plant-gain estimate used by the UPM disturbance rejection algorithm. The controller multiplies the commanded current by this gain to predict the expected acceleration; it also scales the rejection strength inversely with this value. Its range is 1 to 100000000, with a default of 1000. It cannot be changed while the axis is in motion or with the motor on. It is an axis-related parameter saved to flash.

**See also:**

[UPMDistOn](UPMDistOn.md), [UPMDistReject](UPMDistReject.md), [UPMDistFilter](UPMDistFilter.md)
