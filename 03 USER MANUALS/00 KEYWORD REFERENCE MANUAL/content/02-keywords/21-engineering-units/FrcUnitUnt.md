---
keyword: FrcUnitUnt
summary: Display label (name) of the force engineering unit, stored as a short text string.
availability:
  standalone: []
  central-i:
  - v5
can_code: 813
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 11
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 255
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# FrcUnitUnt

Display label (name) of the force engineering unit, stored as a short text string.

## Overview

`FrcUnitUnt` holds the **name of the force engineering unit** — the text label that goes with the scale factor in [FrcUnitFct](FrcUnitFct.md), for example `N` or `mN`. It documents which unit the force group (see [FrcUnitGrp](FrcUnitGrp.md)) is being presented in. The label is descriptive: it is shown alongside values but does not itself perform any conversion — the numeric conversion is set by [FrcUnitFct](FrcUnitFct.md).

This keyword is available from central-i v5 only.

## How it works

`FrcUnitUnt` is a per-axis array stored in flash that holds the unit label as a short text string. Each array element holds one character of the name (a character code in the range 0–255). The array is 1-indexed: the first character is at element [1] and element [0] is reserved and not used. The label can hold up to 10 characters, so the highest usable index is one less than the array size; a shorter label is terminated within the available length.

You typically set the label through a host tool that writes the whole string at once; the per-character array layout is how it is stored on the controller.

## Examples

```text
AFrcUnitUnt[1]      ; read the first character of the force unit label
AFrcUnitUnt[2]      ; read the second character
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [FrcUnitFct](FrcUnitFct.md) — force scale factor (the numeric conversion)
- [FrcUnitGrp](FrcUnitGrp.md) — keywords the unit applies to
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [PosUnitUnt](PosUnitUnt.md) · [VelUnitUnt](VelUnitUnt.md) · [AccUnitUnt](AccUnitUnt.md) — the other quantity unit labels
