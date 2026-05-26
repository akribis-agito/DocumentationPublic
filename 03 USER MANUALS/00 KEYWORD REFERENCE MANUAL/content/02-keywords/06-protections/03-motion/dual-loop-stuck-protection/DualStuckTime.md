---
keyword: DualStuckTime
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 158
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
  default: 4096
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualStuckTime

**Definition:**

DualStuckTime specifies the maximum number of consecutive controller cycles (1 cycle ≈ 61µs) of which the difference between the two feedback in dual-loop can be more than DualStuckVel.

If DualStuckVel is exceeded for consecutive controller cycle number of DualStuckTime, axis will be disabled, and error message will be thrown.
