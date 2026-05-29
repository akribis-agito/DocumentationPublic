---
keyword: FIFOCycleTime
summary: Duration, in control samples, of the FIFO motion segment currently being executed.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 283
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 65536000
  default: 65536
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOCycleTime

Duration, in control samples, of the FIFO motion segment currently being executed.

## Overview

`FIFOCycleTime` is the duration of each FIFO motion segment, expressed as a number of control-loop samples. It governs how long the controller spends interpolating across one segment before taking the next entry from the queue. The default is 65536 samples.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

The cycle time takes effect only at a segment boundary — when the controller finishes one segment and is about to start the next. It is not applied mid-segment, so changing it never disturbs the segment in progress.

`FIFOCycleTime` is **read-only**; it is updated from the queue: a cycle-time entry pushed with [FIFOPushCycle](FIFOPushCycle.md) becomes the active cycle time when the controller reaches it, and applies to every segment that follows until the next cycle-time entry. This is how segment lengths are varied through a sequence.

When a segment begins, its sample count-down is loaded from the cycle time (see [FIFOStatus](FIFOStatus.md) index 3) and the per-sample motion is derived from it — for a position-delta segment, for example, the requested delta is divided across this many samples.

## Changes between versions

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Accepted range | unrestricted | 1 to 65 536 000 |

In **v5** the cycle time is bounded to 1–65 536 000 control samples. **v5 is central-i only.**

## Examples

```text
AFIFOCycleTime            ; read the current segment duration in control samples
AFIFOPushCycle=16         ; queue a cycle-time entry so the next segment lasts 16 samples
```

## See also

- [FIFOType](FIFOType.md) — full FIFO mode description
- [FIFOPushCycle](FIFOPushCycle.md) — push a cycle-time entry into the queue
- [FIFOStatus](FIFOStatus.md) — samples remaining in the active segment (index 3)
