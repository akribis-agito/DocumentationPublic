---
keyword: RptCounter
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 714
attributes:
  access: ro
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RptCounter

**Condition:**

RptCounter is used only when MotionMode = 2 (repetitive point-to-point (PTP) motion).

**Definition:**

RptCounter reports the number of repetitions made in the repetitive PTP motion. Please refer to RptMode on how repetition is defined.

Once RptCounter equals the non-zero RptCycles, the repetitive PTP motion will stop.
