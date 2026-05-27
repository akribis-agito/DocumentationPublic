---
summary: Raw absolute encoder value after bit-masking and direction handling.
---
# EncAbsVal/AuxEncAbsVal

Raw absolute encoder value after bit-masking and direction handling.

## Overview

`EncAbsVal` is the raw value of the absolute encoder after bit-masking ([EncAbsMB](EncAbsMB-AuxEncAbsMB.md)) and direction control ([EncDir](EncDir-AuxEncDir.md)) have been applied. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is set to an absolute encoder (`EncType=3`, EnDat 2.2, or `EncType=6`, BiSS-C). It lets the user inspect the processed absolute reading. `AuxEncAbsVal` is the auxiliary-encoder counterpart and operates the same way.

## Examples

```text
EncAbsVal?          ; read the processed raw absolute value
```

## See also

- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — bit-masking applied before this value
- [EncDir](EncDir-AuxEncDir.md) — direction handling applied to the reading
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset applied to the raw reading
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsVal` applies for absolute encoders
