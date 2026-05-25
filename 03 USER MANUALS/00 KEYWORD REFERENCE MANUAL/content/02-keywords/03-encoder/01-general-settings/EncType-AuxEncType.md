# EncType/AuxEncType

**Definition:**

EncType defines the encoder feedback type as listed below.

| Value | Encoder type                            | Category                    |
|-------|-----------------------------------------|-----------------------------|
| 0     | Reserved                                | \-                          |
| 1     | Incremental – TTL                       | Digital incremental encoder |
| 2     | Absolute – SSI (not supported)          | Absolute encoder            |
| 3     | Absolute – EnDat 2.2                    | Absolute encoder            |
| 4     | Incremental – SINCOS                    | Analog SIN/COS encoder      |
| 5     | Absolute – Nikon 17-bit (not supported) | Absolute encoder            |
| 6     | Absolute – BiSS-C                       | Absolute encoder            |
| 7     | Analog position feedback                | Others                      |
| 8     | Absolute – Tamagawa                     | Absolute encoder            |

For digital incremental encoder, please also refer to the [EncSubType](../../../02-keywords/03-encoder/01-general-settings/EncSubType-AuxEncSubType.md) and [EncFilt](../../../02-keywords/03-encoder/01-general-settings/EncFilt-AuxEncFilt.md).

For absolute encoder, please also refer to the parameters [EncAbsBits](../../../02-keywords/03-encoder/01-general-settings/EncAbsBits-AuxEncAbsBits.md), [EncAbsMB](../../../02-keywords/03-encoder/01-general-settings/EncAbsMB-AuxEncAbsMB.md), [EncAbsOff](../../../02-keywords/03-encoder/01-general-settings/EncAbsOff-AuxEncAbsOff.md) and [EncAbsVal](../../../02-keywords/03-encoder/01-general-settings/EncAbsVal-AuxEncAbsVal.md).

For analog SIN/COS encoder, please also refer to the parameters [SinCosSetup](../../../02-keywords/03-encoder/01-general-settings/SinCosSetup-AuxSinCosSet.md) and [SinCosSignals](../../../02-keywords/03-encoder/01-general-settings/SinCosSignals-AuxSinCosSig.md).
