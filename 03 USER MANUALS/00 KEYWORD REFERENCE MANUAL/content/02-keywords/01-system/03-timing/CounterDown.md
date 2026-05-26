---
keyword: CounterDown
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 39
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
# CounterDown

**Definition:**

CounterDown is a user-writable keyword containing 2 array elements that count down independently from each other. The counters are initialised to 0 upon power up, and if non-zero, will decrement by 1 count every controller cycle.

Once CounterDown reaches 0, it will remain at 0 and not rollover.
