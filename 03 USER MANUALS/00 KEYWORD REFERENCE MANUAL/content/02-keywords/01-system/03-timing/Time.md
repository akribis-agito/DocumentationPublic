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

The control interrupt runs at a fixed sample rate (16384 samples per second). A free-running sample accumulator advances inside the control loop, and when it reaches one second's worth of samples the accumulator is cleared and `Time` is incremented by 1. Because the increment is driven by the sample clock, the resolution is exactly one second and the count is monotonic for the life of the power cycle.

The seconds bookkeeping is not done on every one of the 16384 cycles. The non-time-critical part of each control interrupt runs a round-robin that steps through 16 sub-phases, advancing one phase per cycle and wrapping every 16 cycles. The seconds accumulator is advanced on just one of those phases, by +16 each time it runs (so it still totals 16384 per second), and rolls `Time` over when it reaches 16384. That gives 16384 / 16 = 1024 accumulation steps per second, i.e. a roughly one-millisecond effective tick for the seconds counter, even though the underlying sample clock is 16384 Hz. The per-control-cycle counters [CounterUp](CounterUp.md) and [CounterDown](CounterDown.md) are by contrast advanced unconditionally on every single cycle, so they retain full 16384 Hz resolution.

`Time` is a signed 32-bit value. Incrementing once per second it would take on the order of decades of continuous run-time to approach its positive maximum (2147483647), so rollover is not a practical concern.

Note on accuracy: `Time` measures elapsed seconds by counting the controller's own control-loop samples (16384 nominal samples = one second), not against a separate real-time clock. The physical sample rate is slightly faster than the nominal 16384 Hz: the rate has been measured at 16386.8 Hz, i.e. the nominal value is short of the true rate by the ratio 16384 / 16386.8 = 0.999829131 (the clock runs about 0.0171 % fast). Because `Time` increments once per 16384 samples regardless of the true rate, it advances faster than true wall-clock time by the same fraction, gaining on the order of 14–15 seconds per real day (≈ 14.77 s/day). The error is small but accumulates over long uptimes, so `Time` is suitable for relative elapsed-time measurement and coarse timestamping, but should not be relied on as an accurate absolute clock over long periods.

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
