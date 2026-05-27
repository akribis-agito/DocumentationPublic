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

`CounterDown` provides two independent general-purpose down-counters, `CounterDown[1]` and `CounterDown[2]`. (The array is dimensioned for three elements so that the usable indices start at `[1]`; index `[0]` is not used.) Each starts at 0 at power-up and, while it is greater than 0, decrements by 1 on every control cycle. On reaching 0 the counter stays at 0 — it stops, it does not wrap or go negative. They are read/write, so a user program writes a starting value and then watches for the counter to reach 0.

## How it works

The two counters are decremented together, once per control loop, in the same place the firmware maintains its other periodic timers. The control loop runs about 1024 times per second (roughly once per millisecond), so a value written to a counter elapses in approximately that many milliseconds. Each counter is guarded so it only decrements while positive; once it hits 0 it holds there until written again.

This makes `CounterDown` a convenient self-clearing timer or delay inside a user program: write the number of cycles to wait, then test for the counter being 0 to detect that the interval has elapsed. For example, writing 1000 counts down roughly one second.

For one-second-resolution wall-clock timing use [Time](Time.md); for sub-microsecond intervals use [HWTimer](HWTimer.md); for a free-running count that increases use [CounterUp](CounterUp.md).

## Examples

```text
ACounterDown[1]=1000 ; count down 1000 control cycles (about 1 second)
ACounterDown[1]      ; read the remaining count; 0 means the interval has elapsed
ACounterDown[2]=50   ; second, independent down-counter (about 50 ms)
```

## See also

- [CounterUp](CounterUp.md) — cycle-based up-counters
- [Time](Time.md) / [HWTimer](HWTimer.md) — wall-clock and high-resolution timers
