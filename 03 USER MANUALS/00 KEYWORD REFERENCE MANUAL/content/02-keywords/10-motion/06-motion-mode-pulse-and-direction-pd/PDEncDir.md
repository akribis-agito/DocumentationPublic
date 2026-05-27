---
keyword: PDEncDir
summary: Configures the sign (direction) of PDPos accumulation relative to the direction signal.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 63
attributes:
  access: '0'
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: false
  units: '0'
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: not_implemented
overrides:
  central-i.v5:
    access: rw
    units: none
    range:
    - 0
    - 1
    implemented: final
---
# PDEncDir

Configures the sign (direction) of PDPos accumulation relative to the direction signal.

## Overview

`PDEncDir` reverses the sign of [PDPos](PDPos.md) accumulation, i.e. it flips which way the counter moves for a given direction signal. It lets the pulse-and-direction decoding sense be inverted without rewiring, and is independent of the magnitude scaling set by [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md). It parallels the feedback-direction keyword [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md), but acts on the P/D *input* rather than the encoder feedback.

> **Availability:** `PDEncDir` is implemented on **v5 (central-i) only**. On v4 it is reserved/not implemented — see *Changes between versions* below.

## How it works

`PDEncDir` is applied directly in the per-cycle accumulation as a sign factor `(1 − 2·PDEncDir)` (macro `M_READ_CALCULATE_PDPOS`, `AG300_CTL01ControlInterrupt.h:1265`):

```text
gllPDPos += gllPDPosDelta * (1 - 2*PDEncDir)
```

So `PDEncDir = 0` gives `+1` (the delta is added) and `PDEncDir = 1` gives `−1` (the delta is subtracted). Because the sign is applied to the already-scaled delta, it only flips direction — magnitude is unaffected.

| Value | Effect on PDPos |
|---|---|
| 0 | **Normal.** `PDPos` increments by `pulses × PDFact/PDFactDen` when the direction signal is logic high, and decrements when it is logic low. |
| 1 | **Inverted.** `PDPos` decrements when the direction signal is logic high, and increments when it is logic low. |

This combines with the sign of `PDFact`: a negative `PDFact` and `PDEncDir = 1` cancel out. `PDEncDir` cannot be changed while the axis is in motion or the motor is on.

## Examples

```text
APDEncDir=0          ; normal accumulation direction (default)
APDEncDir=1          ; inverted accumulation direction
```

## Changes between versions

`PDEncDir` is **central-i v5 only**. On v4 the keyword is reserved (not implemented). On v5 (central-i) it is a read/write flash parameter with range 0–1 that applies the sign described above. v5 is central-i only, so the standalone product does not expose `PDEncDir`.

## See also

- [PDPos](PDPos.md) — counter whose accumulation direction this sets
- [PDFact](PDFact.md) / [PDFactDen](PDFactDen.md) — scaling-factor magnitude (its sign combines with `PDEncDir`)
- [EncDir](../../03-encoder/01-general-settings/EncDir-AuxEncDir.md) — the analogous direction control for encoder feedback
