---
summary: Number of bits of the absolute encoder reading.
---
# EncAbsBits/AuxEncAbsBits

Number of bits of the absolute encoder reading.

## Overview

`EncAbsBits` defines the number of bits of the absolute encoder. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is set to an absolute encoder (`EncType=3`, EnDat 2.2, or `EncType=6`, BiSS-C). The bit count tells the controller how to interpret the raw word read from the encoder before offset and direction handling are applied. `AuxEncAbsBits` is the auxiliary-encoder counterpart and operates the same way.

## Examples

```text
EncAbsBits=26       ; 26-bit absolute encoder
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsBits` applies for absolute encoders
- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — least significant bits removed from the reading
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset applied to the raw reading
- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — raw value after masking and direction handling
