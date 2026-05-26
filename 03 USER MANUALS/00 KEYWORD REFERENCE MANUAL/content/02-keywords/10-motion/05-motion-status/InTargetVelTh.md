---
keyword: InTargetVelTh
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 292
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 0
  - 1300000000
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetVelTh

**Condition:**

It is only used when OperationMode =1 or 4.

**Definition:**

In current or force control operation mode, InTargetVelTh is the velocity settling window which the absolute value of feedback velocity (Vel\[1\]) must stay within for InTargetTime, before InTargetStat signals that target is reached (InTargetStat=4).
