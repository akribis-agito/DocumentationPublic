---
summary: Selects the encoder feedback type (incremental, SIN/COS, absolute, or analog).
last_updated: '2026-06-02'
doc_revision: '2026.06'
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

### Tamagawa (value 8)

A Tamagawa encoder is a single-turn serial absolute encoder, selectable for the main encoder (`EncType=8`) and, on products whose hardware supports it, the auxiliary encoder (`AuxEncType=8`). It reports its own resolution in an identification byte (ENID), and how [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) / `AuxEncAbsBits` are set depends on the product:

- **Standalone controller (v4):** the controller reads the resolution from the encoder and stores it in `EncAbsBits` (main) or `AuxEncAbsBits` (auxiliary). While `EncType` or `AuxEncType` is 8, writing either keyword is refused with error 331 ("Tamagawa encoder resolution cannot be changed, it is learned").
- **Central-i:** the resolution is **not** read from the encoder. Set `EncAbsBits`, and `AuxEncAbsBits` for an auxiliary Tamagawa encoder, by hand to the encoder's single-turn resolution. A wrong value is not detected: the rollover modulus is computed from it (see [EncAbsBits](EncAbsBits-AuxEncAbsBits.md)), so the position accumulates incorrectly. On **v4** the bit-count write is refused once either type is 8, so write `EncAbsBits` / `AuxEncAbsBits` before selecting type 8. On **v5** it can be written at any time.

The encoder's on-board memory can be read and written with [EncAbsSendCmd](../07-absolute-encoder/EncAbsSendCmd.md) on a standalone controller; it is not available on a central-i master.

For an analog SIN/COS encoder, also refer to [SinCosSetup](SinCosSetup-AuxSinCosSet.md) and [SinCosSignals](SinCosSignals-AuxSinCosSig.md). For `EncType=4` the direction is set via `SinCosSetup`, not [EncDir](EncDir-AuxEncDir.md).

## Changes between versions

| | v4 (standalone & central-i) | v5 (central-i) |
|---|---|---|
| Tamagawa (value 8) | Supported | Supported (central-i) |
| `EncAbsBits` / `AuxEncAbsBits` with a Tamagawa encoder on central-i | Must be set by hand, before selecting type 8 (the write is refused afterwards) | Must be set by hand; the write is accepted at any time |

Both versions enumerate encoder types up to value 8 (Tamagawa). As always, supported types are ultimately determined by the product hardware. **v5 is central-i only.**

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
AEncType=6                ; absolute, BiSS-C (use 3 for EnDat 2.2; 8 for Tamagawa)
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
