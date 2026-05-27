---
summary: Number of least significant bits removed (right-shifted) from the absolute encoder reading.
---
# EncAbsMB/AuxEncAbsMB

Number of least significant bits removed (right-shifted) from the absolute encoder reading.

## Overview

`EncAbsMB` defines the number of least significant bits removed from the absolute encoder reading: the raw reading is right-shifted by this number of bits. It is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is set to an absolute encoder (`EncType=3`, EnDat 2.2, or `EncType=6`, BiSS-C). Masking off low-order bits discards unused or noisy lower resolution bits so that the reported position uses only the meaningful bits. `AuxEncAbsMB` is the auxiliary-encoder counterpart and operates the same way.

## How it works

The reported value is the raw encoder reading shifted right by `EncAbsMB` bits:

$$Reading_{masked} = Reading_{raw} \gg EncAbsMB$$

## Examples

```text
AEncAbsMB=2          ; discard the 2 least significant bits of the reading
```

## See also

- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — total number of bits of the absolute encoder
- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — raw value after this masking and direction handling
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset applied to the raw reading
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsMB` applies for absolute encoders
