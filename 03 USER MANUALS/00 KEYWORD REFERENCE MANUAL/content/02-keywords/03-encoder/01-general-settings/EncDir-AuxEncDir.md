---
summary: Sets the counting direction of the encoder feedback.
---
# EncDir/AuxEncDir

Sets the counting direction of the encoder feedback.

## Overview

`EncDir` configures the counting direction of the encoder reading, aligning the encoder count with the desired positive motion direction. Conceptually, the controller increments or decrements the position ([Pos](../../10-motion/01-kinematics-status/Pos.md)) by the delta of the raw feedback each cycle — `EncDir=0` keeps the encoder's native direction, `EncDir=1` reverses it.

`EncDir` is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is not 4 (SIN/COS). For SIN/COS encoders (`EncType=4`), configure direction through [SinCosSetup](SinCosSetup-AuxSinCosSet.md) instead. During setup it is important to configure `EncDir` to get the desired direction before performing motor phasing. `AuxEncDir` is the auxiliary-encoder counterpart and operates the same way.

## How it works

For an **incremental** encoder the direction reversal is applied in the **quadrature decode hardware**, not as a software post-step:

- **Standalone controller** — `EncDir` is written into the decoder control register's quadrature-swap bit. Setting it swaps the A and B channels in hardware, inverting the decoded count direction.
- **Central-i remote units** — `EncDir` is packed into the remote encoder configuration word (bit 24) sent to the remote unit, where the hardware reverses the count by **inverting the decoded count direction** inside the quadrature decoder. The A and B inputs are not physically swapped; the up/down decision is inverted, which has the same net effect on the count. (On the standalone controller the equivalent setting instead swaps the A and B channels at the decoder; both achieve the same direction reversal.)

For an **absolute** encoder there is no quadrature decoder to swap, so the firmware applies the reversal in software each cycle: after the raw word has been right-shifted by [EncAbsMB](EncAbsMB-AuxEncAbsMB.md), the masked reading is replaced with `ReadingCycle − reading` when `EncDir = 1`. The net effect on [Pos](../../10-motion/01-kinematics-status/Pos.md) is the same as for an incremental encoder.

| EncDir | Effect on position |
|---|---|
| 0 | Position counts in the encoder's native direction. |
| 1 | Position counts in the reversed direction (incremental: standalone swaps A/B at the decoder, Central-i inverts the decoded count direction; absolute: `ReadingCycle − reading` after masking). |

`EncDir` must be set before motor phasing/commutation, because changing it after phasing inverts the position-to-electrical-angle relationship and would require re-phasing.

## Examples

```text
AEncDir=0            ; count in the encoder's native direction
AEncDir=1            ; reverse the counting direction
```

## Edge cases

- **Motor on / in motion.** Writes are rejected while the motor is on or the axis is in motion. Disable the motor first; on a brushless motor you will then need to re-phase.
- **Encoder type 4 (SIN/COS).** `EncDir` is ignored; set direction via [SinCosSetup](SinCosSetup-AuxSinCosSet.md) index [10] instead.
- **Incremental vs absolute.** For incremental (`EncType=1`) the reversal happens in the decode hardware (A/B swap on standalone; the Central-i remote unit instead inverts the decoded count direction, configured via bit 24). For absolute encoders (`EncType=3/6/8`) the reversal is applied in software each cycle as `ReadingCycle − reading` after the [EncAbsMB](EncAbsMB-AuxEncAbsMB.md) right-shift; net effect on [Pos](../../10-motion/01-kinematics-status/Pos.md) is the same.
- **Power-up / Save / Reset.** The setting is flash-saved; the hardware-swap or software-reversal is applied during initialisation, so a fresh value takes effect after [Save](../../01-system/02-operation/Save.md) + [Reset](../../01-system/02-operation/Reset.md).
- **Central-i disconnect.** The direction bit is packed into the remote encoder configuration word and sent during [CIConnect](../../01-system/05-central-i/CIConnect.md); on a disconnected port the remote keeps its last-applied direction.

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncDir` does not apply to `EncType=4`
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — direction setting for SIN/COS encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position affected by `EncDir`
