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

**No counts are lost to rounding.** Because `PDFact/PDFactDen` is generally fractional, scaling leaves a remainder; the controller carries that remainder into the next cycle. Over time the accumulated `PDPos` therefore matches the exact rational scaling rather than drifting — `PDFact` and `PDFactDen` are kept as separate integers (rather than one combined value) precisely so this exact remainder can be tracked.

The value range is ±16,777,215. A **negative** `PDFact` reverses the sense of accumulation; this is independent of the [PDEncDir](PDEncDir.md) sign (the two combine).

### Worked example

A stepper master sends 10 000 pulses per revolution; the follower axis is configured for 4 000 PDPos counts per revolution. The scaling needed is `4000 / 10000 = 2 / 5`. Set `PDFact = 2`, `PDFactDen = 5`. If the master then streams pulses at 50 kHz, `PDPos` advances at `50000 × 2/5 = 20000` counts per second, exactly the follower's nominal feed rate, with no long-term drift because the fractional remainder of `2/5` per pulse is carried forward each cycle.

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
