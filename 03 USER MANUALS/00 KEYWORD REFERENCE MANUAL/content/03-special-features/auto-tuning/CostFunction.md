---
keyword: CostFunction
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 672
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# CostFunction

**Definition:**

CostFunction evaluates the cost metric used by the automatic current-loop PI tuning. It computes a scalar score from the weighted root-mean-square error between the theoretical current response (TheorCurArray) and the recorded motor-current response, plus an overshoot penalty, which the tuning process minimizes when searching for the current-loop PI gains. It is an axis-related command and is not saved to flash.

**See also:**

[TheorCurArray](TheorCurArray.md)
