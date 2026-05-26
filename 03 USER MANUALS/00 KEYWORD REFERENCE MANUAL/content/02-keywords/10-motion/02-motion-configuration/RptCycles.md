---
keyword: RptCycles
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 713
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RptCycles

**Condition:**

RptCycles is used only when MotionMode = 2 (repetitive point-to-point (PTP) motion).

**Definition:**

RptCycles is used to define the number of repetitions required for repetitive PTP motion. Please refer to RptMode on how repetition is defined.

Once the number of repetitions is reached, the motion will end. If RptCycles=0, the PTP motion will repeat indefinitely.
