---
keyword: PosAuxUnitUnt
summary: Free-text unit label for auxiliary-encoder position, one character per array element.
availability:
  standalone: []
  central-i:
  - v5
can_code: 816
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
# PosAuxUnitUnt

Free-text unit label for auxiliary-encoder position, one character per array element.

## Overview

`PosAuxUnitUnt` holds the textual unit name shown by the host for the auxiliary-encoder position quantity when Global User Units is enabled ([UserUnitsEn](UserUnitsEn.md) = 1). It is the label that goes with the auxiliary position scale factor [PosAuxUnitFct](PosAuxUnitFct.md), and it applies to every keyword in the auxiliary position unit group [PosAuxUnitGrp](PosAuxUnitGrp.md). It is the auxiliary-encoder counterpart of the main-feedback [PosUnitUnt](PosUnitUnt.md).

The label is purely cosmetic: it changes how the auxiliary position unit is named on the host, not the value or the control computation.

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

Set a three-character label `"deg"` (character codes 100, 101, 103) and terminate it:

```text
APosAuxUnitUnt[1]=100   ; 'd'
APosAuxUnitUnt[2]=101   ; 'e'
APosAuxUnitUnt[3]=103   ; 'g'
APosAuxUnitUnt[4]=0     ; string terminator
APosAuxUnitUnt[1]       ; read back the first character code
```

## See also

- [PosAuxUnitFct](PosAuxUnitFct.md) — scale factor for the auxiliary position quantity
- [PosAuxUnitGrp](PosAuxUnitGrp.md) — keywords this label applies to
- [PosUnitUnt](PosUnitUnt.md) — main-feedback position unit label
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
