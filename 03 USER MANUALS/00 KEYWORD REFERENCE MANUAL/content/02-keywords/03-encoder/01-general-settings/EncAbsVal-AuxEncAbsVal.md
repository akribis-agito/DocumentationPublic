---
summary: Raw absolute encoder value after bit-masking and direction handling.
last_updated: '2026-10-16'
doc_revision: '2026.10'
---
# EncAbsVal/AuxEncAbsVal

Read-only absolute encoder reading after bit-masking and direction handling.

## Overview

`EncAbsVal` is the absolute encoder reading after the low bits have been removed ([EncAbsMB](EncAbsMB-AuxEncAbsMB.md)) and direction has been applied ([EncDir](EncDir-AuxEncDir.md)), but **before** the power-up offset ([EncAbsOff](EncAbsOff-AuxEncAbsOff.md)). It applies only when the encoder type ([EncType](EncType-AuxEncType.md)) is an absolute encoder — EnDat 2.2 (`EncType=3`), BiSS-C (`EncType=6`) or Tamagawa (`EncType=8`). It is read-only and evaluated in the encoder processing path; it lets you inspect the processed absolute word, for example to decide an offset or verify direction. `AuxEncAbsVal` is the auxiliary-encoder counterpart and operates the same way.

## How it works

For an absolute word supplied by the encoder interface, the firmware:

1. Right-shifts it by [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) to drop the unused low bits.
2. If [EncDir](EncDir-AuxEncDir.md) is reversed, mirrors it within one full turn: `Reading = ReadingCycle − Reading`, where `ReadingCycle = 2^(EncAbsBits − EncAbsMB)`.
3. Stores the result in `EncAbsVal`.

So `EncAbsVal` is the masked, direction-corrected reading — exactly the value the firmware then offsets by [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and accumulates into the position at power-up (see [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) and [Pos](../../10-motion/01-kinematics-status/Pos.md)). It is exposed so that an application can read the live absolute word and take decisions (such as computing the offset needed to make a chosen physical point read zero). Writing to `EncAbsVal` is rejected — it is read-only.

> [!note]
> For an analog position-feedback input (`EncType=7`) the firmware fills `EncAbsVal` with the direction-handled analog reading using the same code path, so it can be read back the same way.

### Rejected Central-i transport frames

For AGM800/AGM800-EC firmware containing the [retained-feedback repair](https://github.com/akribis-agito/Firmware-Main/issues/1297), a rejected standard AMP transport frame does not cause the previously accepted word to be shifted or direction-inverted again. With unchanged configuration, `EncAbsVal` retains the formatted measurement until another transport word is accepted. Existing error handling may separately predict the position used for accumulation; `EncAbsVal` is not that estimate.

Transport acceptance does not establish a newly acquired, error-free encoder measurement. This repair adds no timestamp, first-sample qualification or detailed encoder alarm reporting. See [EncStatReg](EncStatReg.md) for diagnostic limits. It does not change `EncAbsErrTime=-1` bypass or existing fault thresholds.

### Auxiliary encoder (AuxEncAbsVal)

`AuxEncAbsVal` is the masked and direction-handled auxiliary absolute reading. The retained-feedback repair also covers the existing Central-i auxiliary serial firmware paths; actual protocol support depends on the remote FPGA image. A firmware encoder-type selection alone does not establish auxiliary hardware support.

## Examples

```text
AEncAbsVal              ; read the processed absolute value
AAuxEncAbsVal           ; read the processed auxiliary absolute value
```

## Edge cases

- **Motor off.** The absolute reading runs whenever the encoder interface is active; processing does not require the motor to be enabled. This does not guarantee a fresh encoder sample on each cycle.
- **Power-up seed.** For a fixed period after power-up the firmware seeds the accumulated position from `EncAbsVal + EncAbsOff`. The standalone controller uses a shared countdown; Central-i uses a per-axis countdown re-armed during port configuration. The countdown is not a qualified-first-sample check; a later clear status does not validate the value used during initialization.
- **Startup reading.** Do not infer readiness from a fixed number of host reads or from a nonzero value. Link and encoder startup can leave an unavailable or retained reading; this keyword does not expose sample age or qualified initialization.
- **Encoder type.** Meaningful for absolute encoders (`EncType=3`, `6`, `8`) and for analog position feedback (`EncType=7`, where the analog reading is run through the same direction-handling code path). For incremental/SIN-COS types the value is not produced.
- **Central-i disconnect.** With the port disconnected ([CIStatus](../../01-system/05-central-i/CIStatus.md)`[1] ≠ 3`) no remote frames arrive and the firmware cannot refresh `EncAbsVal`; the keyword holds its last-applied value.
- **Write attempts.** Read-only — assignments are rejected.
- **Configuration changes.** Recheck the reading after encoder or port reconfiguration. Reformatting a retained word under new settings does not establish a new physical measurement.

## See also

- [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) — bit-masking applied before this value
- [EncDir](EncDir-AuxEncDir.md) — direction handling applied to the reading
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset added to this value at power-up
- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — absolute word width
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsVal` applies for absolute encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position; `Pos` is seeded from `EncAbsVal + EncAbsOff`
