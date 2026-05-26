---
keyword: HWTimer
summary: High-resolution free-running counter for measuring short intervals.
---
# HWTimer

High-resolution free-running counter for measuring short intervals.

## Overview

`HWTimer` is a fast free-running counter that ticks every 1/433 of a microsecond (about 433 counts per microsecond). Read it at two moments and subtract to measure the elapsed time between events with sub-microsecond resolution. The counter wraps after roughly 9.9 seconds, so it is intended for short intervals; for longer or coarse timing use [Time](Time.md).

## Examples

```text
HWTimer?            ; read the counter at event A, again at event B, then subtract
```

## See also

- [Time](Time.md) — seconds since power-on
- [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md) — cycle-based counters
