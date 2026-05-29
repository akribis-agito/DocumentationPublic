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
- **Central-i remote units** — `EncDir` is packed into the remote encoder configuration word (bit 8) sent to the remote unit, where the hardware applies the same swap.

For an **absolute** encoder there is no quadrature decoder to swap, so the firmware applies the reversal in software each cycle: after the raw word has been right-shifted by [EncAbsMB](EncAbsMB-AuxEncAbsMB.md), the masked reading is replaced with `ReadingCycle − reading` when `EncDir = 1`. The net effect on [Pos](../../10-motion/01-kinematics-status/Pos.md) is the same as for an incremental encoder.

| EncDir | Effect on position |
|---|---|
| 0 | Position counts in the encoder's native direction. |
| 1 | Position counts in the reversed direction (incremental: A/B swapped at the decoder; absolute: `ReadingCycle − reading` after masking). |

`EncDir` must be set before motor phasing/commutation, because changing it after phasing inverts the position-to-electrical-angle relationship and would require re-phasing.

## Examples

```text
AEncDir=0            ; count in the encoder's native direction
AEncDir=1            ; reverse the counting direction
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncDir` does not apply to `EncType=4`
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — direction setting for SIN/COS encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position affected by `EncDir`
