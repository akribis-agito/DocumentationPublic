---
summary: Enables or disables event-based feedback logging.
---
# LockEn/AuxLockEn

Enables or disables event-based feedback logging.

## Overview

`LockEn` enables or disables the event-based feedback logging feature: `LockEn=0` disables it and `LockEn=1` enables it. When enabled, an internal timer starts from 0 and each digital event (defined by [LockSrc](LockSrc-AuxLockSrc.md)) records the encoder feedback position and event time. Enabling from the disabled state resets the event counter [LockCntr](LockCntr-AuxLockCntr.md) to 0. `AuxLockEn` is the auxiliary-encoder counterpart.

## How it works

| LockEn | State |
|---|---|
| 0 | Event-based feedback logging disabled |
| 1 | Event-based feedback logging enabled |

## Examples

```text
LockEn=1            ; enable event-based feedback logging
LockEn=0            ; disable logging
```

## See also

- [LockSrc](LockSrc-AuxLockSrc.md) — defines the digital event source
- [LockCntr](LockCntr-AuxLockCntr.md) — event counter, reset on enable
- [LockVal](LockVal-AuxLockVal.md) — last logged feedback position
