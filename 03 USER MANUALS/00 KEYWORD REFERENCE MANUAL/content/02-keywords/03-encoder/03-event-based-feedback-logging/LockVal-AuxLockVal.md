---
summary: Records the feedback position of the most recent logged digital event.
---
# LockVal/AuxLockVal

Records the feedback position of the most recent logged digital event.

## Overview

`LockVal` holds the feedback position latched at the most recent trigger event (the event source is set by [LockSrc](LockSrc-AuxLockSrc.md)). It is reported in user units. Each event also appends this value to the position history array [LockValTable](LockValTable-LockValTabB.md) at index [LockCntr](LockCntr-AuxLockCntr.md). `AuxLockVal` is the auxiliary-encoder counterpart.

`LockVal` is read-only and keeps updating on every trigger event even after the history tables are full.

## How it works

How the position is captured depends on the encoder type:

- **Digital incremental / SIN-COS encoders** — the encoder counter is latched in hardware at the exact instant of the trigger edge. The firmware reads that latched count and offsets it to user feedback units, so `LockVal` is precise to the trigger moment and unaffected by control-cycle jitter. This is the intended use for registration / probing.
- **Absolute / other non-incremental encoders** — hardware latching is not available, so `LockVal` is set to the most recent polled feedback position ([Pos](../../10-motion/01-kinematics-status/Pos.md)). The trigger must persist long enough to be seen at the control-cycle rate, and the captured value is exact to the position at the polling instant but slightly delayed relative to the true trigger instant. For this method, keep axis speed low enough that an index/trigger is not missed between control cycles.

The captured value is referenced to the same feedback pipeline as [Pos](../../10-motion/01-kinematics-status/Pos.md): the firmware compensates for the offset between the raw hardware capture counter and the user-unit feedback value, so `LockVal` is directly comparable to `Pos`.

## Examples

```text
ALockVal             ; read the position of the most recent captured event
```

## See also

- [LockSrc](LockSrc-AuxLockSrc.md) — defines the trigger event that updates `LockVal`
- [LockValTable](LockValTable-LockValTabB.md) — history array of captured positions
- [LockCntr](LockCntr-AuxLockCntr.md) — count of captured events
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — the feedback position that is captured
