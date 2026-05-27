---
summary: History arrays storing the controller-cycle time of each logged digital event.
---
# LockTimeTable/LockTimeTabB

History arrays storing the controller-cycle time of each logged digital event.

## Overview

`LockTimeTable` and `LockTimeTabB` store the time at which each trigger event occurs, expressed as the number of control cycles elapsed since feedback logging was enabled (the elapsed-cycle timer is reset to 0 when [LockEn](LockEn-AuxLockEn.md) goes from disabled to enabled, and increments once per control cycle). They are the time-stamp companions of the position history arrays [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB`, written at the same index, [LockCntr](LockCntr-AuxLockCntr.md). When `LockTimeTable` fills, recording continues into `LockTimeTabB`.

To convert a stored value to seconds, multiply by the control-cycle period (the control sampling interval).

## How it works

Both arrays are 1-indexed. On each event the firmware increments [LockCntr](LockCntr-AuxLockCntr.md) and writes the timer into the array selected by the counter. The capacity is product-dependent: each array holds 50 entries on standalone products and 65000 entries on Central-i products.

**Standalone** (50 + 50 = 100 events):

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq LockCntr \leq 50$ | LockTimeTable | $LockCntr$ |
| $51 \leq LockCntr \leq 100$ | LockTimeTabB | $LockCntr - 50$ |

**Central-i** (65000 + 65000 = 130000 events):

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq LockCntr \leq 65000$ | LockTimeTable | $LockCntr$ |
| $65001 \leq LockCntr \leq 130000$ | LockTimeTabB | $LockCntr - 65000$ |

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
