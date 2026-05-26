---
keyword: AllStat
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 420
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range: null
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AllStat

**Definition:**

AllStat is only supported over Ethernet Binary communication. It is used by AAMotion API to query various statuses for multiple axes in a single message. This keyword is scheduled to be deprecated / revamped.