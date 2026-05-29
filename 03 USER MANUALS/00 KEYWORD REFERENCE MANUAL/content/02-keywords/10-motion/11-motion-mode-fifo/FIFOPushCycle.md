---
keyword: FIFOPushCycle
summary: Pushes a cycle-time (segment-duration) entry into the FIFO motion queue.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 284
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 1
  - 65536000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FIFOPushCycle

Pushes a cycle-time (segment-duration) entry into the FIFO motion queue.

## Overview

`FIFOPushCycle` appends a **cycle-time** entry (type 5 in [FIFOType](FIFOType.md)) to the queue. The value is a segment duration in control samples. When the controller reaches this entry during playback it is consumed without producing motion: it updates [FIFOCycleTime](FIFOCycleTime.md), which then applies to every segment queued after it, until the next cycle-time entry. This lets the segment length vary through a streamed sequence.

It is one of the `FIFOPush*` functions used to fill the queue before or during motion. The entry is added at the tail of the queue. If the queue is full (no free entries), the push is rejected with an error.

See [FIFOType](FIFOType.md) for a full description of FIFO motion mode and all related keywords.

## How it works

A push writes the supplied value into the next free queue slot, tags it as a cycle-time entry, and decrements the free-entry count reported by [FIFOStatus](FIFOStatus.md) (index 2). Because a cycle-time entry occupies a queue slot, interleaving many of them reduces the number of slots left for motion segments (128 usable in total).

## Changes between versions

| | v4 (standalone &amp; central-i) | v5 (central-i) |
|---|---|---|
| Accepted range | unrestricted | 1 to 65 536 000 |

In **v5** the pushed cycle time is bounded to 1–65 536 000 control samples. **v5 is central-i only.**

## Examples

```text
AFIFOPushCycle=16    ; queue a cycle-time entry of 16 control samples
```

## See also

- [FIFOCycleTime](FIFOCycleTime.md) — current segment duration
- [FIFOPushLinP](FIFOPushLinP.md), [FIFOPushLinV](FIFOPushLinV.md) — push linear segments
- [FIFOPushParP](FIFOPushParP.md), [FIFOPushParA](FIFOPushParA.md) — push parabolic segments
- [FIFOType](FIFOType.md) — full FIFO mode description
