---
summary: History arrays storing the feedback position of each logged digital event.
---
# LockValTable/LockValTabB

History arrays storing the feedback position of each logged digital event.

## Overview

`LockValTable` and `LockValTabB` store the feedback position captured at each trigger event (i.e. each successive value of [LockVal](LockVal-AuxLockVal.md)), in user units. They are written at the running index [LockCntr](LockCntr-AuxLockCntr.md) and are the position companions of the time-stamp arrays [LockTimeTable](LockTimeTable-LockTimeTabB.md) / `LockTimeTabB`. When `LockValTable` fills, recording continues into `LockValTabB`.

## How it works

Both arrays are 1-indexed and written at the same index as their time-stamp companions. On each event the firmware increments [LockCntr](LockCntr-AuxLockCntr.md) and writes [LockVal](LockVal-AuxLockVal.md) into the array selected by the counter. The capacity is product-dependent: each array holds 50 entries on standalone products and 65000 entries on Central-i products.

**Standalone** (50 + 50 = 100 events):

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 50$ | LockValTable | $\text{LockCntr}$ |
| $51 \leq \text{LockCntr} \leq 100$ | LockValTabB | $\text{LockCntr} - 50$ |

**Central-i** (65000 + 65000 = 130000 events):

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 65000$ | LockValTable | $\text{LockCntr}$ |
| $65001 \leq \text{LockCntr} \leq 130000$ | LockValTabB | $\text{LockCntr} - 65000$ |

Once both arrays are full, position logging stops while [LockCntr](LockCntr-AuxLockCntr.md) and [LockVal](LockVal-AuxLockVal.md) keep updating.

## Examples

On a Central-i product, when an event triggers logging and `LockCntr` reaches 71000, `LockValTabB[6000]` stores the captured position. On a standalone product, when `LockCntr` reaches 71, `LockValTabB[21]` is used.

```text
ALockValTable[1]     ; read the captured position of the first event
```

## See also

- [LockVal](LockVal-AuxLockVal.md) — the value stored into these arrays
- [LockTimeTable](LockTimeTable-LockTimeTabB.md) — time-stamp history arrays (same indexing scheme)
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter used as the array index
