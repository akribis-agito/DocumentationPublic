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

For each controller cycle:

```text
PDPos increment = (pulses detected) × PDFact / PDFactDen   (then sign-corrected by PDEncDir)
```

## Examples

```text
APDFact=1000         ; numerator of the P/D scaling factor (default)
APDFact             ; read the current numerator
```

## See also

- [PDFactDen](PDFactDen.md) — denominator of the scaling factor
- [PDPos](PDPos.md) — counter the scaling is accumulated into
- [PDEncDir](PDEncDir.md) — accumulation direction (sign)
