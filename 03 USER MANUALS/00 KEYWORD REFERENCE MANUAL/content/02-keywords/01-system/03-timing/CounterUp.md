---
keyword: CounterUp
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 40
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: array
  array_size: 3
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
# CounterUp

**Definition:**

CounterUp is a user-writable keyword containing 2 array elements that count up independently from each other. The counters are initialised to 0 upon power up, and will always increment by 1 count every controller cycle.

If CounterUp reaches its maximum value of 2147483647, it will rollover to -2147483648 and continue incrementing.
