---
summary: Selects the encoder feedback type (incremental, SIN/COS, absolute, or analog).
---
# EncType/AuxEncType

Selects the encoder feedback type for the axis.

## Overview

`EncType` defines the encoder feedback type. It tells the controller how to read and decode the position feedback hardware connected to the axis, which in turn determines which additional configuration keywords apply (subtype and filter for incremental, absolute-encoder parameters, or SIN/COS setup). `AuxEncType` is the auxiliary-encoder counterpart and operates the same way.

## How it works

| Value | Encoder type                            | Category                    |
|-------|-----------------------------------------|-----------------------------|
| 0     | Reserved                                | -                           |
| 1     | Incremental – TTL                       | Digital incremental encoder |
| 2     | Absolute – SSI (not supported)          | Absolute encoder            |
| 3     | Absolute – EnDat 2.2                    | Absolute encoder            |
| 4     | Incremental – SINCOS                    | Analog SIN/COS encoder      |
| 5     | Absolute – Nikon 17-bit (not supported) | Absolute encoder            |
| 6     | Absolute – BiSS-C                       | Absolute encoder            |
| 7     | Analog position feedback                | Others                      |
| 8     | Absolute – Tamagawa                     | Absolute encoder            |

For a digital incremental encoder, also refer to [EncSubType](EncSubType-AuxEncSubType.md) and [EncFilt](EncFilt-AuxEncFilt.md).

For an absolute encoder, also refer to [EncAbsBits](EncAbsBits-AuxEncAbsBits.md), [EncAbsMB](EncAbsMB-AuxEncAbsMB.md), [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and [EncAbsVal](EncAbsVal-AuxEncAbsVal.md).

For an analog SIN/COS encoder, also refer to [SinCosSetup](SinCosSetup-AuxSinCosSet.md) and [SinCosSignals](SinCosSignals-AuxSinCosSig.md).

## Examples

```text
EncType=1           ; incremental TTL encoder
EncType=4           ; SIN/COS encoder
EncType=6           ; BiSS-C absolute encoder
```

## See also

- [EncSubType](EncSubType-AuxEncSubType.md) — incremental encoder subtype (`EncType=1`)
- [EncFilt](EncFilt-AuxEncFilt.md) — incremental input filter (`EncType=1`)
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) / [SinCosSignals](SinCosSignals-AuxSinCosSig.md) — SIN/COS configuration and status (`EncType=4`)
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — absolute encoder bit count (absolute types)
