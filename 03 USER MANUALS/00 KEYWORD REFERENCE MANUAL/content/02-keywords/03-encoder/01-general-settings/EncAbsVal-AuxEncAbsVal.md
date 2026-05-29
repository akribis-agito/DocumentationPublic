---
summary: Raw absolute encoder value after bit-masking and direction handling.
---
# EncAbsVal/AuxEncAbsVal

Read-only absolute encoder reading after bit-masking and direction handling.

## Overview

`EncAbsVal` is the absolute encoder reading after the low bits have been removed ([EncAbsMB](EncAbsMB-AuxEncAbsMB.md)) and direction has been applied ([EncDir](EncDir-AuxEncDir.md)), but **before** the power-up offset ([EncAbsOff](EncAbsOff-AuxEncAbsOff.md)). It applies only when the encoder type ([EncType](EncType-AuxEncType.md)) is an absolute encoder — EnDat 2.2 (`EncType=3`), BiSS-C (`EncType=6`) or Tamagawa (`EncType=8`). It is read-only and updated every control cycle; it lets you inspect the processed absolute word, for example to decide an offset or verify direction. `AuxEncAbsVal` is the auxiliary-encoder counterpart and operates the same way.

## How it works

Each control cycle the firmware reads the raw absolute word from the encoder interface, then:

1. Right-shifts it by [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) to drop the unused low bits.
2. If [EncDir](EncDir-AuxEncDir.md) is reversed, mirrors it within one full turn: `Reading = ReadingCycle − Reading`, where `ReadingCycle = 2^(EncAbsBits − EncAbsMB)`.
3. Stores the result in `EncAbsVal`.

So `EncAbsVal` is the masked, direction-corrected reading — exactly the value the firmware then offsets by [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and accumulates into the position at power-up (see [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and [Pos](../../10-motion/01-kinematics-status/Pos.md)). It is exposed so that an application can read the live absolute word and take decisions (such as computing the offset needed to make a chosen physical point read zero). Writing to `EncAbsVal` is rejected — it is read-only.

> [!note]
> For an analog position-feedback input (`EncType=7`) the firmware fills `EncAbsVal` with the direction-handled analog reading using the same code path, so it can be read back the same way.

### Auxiliary encoder (AuxEncAbsVal)

`AuxEncAbsVal` is the masked and direction-handled auxiliary absolute reading, captured the same way.

## Examples

```text
AEncAbsVal              ; read the processed absolute value
AAuxEncAbsVal           ; read the processed auxiliary absolute value
```

## Edge cases

- **Motor off.** The absolute reading runs whenever the encoder interface is active; `EncAbsVal` updates every cycle regardless of motor state.
- **Power-up seed.** For a fixed number of control cycles after power-up the firmware seeds the accumulated position from `EncAbsVal + EncAbsOff`. On the standalone controller this window is governed by a single shared counter and spans up to about 31 control cycles on a single-axis controller, fewer on a multi-axis one; on Central-i each axis has its own window (re-armed whenever the port is reconfigured) spanning roughly the first 150 cycles after the port is configured. In all cases the seed completes within the first handful of cycles after boot or configuration.
- **First reading is delayed.** The valid absolute frame is not available on the very first control cycle — the encoder returns its data after a short link delay, so the first usable reading appears one cycle later. Read `EncAbsVal` after the controller has settled (a few cycles into boot) to obtain the raw masked, direction-handled word; a read on the very first cycle may return a stale value.
- **Encoder type.** Meaningful for absolute encoders (`EncType=3`, `6`, `8`) and for analog position feedback (`EncType=7`, where the analog reading is run through the same direction-handling code path). For incremental/SIN-COS types the value is not produced.
- **Central-i disconnect.** With the port disconnected ([CIStatus](../../01-system/05-central-i/CIStatus.md)`[1] ≠ 3`) no remote frames arrive and the firmware cannot refresh `EncAbsVal`; the keyword holds its last-applied value.
- **Write attempts.** Read-only — assignments are rejected.
- **After EncDir / EncAbsMB / EncAbsBits change.** Take a fresh reading; the value is recomputed from the new mask and direction starting on the next cycle.

## See also

- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — bit-masking applied before this value
- [EncDir](EncDir-AuxEncDir.md) — direction handling applied to the reading
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset added to this value at power-up
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — absolute word width
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsVal` applies for absolute encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position; `Pos` is seeded from `EncAbsVal + EncAbsOff`
