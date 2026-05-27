---
summary: History arrays storing the controller-cycle time of each logged digital event.
---
# LockTimeTable/LockTimeTabB

History arrays storing the controller-cycle time of each logged digital event.

## Overview

`LockTimeTable` and `LockTimeTabB` store the time at which each digital event is triggered, expressed as the number of controller cycles elapsed since feedback logging was enabled from the disabled state. They are the time-stamp companions of the position history arrays [LockValTable](LockValTable-LockValTabB.md) / `LockValTabB`, and are indexed by the event counter [LockCntr](LockCntr-AuxLockCntr.md). When `LockTimeTable` fills, recording continues into `LockTimeTabB`.

## How it works

`LockTimeTable` and `LockTimeTabB` are populated based on `LockCntr`:

| Condition | Array used | Corresponding index |
|:--:|:--:|:--:|
| $1 \leq LockCntr \leq 65000$ | LockTimeTable | $LockCntr$ |
| $65001 \leq LockCntr \leq 130000$ | LockTimeTabB | $LockCntr - 65000$ |

## Examples

When an event triggers feedback logging and `LockCntr` reaches 70000, `LockTimeTabB[5000]` is used to store the logging time.

```text
LockTimeTable[1]?       ; read the time stamp of the first logged event
```

## See also

- [LockValTable](LockValTable-LockValTabB.md) — position history arrays (same indexing scheme)
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter used as the array index
- [LockEn](LockEn-AuxLockEn.md) — enables logging; resets the elapsed-cycle timer
