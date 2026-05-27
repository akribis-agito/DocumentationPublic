---
keyword: CounterUp
summary: Two independent up-counters incremented every controller cycle.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
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

Two independent up-counters incremented every controller cycle.

## Overview

`CounterUp` provides two independent counters, `CounterUp[1]` and `CounterUp[2]`. Each starts at 0 at power-up and increments by 1 every controller cycle. On reaching the maximum (2147483647) a counter rolls over to −2147483648 and keeps incrementing. Because it is writable, a user program can preset or reset a counter to time or count events in units of controller cycles.

## Examples

```text
ACounterUp[1]       ; read the first up-counter
ACounterUp[1]=0      ; reset the first up-counter
```

## See also

- [CounterDown](CounterDown.md) — cycle-based down-counters
- [Time](Time.md) / [HWTimer](HWTimer.md) — wall-clock and high-resolution timers
