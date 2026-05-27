---
keyword: DualStuckTime
summary: Consecutive cycles the dual-loop feedback mismatch may persist before tripping.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 158
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 2147483647
  default: 4096
  scaling: 1.0
  implemented: final
overrides: {}
---
# DualStuckTime

Consecutive cycles the dual-loop feedback mismatch may persist before tripping.

## Overview

`DualStuckTime` is how long the dual-loop feedback mismatch may persist before the dual-stuck fault fires. The keyword carries a samples-to-milliseconds scaling, and internally it is compared against a sample counter (1 control sample ≈ 61 µs). The default is `4096`.

## How it works

When dual-loop is enabled, each control sample the firmware tests whether the two feedbacks' velocity difference exceeds [DualStuckVel](DualStuckVel.md):

```text
increment the dual-stuck counter
if the dual-stuck counter has reached DualStuckTime
    turn the axis off and log the fault
```

- The internal counter increments once per sample for as long as the mismatch exceeds `DualStuckVel`; any in-tolerance sample resets it to `0`. The fault requires a single unbroken run of `DualStuckTime`.
- On reaching the threshold, the axis is turned off and [ConFlt](../../../07-status-and-faults/ConFlt.md) records fault code 1049 (dual-loop stuck).
- The whole check is gated on `DualLoopOn`, so on single-loop axes the counter never runs.

A larger `DualStuckTime` tolerates longer transient divergences (e.g. during aggressive transients where the two feedbacks momentarily disagree); a smaller value reacts faster to a genuinely slipping or broken coupling.

## Examples

```text
ADualStuckTime[1]=4096   ; how long the feedback mismatch may persist before tripping
ADualStuckTime[1]        ; read back
```

## See also

- [DualStuckVel](DualStuckVel.md) — the tolerated velocity-difference threshold
- [ConFlt](../../../07-status-and-faults/ConFlt.md) — records fault code 1049 (dual-loop stuck)
