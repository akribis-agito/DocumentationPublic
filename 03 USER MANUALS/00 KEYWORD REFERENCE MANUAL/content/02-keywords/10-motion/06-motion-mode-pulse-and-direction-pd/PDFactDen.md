---
keyword: PDFactDen
summary: Denominator of the scaling factor applied to detected pulses before accumulation into PDPos.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 119
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
  - 1
  - 16777215
  default: 1000
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDFactDen

Denominator of the scaling factor applied to detected pulses before accumulation into PDPos.

## Overview

`PDFactDen` is the denominator of the scaling factor applied to the number of pulses detected, before the sign correction and accumulation into the internal counter [PDPos](PDPos.md). Together with the numerator [PDFact](PDFact.md) it forms the rational scale `PDFact / PDFactDen` that converts incoming pulse counts into `PDPos` increments, letting the decoded pulse-and-direction command be matched to the desired axis resolution. The minimum value is `1` (division by zero is not allowed).

## How it works

For each controller cycle:

```text
PDPos increment = (pulses detected) × PDFact / PDFactDen   (then sign-corrected by PDEncDir)
```

## Examples

```text
PDFactDen=1000      ; denominator of the P/D scaling factor (default)
PDFactDen?          ; read the current denominator
```

## See also

- [PDFact](PDFact.md) — numerator of the scaling factor
- [PDPos](PDPos.md) — counter the scaling is accumulated into
- [PDEncDir](PDEncDir.md) — accumulation direction (sign)
