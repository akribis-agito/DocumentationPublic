---
summary: Counts digital events and serves as the index into the feedback-logging history arrays.
---
# LockCntr/AuxLockCntr

Counts digital events and serves as the index into the feedback-logging history arrays.

## Overview

`LockCntr` tracks the number of digital events encountered, as defined by [LockSrc](LockSrc-AuxLockSrc.md). It is also used as the index for populating the history arrays [LockValTable](LockValTable-LockValTabB.md) and [LockTimeTable](LockTimeTable-LockTimeTabB.md). `LockCntr` increments by 1 each time a digital event occurs. `AuxLockCntr` is the auxiliary-encoder counterpart.

`LockCntr` is reset to 0 when the logging feature ([LockEn](LockEn-AuxLockEn.md)) is enabled from the disabled state. The user can write any value to `LockCntr` so that the history arrays are populated at a desired index.

## Examples

```text
LockCntr?           ; read the number of events logged
LockCntr=0          ; reset the history-array index
```

## See also

- [LockEn](LockEn-AuxLockEn.md) — enables logging; resets `LockCntr` to 0
- [LockSrc](LockSrc-AuxLockSrc.md) — defines the digital event that increments `LockCntr`
- [LockValTable](LockValTable-LockValTabB.md) / [LockTimeTable](LockTimeTable-LockTimeTabB.md) — history arrays indexed by `LockCntr`
