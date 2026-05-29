---
keyword: VelPDUnitUnt
summary: "Free-text unit label for pulse-and-direction velocity, one character per array element."
availability:
  standalone: []
  central-i:
  - v5
can_code: 825
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
# VelPDUnitUnt

Free-text unit label for pulse-and-direction velocity, one character per array element.

## Overview

`VelPDUnitUnt` holds the textual unit name shown by the host for the pulse-and-direction (P/D) velocity quantity when Global User Units is enabled ([UserUnitsEn](UserUnitsEn.md) = 1). It is the label that goes with the P/D velocity scale factor [VelPDUnitFct](VelPDUnitFct.md), and it applies to every keyword in the P/D velocity unit group [VelPDUnitGrp](VelPDUnitGrp.md). It is the P/D counterpart of the main-feedback [VelUnitUnt](VelUnitUnt.md).

The label is purely cosmetic: it changes how the P/D velocity unit is named on the host, not the value or the control computation.

## How it works

The label is stored as a per-axis character array, one character code per element. Arrays are 1-indexed; element [0] does not exist. With `array_size` 11 there is one reserved slot, so the usable indices are [1] through [10] — a label of up to 10 characters. Each element holds one character code in the range 0–255; a 0 terminates the string. The default is an empty label.

| Index | Element |
|-------|---------|
| [1]   | First character of the label |
| [2]   | Second character of the label |
| ...   | ... |
| [10]  | Tenth character of the label |

The label is stored in flash, so it persists across power cycles.

This keyword is available from v5 (central-i) only.

## Examples

Set a four-character label `"mm/s"` (character codes 109, 109, 47, 115) and terminate it:

```text
AVelPDUnitUnt[1]=109   ; 'm'
AVelPDUnitUnt[2]=109   ; 'm'
AVelPDUnitUnt[3]=47    ; '/'
AVelPDUnitUnt[4]=115   ; 's'
AVelPDUnitUnt[5]=0     ; string terminator
AVelPDUnitUnt[1]       ; read back the first character code
```

## See also

- [VelPDUnitFct](VelPDUnitFct.md) — scale factor for the P/D velocity quantity
- [VelPDUnitGrp](VelPDUnitGrp.md) — keywords this label applies to
- [VelUnitUnt](VelUnitUnt.md) — main-feedback velocity unit label
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
