---
keyword: PosUnitUnt
summary: "Display label (name) of the position engineering unit, stored as a short text string."
availability:
  standalone: []
  central-i:
  - v5
can_code: 804
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
# PosUnitUnt

Display label (name) of the position engineering unit, stored as a short text string.

## Overview

`PosUnitUnt` holds the **name of the position engineering unit** — the text label that goes with the scale factor in [PosUnitFct](PosUnitFct.md), for example `mm` or `um`. It documents which unit the position group (see [PosUnitGrp](PosUnitGrp.md)) is being presented in. The label is descriptive: it is shown alongside values but does not itself perform any conversion — the numeric conversion is set by [PosUnitFct](PosUnitFct.md).

This keyword is available from central-i v5 only.

## How it works

`PosUnitUnt` is a per-axis array stored in flash that holds the unit label as a short text string. Each array element holds one character of the name (a character code in the range 0–255). The array is 1-indexed: the first character is at element [1] and element [0] is reserved and not used. The label can hold up to 10 characters, so the highest usable index is one less than the array size; a shorter label is terminated within the available length.

You typically set the label through a host tool that writes the whole string at once; the per-character array layout is how it is stored on the controller.

## Examples

```text
APosUnitUnt[1]      ; read the first character of the position unit label
APosUnitUnt[2]      ; read the second character
```

## See also

- [00-overview](00-overview.md) — the Group / Factor / Unit model
- [PosUnitFct](PosUnitFct.md) — position scale factor (the numeric conversion)
- [PosUnitGrp](PosUnitGrp.md) — keywords the unit applies to
- [UserUnitsEn](UserUnitsEn.md) — master enable
- [VelUnitUnt](VelUnitUnt.md) · [AccUnitUnt](AccUnitUnt.md) · [FrcUnitUnt](FrcUnitUnt.md) — the other quantity unit labels
