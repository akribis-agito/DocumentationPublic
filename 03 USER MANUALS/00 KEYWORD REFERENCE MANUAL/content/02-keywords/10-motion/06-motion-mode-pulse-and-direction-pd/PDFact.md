---
keyword: PDFact
summary: Numerator of the scaling factor applied to detected pulses before accumulation into PDPos.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 110
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -16777215
  - 16777215
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDFact

Numerator of the scaling factor applied to detected pulses before accumulation into PDPos.

## Overview

`PDFact` is the numerator of the scaling factor applied to the number of pulses detected, before the sign correction and accumulation into the internal counter [PDPos](PDPos.md). Together with the denominator [PDFactDen](PDFactDen.md) it forms the rational scale `PDFact / PDFactDen` that converts incoming pulse counts into `PDPos` increments. This lets the decoded pulse-and-direction command be matched to the desired axis resolution.

A negative `PDFact` reverses the sense of accumulation; the direction sign can also be configured separately with [PDEncDir](PDEncDir.md).

## How it works

Each controller cycle the increment added to [PDPos](PDPos.md) is:

```text
PDPos increment = (pulses this cycle) × PDFact / PDFactDen   (then signed by PDEncDir)
```

When either `PDFact` or `PDFactDen` is written, the special function `SpPDFactors` (`SpecialFuncs.c:3948`) precomputes a floating-point factor `gfPDFact = PDFact / PDFactDen` and the reciprocal `gfOneDivPDFactDen = 1 / PDFactDen`. The control interrupt uses `gfPDFact` for the fast per-cycle multiply (`AG300_CTL01ControlInterrupt.h:1265`).

**No counts are lost to rounding.** Because `PDFact/PDFactDen` is generally fractional, the float multiply leaves a remainder; the firmware computes the exact remainder each cycle with full 64-bit integer math and carries it into the next cycle (`glPDPosDeltaRemainderPrev`). Over time the accumulated `PDPos` therefore matches the exact rational scaling rather than drifting — `PDFact` and `PDFactDen` are kept as separate integers (rather than one float) precisely so this exact remainder can be computed.

The value range is ±16,777,215. A **negative** `PDFact` reverses the sense of accumulation; this is independent of the [PDEncDir](PDEncDir.md) sign (the two combine).

## Examples

To scale so that 4 input pulses advance `PDPos` by 1 count, set `PDFact = 1`, `PDFactDen = 4`:

```text
APDFact=1            ; numerator: 1 PDPos count
APDFactDen=4         ; denominator: per 4 input pulses
APDFact=1000         ; default numerator (with default PDFactDen=1000, ratio = 1)
APDFact             ; read the current numerator
```

## See also

- [PDFactDen](PDFactDen.md) — denominator of the scaling factor
- [PDPos](PDPos.md) — counter the scaling is accumulated into
- [PDEncDir](PDEncDir.md) — accumulation direction (sign), combined with the sign of `PDFact`
