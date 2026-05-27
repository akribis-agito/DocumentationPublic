---
summary: Sets the counting direction of the encoder feedback.
---
# EncDir/AuxEncDir

Sets the counting direction of the encoder feedback.

## Overview

`EncDir` configures the direction of the encoder reading. The controller increments or decrements the position ([Pos](../../10-motion/01-kinematics-status/Pos.md)) by the delta of the raw position feedback at every controller cycle (hardware interrupt): if `EncDir=0` the delta is added, if `EncDir=1` the delta is subtracted. This lets the encoder count be aligned with the desired positive motion direction.

`EncDir` is only used when the encoder type ([EncType](EncType-AuxEncType.md)) is not 4 (SIN/COS). For SIN/COS encoders (`EncType=4`), configure direction through [SinCosSetup](SinCosSetup-AuxSinCosSet.md) instead. During setup it is important to configure `EncDir` to get the desired direction before performing motor phasing. `AuxEncDir` is the auxiliary-encoder counterpart and operates the same way.

## How it works

| EncDir | Effect on position |
|---|---|
| 0 | Position is incremented by the raw feedback delta each controller cycle. |
| 1 | Position is decremented by the raw feedback delta each controller cycle. |

## Examples

```text
AEncDir=0            ; count in the encoder's native direction
AEncDir=1            ; reverse the counting direction
```

## See also

- [EncType](EncType-AuxEncType.md) — encoder type; `EncDir` does not apply to `EncType=4`
- [SinCosSetup](SinCosSetup-AuxSinCosSet.md) — direction setting for SIN/COS encoders
- [Pos](../../10-motion/01-kinematics-status/Pos.md) — feedback position affected by `EncDir`
