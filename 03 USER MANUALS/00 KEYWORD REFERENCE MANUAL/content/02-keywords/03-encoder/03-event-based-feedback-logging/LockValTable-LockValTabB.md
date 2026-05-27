---
summary: History arrays storing the feedback position of each logged digital event.
---
# LockValTable/LockValTabB

History arrays storing the feedback position of each logged digital event.

## Overview

`LockValTable` and `LockValTabB` store the feedback position when each digital event is triggered (i.e. the value of [LockVal](LockVal-AuxLockVal.md)). They are indexed by the event counter [LockCntr](LockCntr-AuxLockCntr.md), and are the position companions of the time-stamp arrays [LockTimeTable](LockTimeTable-LockTimeTabB.md) / `LockTimeTabB`. When `LockValTable` fills, recording continues into `LockValTabB`.

## How it works

`LockValTable` and `LockValTabB` are populated based on `LockCntr`:

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq LockCntr \leq 65000$ | LockValTable | $LockCntr$ |
| $65001 \leq LockCntr \leq 130000$ | LockValTabB | $LockCntr - 65000$ |

## Examples

When an event triggers feedback logging and `LockCntr` reaches 71000, `LockValTabB[6000]` is used to store the updated `LockVal`.

```text
LockValTable[1]?        ; read the position of the first logged event
```

## See also

- [LockVal](LockVal-AuxLockVal.md) — the value stored into these arrays
- [LockTimeTable](LockTimeTable-LockTimeTabB.md) — time-stamp history arrays (same indexing scheme)
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter used as the array index
