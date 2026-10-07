---
summary: Counts digital events and serves as the index into the feedback-logging history arrays.
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# LockCntr/AuxLockCntr

Counts digital events and serves as the index into the feedback-logging history arrays.

## Overview

`LockCntr` tracks the number of trigger events captured since logging was armed, as defined by [LockSrc](LockSrc-AuxLockSrc.md). It also acts as the running index for the history arrays [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) (and their B-tables). `LockCntr` increments by 1 each time a trigger event is captured (see below for edges that share a control cycle). `AuxLockCntr` is the auxiliary-encoder counterpart.

`LockCntr` is reset to `0` when logging ([LockEn](LockEn-AuxLockEn.md)) is enabled from the disabled state. It is writable, so you can preset it to populate the history arrays starting at a chosen index, or reset it to overwrite from the beginning of the tables.

## How it works

On each trigger event the firmware first increments `LockCntr`, then stores the captured position ([LockVal](LockVal-AuxLockVal.md)) and the elapsed-cycle time into the history arrays at index `LockCntr`. Because the counter is pre-incremented, the first event lands at index `1` (index `0` is unused), which is why the arrays are 1-indexed.

### Table capacity (product-dependent)

The number of events that can be stored in the history arrays depends on the product:

| Product family | LockValTable / LockTimeTable | LockValTabB / LockTimeTabB | Total events stored |
|---|--:|--:|--:|
| Standalone | 50 | 50 | 100 |
| Central-i | 65000 | 65000 | 130000 |

While `LockCntr` is within the first table's capacity the event is stored in [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md); once it exceeds that, recording continues into the B-tables ([LockValTabB](LockValTable-LockValTabB.md) / [LockTimeTabB](LockTimeTable-LockTimeTabB.md)). Once **both** tables are full the history logging stops, but `LockCntr` and [LockVal](LockVal-AuxLockVal.md) keep updating on every further event — so the counter and the latest captured value remain live even after the buffers are exhausted.

`LockCntr` itself is a 32-bit counter and does not wrap in any practical run; it is the *table index* that is bounded by the capacities above.

### One event recorded per control cycle

The counter is serviced once per control cycle, and at most one capture is recorded per cycle. The hardware keeps only the most recent captured position from a cycle, so edges that share a control cycle share one capture.

On Central-i masters, if more than one trigger edge occurs within a single control cycle, `LockCntr` advances by one with the position of the last edge, and [LockLost](LockLost.md) advances by one. The earlier edges in that cycle are not counted or stored separately. Central-i firmware without `LockLost` ignored such a cycle: `LockCntr` did not advance. An edge that arrives while the position of the previous edge is still being read is read afterwards and recorded as its own entry, and `LockLost` does not change; a further edge before that second read is made adds one to `LockLost`.

To capture every edge as a distinct entry, keep the trigger edges well apart. In a bench measurement with four events at a fixed gap on a Central-i master, every edge was recorded at gaps of 200 µs and above. Closer edges can share a capture; see [LockLost](LockLost.md).

## Examples

```text
ALockCntr            ; read the number of events captured so far
ALockCntr=0          ; reset the history-array index (overwrite from the start)
```

## See also

- [LockEn](LockEn-AuxLockEn.md) — enables logging; resets `LockCntr` to 0
- [LockSrc](LockSrc-AuxLockSrc.md) — defines the trigger event that increments `LockCntr`
- [LockLost](LockLost.md) — counts the lock samples on Central-i masters that did not become a capture of their own
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — history arrays indexed by `LockCntr`
