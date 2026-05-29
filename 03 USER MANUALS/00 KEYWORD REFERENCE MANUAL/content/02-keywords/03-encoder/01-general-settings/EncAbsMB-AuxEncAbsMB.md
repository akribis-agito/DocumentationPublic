---
summary: Number of least significant bits removed (right-shifted) from the absolute encoder reading.
---
# EncAbsMB/AuxEncAbsMB

Number of least significant bits removed (right-shifted) from the absolute encoder reading.

## Overview

`EncAbsMB` defines how many least-significant bits are discarded from the raw absolute reading: the reading is right-shifted by `EncAbsMB` bits before it is used. It applies only when the encoder type ([EncType](EncType-AuxEncType.md)) is an absolute encoder — EnDat 2.2 (`EncType=3`), BiSS-C (`EncType=6`) or Tamagawa (`EncType=8`). Removing low-order bits drops unused or excessively fine resolution bits so that the accumulated position uses only the meaningful bits and so that the rollover modulus is set correctly. `AuxEncAbsMB` is the auxiliary-encoder counterpart and operates the same way.

Range 0–8, default 0 (no bits removed).

## How it works

The very first operation applied to a fresh absolute reading each control cycle is the right-shift:

$$\text{Reading}_{\text{masked}} = \text{Reading}_{\text{raw}} \gg \text{EncAbsMB}$$

This happens before direction handling, before [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) is captured, and before the offset and accumulation. So every downstream value already reflects the masked reading.

`EncAbsMB` also shifts the rollover modulus. The width of one full turn of the *masked* word is

$$\text{ReadingCycle} = 2^{\,\text{EncAbsBits} - \text{EncAbsMB}}$$

precomputed when `EncAbsMB` (or [EncAbsBits](EncAbsBits-AuxEncAbsBits.md)) is written. Increasing `EncAbsMB` by 1 halves `ReadingCycle`, which is consistent: discarding a low bit halves the number of distinct counts in the word. The accumulator uses `ReadingCycle` (and its 25 %/75 % marks) to detect when the masked reading wraps and to add or subtract a full cycle so the position counts continuously.

Because `EncAbsMB` changes the count-to-electrical-angle scaling, changing it on a brushless motor invalidates commutation and the controller flags that commutation must be repeated.

> [!note]
> `EncAbsMB` removes bits from the **bottom** (least significant) of the word. The remaining low bits represent the single-turn position and the high bits the multi-turn count, as shown in the [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) bit-layout figure.

### Auxiliary encoder (AuxEncAbsMB)

`AuxEncAbsMB` right-shifts the auxiliary absolute reading by the same rule and feeds the auxiliary rollover modulus `2^(AuxEncAbsBits − AuxEncAbsMB)`.

## Examples

```text
AEncAbsMB=2             ; discard the 2 least significant bits of the reading
AEncAbsMB               ; query the configured number of removed bits
AAuxEncAbsMB=0          ; keep all bits of the auxiliary absolute reading
```

## See also

- [EncAbsBits](EncAbsBits-AuxEncAbsBits.md) — total bit count; combines with `EncAbsMB` to set the rollover modulus
- [EncAbsVal](EncAbsVal-AuxEncAbsVal.md) — reading after this masking and direction handling
- [EncAbsOff](EncAbsOff-AuxEncAbsOff.md) — offset added to the masked reading at power-up
- [EncDir](EncDir-AuxEncDir.md) — direction handling applied after masking
- [EncType](EncType-AuxEncType.md) — encoder type; `EncAbsMB` applies for absolute encoders
