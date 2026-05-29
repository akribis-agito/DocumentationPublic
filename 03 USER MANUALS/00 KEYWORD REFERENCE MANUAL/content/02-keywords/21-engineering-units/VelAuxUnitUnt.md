---
keyword: VelAuxUnitUnt
summary: "Free-text unit label for auxiliary-encoder velocity, one character per array element."
availability:
  standalone: []
  central-i:
  - v5
can_code: 822
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
# VelAuxUnitUnt

Free-text unit label for auxiliary-encoder velocity, one character per array element.

## Overview

`VelAuxUnitUnt` holds the textual unit name shown by the host for the auxiliary-encoder velocity quantity when Global User Units is enabled ([UserUnitsEn](UserUnitsEn.md) = 1). It is the label that goes with the auxiliary velocity scale factor [VelAuxUnitFct](VelAuxUnitFct.md), and it applies to every keyword in the auxiliary velocity unit group [VelAuxUnitGrp](VelAuxUnitGrp.md). It is the auxiliary-encoder counterpart of the main-feedback [VelUnitUnt](VelUnitUnt.md).

The label is purely cosmetic: it changes how the auxiliary velocity unit is named on the host, not the value or the control computation.

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

Set a five-character label `"deg/s"` (character codes 100, 101, 103, 47, 115) and terminate it:

```text
AVelAuxUnitUnt[1]=100   ; 'd'
AVelAuxUnitUnt[2]=101   ; 'e'
AVelAuxUnitUnt[3]=103   ; 'g'
AVelAuxUnitUnt[4]=47    ; '/'
AVelAuxUnitUnt[5]=115   ; 's'
AVelAuxUnitUnt[6]=0     ; string terminator
AVelAuxUnitUnt[1]       ; read back the first character code
```

## See also

- [VelAuxUnitFct](VelAuxUnitFct.md) — scale factor for the auxiliary velocity quantity
- [VelAuxUnitGrp](VelAuxUnitGrp.md) — keywords this label applies to
- [VelUnitUnt](VelUnitUnt.md) — main-feedback velocity unit label
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
