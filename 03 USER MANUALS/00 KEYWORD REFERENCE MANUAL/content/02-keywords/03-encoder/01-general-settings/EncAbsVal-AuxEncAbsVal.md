---
summary: Raw absolute encoder value after bit-masking and direction handling.
---
# EncAbsVal/AuxEncAbsVal

Read-only absolute encoder reading after bit-masking and direction handling.

## Overview

`EncAbsVal` is the absolute encoder reading after the low bits have been removed ([EncAbsMB](EncAbsMB-AuxEncAbsMB.md)) and direction has been applied ([EncDir](EncDir-AuxEncDir.md)), but **before** the power-up offset ([EncAbsOff](EncAbsOff-AuxEncAbsOff.md)). It applies only when the encoder type ([EncType](EncType-AuxEncType.md)) is an absolute encoder — EnDat 2.2 (`EncType=3`), BiSS-C (`EncType=6`) or Tamagawa (`EncType=8`). It is read-only and updated every control cycle; it lets you inspect the processed absolute word, for example to decide an offset or verify direction. `AuxEncAbsVal` is the auxiliary-encoder counterpart and operates the same way.

## How it works

Each control cycle the firmware reads the raw absolute word from the encoder interface, then (`ControlInterrupt.c:2071`–`2078`):

1. Right-shifts it by [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) to drop the unused low bits.
2. If [EncDir](EncDir-AuxEncDir.md) is reversed, mirrors it within one full turn: `Reading = ReadingCycle − Reading`, where `ReadingCycle = 2^(EncAbsBits − EncAbsMB)`.
3. Stores the result in `EncAbsVal` (`ControlInterrupt.c:2078`).

So `EncAbsVal` is the masked, direction-corrected reading — exactly the value the firmware then offsets by [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and accumulates into the position at power-up (see [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and [Pos](../../10-motion/01-kinematics-status/Pos.md)). It is exposed so that an application can read the live absolute word and take decisions (such as computing the offset needed to make a chosen physical point read zero). Writing to `EncAbsVal` is rejected — it is read-only.

> [!note]
> For an analog position-feedback input (`EncType=7`) the firmware fills `EncAbsVal` with the direction-handled analog reading using the same code path, so it can be read back the same way.

### Auxiliary encoder (AuxEncAbsVal)

`AuxEncAbsVal` is the masked and direction-handled auxiliary absolute reading, captured the same way (`ControlInterrupt.c:2276`).

## Examples

```text
AEncAbsVal              ; read the processed absolute value
AAuxEncAbsVal           ; read the processed auxiliary absolute value
```

## See also

- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — bit-masking applied before this value
- [EncDir](EncDir-AuxEncDir.md) — direction handling applied to the reading
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset added to this value at power-up
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — absolute word width
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsVal` applies for absolute encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position; `Pos` is seeded from `EncAbsVal + EncAbsOff`
