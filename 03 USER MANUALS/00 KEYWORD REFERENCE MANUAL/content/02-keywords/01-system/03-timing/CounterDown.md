---
keyword: CounterDown
summary: Two independent down-counters decremented every controller cycle.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Two independent down-counters decremented every controller cycle.

## Overview

`CounterDown` provides two independent counters, `CounterDown[1]` and `CounterDown[2]`. Each starts at 0 at power-up and, while non-zero, decrements by 1 every controller cycle. On reaching 0 a counter stays at 0 — it does not roll over. Write a starting value to count down a fixed number of controller cycles, for example to implement a timeout or delay in a user program.

## Examples

```text
ACounterDown[1]=1000 ; count down 1000 controller cycles
ACounterDown[1]     ; read the remaining count
```

## See also

- [CounterUp](CounterUp.md) — cycle-based up-counters
- [Time](Time.md) / [HWTimer](HWTimer.md) — wall-clock and high-resolution timers
