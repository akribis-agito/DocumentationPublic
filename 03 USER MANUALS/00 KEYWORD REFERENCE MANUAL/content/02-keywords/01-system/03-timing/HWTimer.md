---
keyword: HWTimer
summary: High-resolution free-running counter for measuring short intervals.
availability:
  standalone: []
  central-i:
  - v5
can_code: 768
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# HWTimer

High-resolution free-running counter for measuring short intervals.

## Overview

`HWTimer` is a fast, read-only, free-running counter for timing short intervals at sub-microsecond resolution. It ticks about 433 times per microsecond (one count roughly every 1/433 µs). Read it at two moments and subtract the two readings to get the elapsed time between events. The counter wraps after roughly 9.9 seconds, so it is intended for short intervals only; for longer or coarse timing use [Time](Time.md), and for counting in whole control cycles use [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md).

`HWTimer` exists only on the central-i platform (firmware v5).

## How it works

`HWTimer` is not a software counter that the firmware increments; reading it returns the current value of a hardware timer register on the processor. That register counts continuously at the processor's timer clock (about 433 MHz), which is why it offers far finer resolution than the one-second [Time](Time.md) tick or the per-cycle counters.

To convert a difference of two readings into time:

$$
\Delta t\ [\mu\text{s}] = \dfrac{\text{HWTimer}_{\text{end}} - \text{HWTimer}_{\text{start}}}{433}
$$

Because the value is a 32-bit register, it rolls over after about $2^{32} / (433 \cdot 10^6) \approx 9.9$ seconds. As long as the interval being measured is shorter than that and the subtraction is done with unsigned/wrapping arithmetic, a single rollover between the two readings still yields the correct difference. Intervals longer than one full wrap cannot be measured with `HWTimer`.

## Examples

```text
AHWTimer            ; read the counter at event A, again at event B, then subtract
```

Read `AHWTimer` immediately before and after a short operation; the count difference divided by 433 gives the duration in microseconds.

## See also

- [Time](Time.md) — seconds since power-on (coarse, one-second resolution)
- [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md) — cycle-based counters
