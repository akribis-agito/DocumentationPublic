---
keyword: UPMDistOn
summary: Enables the UPM disturbance rejection function.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 603
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# UPMDistOn

**Definition:**

UPMDistOn enables the UPM disturbance rejection function. When active, the controller runs a disturbance-observer-style acceleration-feedback loop: it compares the acceleration expected from the commanded current (the current reference scaled by the plant gain UPMDistSystem) against the low-pass-filtered measured acceleration, then integrates the difference; the integrator output becomes the new current reference, rejecting the estimated disturbance. UPMDistOn is a 0/1 enable. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

**See also:**

[UPMDistSystem](UPMDistSystem.md), [UPMDistReject](UPMDistReject.md), [UPMDistFilter](UPMDistFilter.md), [UPMVelOn](UPMVelOn.md)
