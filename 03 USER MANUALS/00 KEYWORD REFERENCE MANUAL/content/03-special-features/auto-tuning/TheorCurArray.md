---
keyword: TheorCurArray
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 671
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 309
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: float32
    range: null
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# TheorCurArray

**Definition:**

TheorCurArray is an array parameter that stores the theoretical current-loop response used by the automatic current-loop PI tuning as a reference for computing the cost function. It holds the expected current step-response waveform that the recorded motor-current response is compared against; the firmware only reads it, so the reference points must be supplied by the host. The array holds up to 308 entries (indexes [1] to [308]). It is an axis-related array parameter saved to flash and can be changed at any time, including while the axis is in motion and with the motor on.

**See also:**

[CostFunction](CostFunction.md)
