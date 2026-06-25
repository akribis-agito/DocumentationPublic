---
keyword: AutoGPosFilt
summary: Sets the cutoff frequency of the first-order low-pass filter used by the auto-gain identification algorithm.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 354
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 1000
  default: 50
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# AutoGPosFilt

**Definition:**

AutoGPosFilt sets the cutoff frequency of the first-order low-pass filter used by the auto-gain identification algorithm. The same filter is applied to both the position and the current-command signals that the algorithm uses; changing this value recomputes the filter coefficients. A higher value gives a higher cutoff frequency. Range 1 to 1000; default 50. It is an axis-related parameter saved to flash and can be changed at any time.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGAccTh](AutoGAccTh.md), [AutoGVelTh](AutoGVelTh.md)
