---
summary: History arrays storing the before-map feedback position of each logged digital event, on Central-i masters built with the lock FIFO.
last_updated: '2026-10-20'
doc_revision: '2026.10'
---
# LockBMapTable/LockBMapTabB

History arrays storing the before-map feedback position of each logged digital event, on Central-i masters built with the lock FIFO.

## Overview

`LockBMapTable` (CAN code 958) and `LockBMapTabB` (CAN code 959) store, for each logged trigger event, the captured feedback position **before error mapping** (the value of `LockValBefMap`, CAN code 957), in user units. They are the before-map companions of [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB`: the same event is written at the same index, so `LockBMapTable[n]` and `LockValTable[n]` describe the same capture, before and after mapping.

Both arrays are read-only, per axis and not saved to flash.

**Availability:** only on Central-i masters whose firmware is built with the lock FIFO (compile switch `CFG_CI_LOCK_FIFO = 1`, off by default). In every other build, CAN codes 958 and 959 are unused placeholders and reading them returns an error.

## How it works

Both arrays are 1-indexed. On each event the firmware increments [LockCntr](LockCntr-AuxLockCntr.md) and writes the before-map position into the array selected by the counter, at the same index as [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB` and [LockTimeTable](LockTimeTable-LockTimeTabB.md) / `LockTimeTabB`:

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq \text{LockCntr} \leq 65000$ | LockBMapTable | $\text{LockCntr}$ |
| $65001 \leq \text{LockCntr} \leq 130000$ | LockBMapTabB | $\text{LockCntr} - 65000$ |

Once both arrays are full, logging stops while [LockCntr](LockCntr-AuxLockCntr.md) and [LockVal](LockVal-AuxLockVal.md) keep updating, exactly as for `LockValTable`.

Each entry is 32 bits wide, like `LockValTable`. On Central-i masters the position itself is 64 bits wide, so an entry holds the low 32 bits of the before-map position.

## Examples

```text
ALockBMapTable[1]    ; read the before-map position of the first logged event
ALockValTable[1]     ; the same event after error mapping
```

## See also

- [LockValTable](LockValTable-LockValTabB.md) — mapped position history arrays (same indexing scheme)
- [LockTimeTable](LockTimeTable-LockTimeTabB.md) — time-stamp history arrays (same indexing scheme)
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter used as the array index
- [LockVal](LockVal-AuxLockVal.md) — the mapped position of the most recent event
