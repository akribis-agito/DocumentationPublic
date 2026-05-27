---
summary: Records the feedback position of the most recent logged digital event.
---
# LockVal/AuxLockVal

Records the feedback position of the most recent logged digital event.

## Overview

`LockVal` records the latest feedback position where a digital event was triggered (as defined by [LockSrc](LockSrc-AuxLockSrc.md)). Each event also appends this value to the position history array [LockValTable](LockValTable-LockValTabB.md). `AuxLockVal` is the auxiliary-encoder counterpart.

## Examples

```text
LockVal?            ; read the position of the most recent event
```

## See also

- [LockSrc](LockSrc-AuxLockSrc.md) — defines the digital event that updates `LockVal`
- [LockValTable](LockValTable-LockValTabB.md) — history array of logged positions
- [LockCntr](LockCntr-AuxLockCntr.md) — count of logged events
