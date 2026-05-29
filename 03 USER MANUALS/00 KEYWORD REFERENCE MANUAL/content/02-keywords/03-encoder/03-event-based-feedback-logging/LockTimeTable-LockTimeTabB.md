---
summary: History arrays storing the controller-cycle time of each logged digital event.
---
# LockTimeTable/LockTimeTabB

History arrays storing the controller-cycle time of each logged digital event.

## Overview

`LockTimeTable` and `LockTimeTabB` store the time at which each trigger event occurs, expressed as the number of control cycles elapsed since feedback logging was enabled (the elapsed-cycle timer is reset to 0 when [LockEn](LockEn-AuxLockEn.md) goes from disabled to enabled, and increments once per control cycle). They are the time-stamp companions of the position history arrays [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB`, written at the same index, [LockCntr](LockCntr-AuxLockCntr.md). When `LockTimeTable` fills, recording continues into `LockTimeTabB`.

To convert a stored value to seconds, multiply by the control-cycle period (the control sampling interval). On standard products the control loop runs at 16384 Hz, so each count is 1/16384 s ≈ 61.035 µs; on fast-sampling products it runs at 65536 Hz, so each count is 1/65536 s ≈ 15.259 µs. For example, a stored value of 1000 on a standard product corresponds to 1000 × 61.035 µs ≈ 61.0 ms after logging was enabled.

The time stamp is the elapsed-cycle count itself, so its resolution is exactly one control cycle. Two events captured in different cycles always differ by at least one count, and an event's time stamp reflects the cycle in which it was serviced rather than the exact sub-cycle instant of the trigger edge. Because at most one event is recorded per control cycle (see [LockCntr](LockCntr-AuxLockCntr.md)), any trigger edges that fall within the same cycle share that single time stamp.

## How it works

Both arrays are 1-indexed. On each event the firmware increments [LockCntr](LockCntr-AuxLockCntr.md) and writes the timer into the array selected by the counter. The capacity is product-dependent: each array holds 50 entries on standalone products and 65000 entries on Central-i products.

**Standalone** (50 + 50 = 100 events):

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 50$ | LockTimeTable | $\text{LockCntr}$ |
| $51 \leq \text{LockCntr} \leq 100$ | LockTimeTabB | $\text{LockCntr} - 50$ |

**Central-i** (65000 + 65000 = 130000 events):

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 65000$ | LockTimeTable | $\text{LockCntr}$ |
| $65001 \leq \text{LockCntr} \leq 130000$ | LockTimeTabB | $\text{LockCntr} - 65000$ |

Once both arrays are full, time-stamp logging stops while [LockCntr](LockCntr-AuxLockCntr.md) and [LockVal](LockVal-AuxLockVal.md) keep updating.

## Examples

On a Central-i product, when an event triggers logging and `LockCntr` reaches 70000, `LockTimeTabB[5000]` stores the elapsed-cycle time. On a standalone product, when `LockCntr` reaches 70, `LockTimeTabB[20]` is used.

```text
ALockTimeTable[1]    ; read the time stamp (in control cycles) of the first captured event
```

## See also

- [LockValTable](LockValTable-LockValTabB.md) — position history arrays (same indexing scheme)
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter used as the array index
- [LockEn](LockEn-AuxLockEn.md) — enables logging; resets the elapsed-cycle timer
