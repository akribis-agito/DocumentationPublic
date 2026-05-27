---
summary: Offset added to the raw absolute encoder reading.
---
# EncAbsOff/AuxEncAbsOff

Offset added to the raw absolute encoder reading.

## Overview

`EncAbsOff` defines the offset applied to the raw reading of the absolute encoder. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is set to an absolute encoder (`EncType=3`, EnDat 2.2, or `EncType=6`, BiSS-C). The offset is used to align the absolute position reported by the encoder with the desired machine zero. `AuxEncAbsOff` is the auxiliary-encoder counterpart and operates the same way.

## Examples

```text
AEncAbsOff=1000      ; add an offset of 1000 to the raw absolute reading
```

## See also

- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — total number of bits of the absolute encoder
- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — least significant bits removed from the reading
- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — raw value after masking and direction handling
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsOff` applies for absolute encoders
