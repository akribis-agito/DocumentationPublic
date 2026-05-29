---
keyword: Time
summary: Read-only seconds elapsed since power-on.
availability:
  standalone:
  - v4
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

`Time` holds the number of whole seconds elapsed since the controller powered on (or was reset). It is read-only, unit-wide (non-axis), not saved to flash, and resets to 0 at every power-up. Use it for coarse, second-resolution timestamping or elapsed-time checks. For measuring short intervals at sub-microsecond resolution use [HWTimer](HWTimer.md); for cycle-accurate counting use [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md).

`Time` is the timestamp source for the error log: each entry in [ErrLog](../../07-status-and-faults/ErrLog.md) stores a copy of `Time` (seconds since power-on) alongside the error code.

## How it works

The control interrupt runs at a fixed sample rate (16384 samples per second). A free-running sample counter advances inside the control loop, and when it reaches one second's worth of samples the counter is cleared and `Time` is incremented by 1. Because the increment is driven by the sample clock, the resolution is exactly one second and the count is monotonic for the life of the power cycle.

`Time` is a signed 32-bit value. Incrementing once per second it would take on the order of decades of continuous run-time to approach its positive maximum (2147483647), so rollover is not a practical concern.

Note on accuracy: `Time` measures elapsed seconds by counting the controller's own control-loop samples (16384 nominal samples = one second), not against a separate real-time clock. The physical sample rate is slightly faster than the nominal 16384 Hz, so `Time` advances a little faster than true wall-clock time. The error is small but accumulates over long uptimes — on the order of seconds per day — so `Time` is suitable for relative elapsed-time measurement and coarse timestamping, but should not be relied on as an accurate absolute clock over long periods.

Worked examples (uptime conversions):

| `Time` value | Elapsed run-time |
|-------------:|------------------|
| 60           | 1 minute         |
| 3600         | 1 hour           |
| 86400        | 1 day            |
| 604800       | 1 week           |
| 2147483647   | ≈ 68 years (signed 32-bit maximum) |

## Examples

```text
ATime               ; seconds since power-on (e.g. 86400 -> 1 day of uptime)
```

Measure how long an operation took, at one-second resolution, by reading `ATime` before and after and subtracting.

## See also

- [HWTimer](HWTimer.md) — high-resolution (sub-microsecond) interval timer
- [CounterUp](CounterUp.md) / [CounterDown](CounterDown.md) — cycle-based counters
- [ErrLog](../../07-status-and-faults/ErrLog.md) — error log that timestamps each entry with `Time`
