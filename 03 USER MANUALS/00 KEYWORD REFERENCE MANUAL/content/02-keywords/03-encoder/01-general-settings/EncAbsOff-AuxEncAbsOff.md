---
summary: Offset added to the raw absolute encoder reading.
last_updated: '2026-10-16'
doc_revision: '2026.10'
---
# EncAbsOff/AuxEncAbsOff

Offset added to the absolute encoder reading at power-up.

## Overview

`EncAbsOff` is an offset added to the absolute reading when the position is first established at power-up. It applies only when the encoder type ([EncType](EncType-AuxEncType.md)) is an absolute encoder — EnDat 2.2 (`EncType=3`), BiSS-C (`EncType=6`) or Tamagawa (`EncType=8`). Its purpose is to align the absolute position reported by the encoder with the desired machine zero, so the axis comes up at a known position without homing. Unlike incremental encoders, an absolute encoder lets [Pos](../../10-motion/01-kinematics-status/Pos.md) be initialised from the encoder itself rather than starting at zero. `AuxEncAbsOff` is the auxiliary-encoder counterpart and operates the same way.

`EncAbsOff` is expressed in user units; `AuxEncAbsOff` is in auxiliary user units. Default 0.

## How it works

For a fixed number of control cycles immediately after power-up the firmware seeds the accumulated position directly from the absolute reading plus this offset, instead of letting it accumulate from zero:

$$\text{EncoderPos}_{\text{init}} = \text{Reading}_{\text{masked}} + \text{EncAbsOff}$$

where `Reading_masked` is the raw reading after the [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) right-shift and [EncDir](EncDir-AuxEncDir.md) direction handling (the same value reported as [EncAbsVal](EncAbsVal-AuxEncAbsVal.md)). At the same time the delta is forced to 0 and the previous-reading register is primed, so the axis starts at `EncoderPos_init` with no spurious jump. This seeded value flows through the normal feedback pipeline (error mapping, modulo) to become [Pos](../../10-motion/01-kinematics-status/Pos.md). After the seed window closes the offset is no longer added; the position simply accumulates the per-cycle deltas.

The standalone controller uses a shared countdown; Central-i uses a per-axis countdown re-armed during port configuration (see [EncAbsVal](EncAbsVal-AuxEncAbsVal.md)). This countdown does not qualify the sample used to seed position.

So `EncAbsOff` shifts where the encoder's absolute zero lands in the controller's position frame. To place machine zero at a chosen physical point, set `EncAbsOff` to the negative of the masked reading observed at that point (read it from [EncAbsVal](EncAbsVal-AuxEncAbsVal.md)).

Changing `EncAbsOff` on a brushless motor invalidates commutation (it shifts the position-to-electrical-angle relationship), so the controller flags that commutation must be repeated.

### Auxiliary encoder (AuxEncAbsOff)

`AuxEncAbsOff` seeds the auxiliary accumulated position the same way at power-up — `AuxPos_init = Reading_masked + AuxEncAbsOff` — establishing the auxiliary feedback at a known value without homing.

## Examples

```text
AEncAbsOff=1000         ; add an offset of 1000 to the absolute reading at power-up
AEncAbsOff=0            ; encoder absolute zero = machine zero
AAuxEncAbsOff=-50000    ; place auxiliary machine zero at reading 50000
```

## Edge cases

- **Unvalidated power-up seed.** Initialization uses the processed reading during its countdown; it does not wait for a qualified first sample. Main absolute-encoder error handling begins after this window. A later clear [EncStatReg](EncStatReg.md) does not validate the reading used to seed [Pos](../../10-motion/01-kinematics-status/Pos.md). The [retained-feedback repair](https://github.com/akribis-agito/Firmware-Main/issues/1297) prevents repeated formatting of a retained Central-i word; it adds no startup qualification.

## See also

- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — the masked, direction-handled reading the offset is added to
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — absolute word width
- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — low bits removed before the offset is applied
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsOff` applies for absolute encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position seeded from `reading + EncAbsOff` at power-up
- [EncStatReg](EncStatReg.md) — diagnostic meaning and startup limits
- [EncAbsErrTime](../07-absolute-encoder/EncAbsErrTime.md) — abnormal-frame monitoring; begins only after the seed window closes
- [SetPosition](../../10-motion/03-kinematics-configuration/SetPosition.md) — preset the feedback after start-up
