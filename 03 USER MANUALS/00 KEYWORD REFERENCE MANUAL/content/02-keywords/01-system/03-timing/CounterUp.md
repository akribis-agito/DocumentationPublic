---
keyword: CounterUp
summary: Two independent up-counters incremented every controller cycle.
availability:
  standalone:
  - v4
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

`CounterUp` provides two independent general-purpose up-counters, `CounterUp[1]` and `CounterUp[2]`. (The array is dimensioned for three elements so that the usable indices start at `[1]`; index `[0]` is not used.) Each counter starts at 0 at power-up and increments by 1 on every control cycle. They are read/write, so a user program can preset or reset either counter at any time, then read it later to count or time events in units of control cycles.

## How it works

The two counters are advanced together inside the control interrupt, in the same place the firmware maintains its other periodic timers. The control interrupt runs at **16384 samples per second** (one tick every 61.04 µs), so each counter increases by 16384 every second of run-time. Counting up is unbounded: on reaching the signed 32-bit maximum (2147483647) a counter wraps to −2147483648 and keeps incrementing.

Worked examples:

- One second of elapsed time = 16384 control cycles.
- One millisecond ≈ 16 control cycles (16384 / 1000 ≈ 16.4).
- A free-running `CounterUp[1]` started at 0 reaches 2 147 483 647 after about 2147483647 / 16384 / 86400 ≈ 1.5 days of run-time before it wraps to −2147483648.

Typical uses:

- Reset a counter to 0, run an operation, then read the counter to measure how many control cycles (61.04 µs each) it took.
- Preset a counter and watch for it to reach a target value as a simple elapsed-cycle trigger inside a user program.

For one-second-resolution wall-clock timing use [Time](Time.md); for sub-microsecond intervals use [HWTimer](HWTimer.md); for counting *down* to a target use [CounterDown](CounterDown.md).

## Examples

```text
ACounterUp[1]       ; read the first up-counter
ACounterUp[1]=0     ; reset the first up-counter, then read it later to measure elapsed cycles
ACounterUp[2]       ; read the second, independent up-counter
```

For example, if `ACounterUp[1]` reads `16384` after a reset, exactly one second of run-time has passed.

## See also

- [CounterDown](CounterDown.md) — cycle-based down-counters
- [Time](Time.md) / [HWTimer](HWTimer.md) — wall-clock and high-resolution timers
