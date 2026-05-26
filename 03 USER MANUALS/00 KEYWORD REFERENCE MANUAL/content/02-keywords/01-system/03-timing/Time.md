---
keyword: Time
summary: Read-only seconds elapsed since power-on.
availability:
  standalone:
  - v4
  - v5
  central-i:
  - v4
  - v5
can_code: 41
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
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# Time

Read-only seconds elapsed since power-on.

## Overview

`Time` holds the number of seconds elapsed since the controller powered on. It is read-only and resets to 0 at each power-up, making it convenient for coarse, second-resolution timestamping or elapsed-time checks. For measuring short intervals at sub-microsecond resolution, use [HWTimer](HWTimer.md) instead.

## Examples

```text
Time?               ; seconds since power-on
```

## See also

- [HWTimer](HWTimer.md) — high-resolution interval timer
- [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md) — cycle-based counters
