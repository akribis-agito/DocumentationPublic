---
keyword: PDFactDen
summary: Denominator of the scaling factor applied to detected pulses before accumulation into PDPos.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

Each controller cycle the increment added to [PDPos](PDPos.md) is:

```text
PDPos increment = (pulses this cycle) × PDFact / PDFactDen   (then signed by PDEncDir)
```

Writing `PDFactDen` (or [PDFact](PDFact.md)) causes the controller to precompute the float factor `PDFact / PDFactDen` and the reciprocal `1 / PDFactDen` used for the fast per-cycle scaling in the control interrupt.

The minimum value is `1` (the reciprocal `1/PDFactDen` would be undefined at 0), and the maximum is 16,777,215. Because the per-cycle remainder of the division is carried forward in 64-bit integer math, even a non-integer `PDFact/PDFactDen` ratio accumulates into `PDPos` exactly, without drift — see [PDFact](PDFact.md).

## Examples

```text
APDFactDen=4         ; 4 input pulses per PDFact numerator
APDFactDen=1000      ; default denominator (with default PDFact=1000, ratio = 1)
APDFactDen          ; read the current denominator
```

## See also

- [PDFact](PDFact.md) — numerator of the scaling factor (and the exact-remainder mechanism)
- [PDPos](PDPos.md) — counter the scaling is accumulated into
- [PDEncDir](PDEncDir.md) — accumulation direction (sign)
