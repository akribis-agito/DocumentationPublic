---
keyword: RptWait
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 147
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RptWait

**Condition:**

RptWait is used only when MotionMode=2 (repetitive point-to-point (PTP) motion).

**Definition:**

RptWait is the dwell time in between PTP motions, in terms of milliseconds.
