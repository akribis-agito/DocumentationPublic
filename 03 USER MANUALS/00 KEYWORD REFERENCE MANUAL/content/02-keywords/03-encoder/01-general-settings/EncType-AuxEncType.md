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

Whether a given type is actually supported depends on the product hardware; selecting an unsupported type is rejected.

For a digital incremental encoder, also refer to [EncSubType](EncSubType-AuxEncSubType.md) and [EncFilt](EncFilt-AuxEncFilt.md). `EncSubType` selects the incremental decoding scheme: A/B quadrature (0), pulse/direction (1), C0/C1 (2), or up/down (3). The incremental type (`EncType=1`) is also the only type for which [EncDir](EncDir-AuxEncDir.md) and [EncFilt](EncFilt-AuxEncFilt.md) apply.

For an absolute encoder, also refer to [EncAbsBits](EncAbsBits-AuxEncAbsBits.md), [EncAbsMB](EncAbsMB-AuxEncAbsMB.md), [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and [EncAbsVal](EncAbsVal-AuxEncAbsVal.md). With an absolute encoder the feedback [Pos](../../10-motion/01-kinematics-status/Pos.md) is initialised from the absolute reading at power-up rather than starting at zero.

For an analog SIN/COS encoder, also refer to [SinCosSetup](SinCosSetup-AuxSinCosSet.md) and [SinCosSignals](SinCosSignals-AuxSinCosSig.md). For `EncType=4` the direction is set via `SinCosSetup`, not [EncDir](EncDir-AuxEncDir.md).

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Tamagawa (value 8) | Defined (types enumerated up to value 8) | Tamagawa absent from the core type list (types enumerated up to value 7) |

In **v5** the core firmware enumerates encoder types up to value 7 (analog position feedback); value 8 (Tamagawa) is present in the v4 list. As always, supported types are ultimately determined by the product hardware. **v5 is central-i only.**

## Examples

```text
AEncType=1           ; incremental TTL encoder
AEncType=4           ; SIN/COS encoder
AEncType=6           ; BiSS-C absolute encoder
```

### Walk-through: set up an absolute encoder at boot

A typical absolute-encoder commissioning sequence. The example uses a 26-bit BiSS-C device, discarding the 4 least-significant (fine/unused) bits, and no offset; adapt the values to your encoder's datasheet.

```text
AMotorOn=0                ; motor off — these keywords change the feedback pipeline
AEncType=6                ; absolute, BiSS-C (use 3 for EnDat 2.2, 8 for Tamagawa)
AEncAbsBits=26            ; total bit count of the absolute word
AEncAbsMB=4               ; discard the 4 least-significant (unused/fine) bits
AEncAbsOff=0              ; offset added to the masked reading at power-up
ASave                     ; persist the encoder configuration to flash
AReset                    ; software power cycle so the encoder is configured cleanly
                          ; ... then check the seeded position ...
AEncAbsVal                ; raw masked, direction-handled absolute reading
APos                      ; Pos seeded from (EncAbsVal + EncAbsOff) — no homing required
```

To place machine zero at a chosen physical point: park the axis there, read `EncAbsVal`, then set `EncAbsOff` to the negation of that reading and `Save`/`Reset`. On a brushless motor, changing any of these invalidates commutation, so the controller flags that commutation must be repeated.

## See also

- [EncSubType](EncSubType-AuxEncSubType.md) — incremental encoder subtype (`EncType=1`)
- [EncFilt](EncFilt-AuxEncFilt.md) — incremental input filter (`EncType=1`)
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) / [SinCosSignals](SinCosSignals-AuxSinCosSig.md) — SIN/COS configuration and status (`EncType=4`)
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — absolute encoder bit count (absolute types)
