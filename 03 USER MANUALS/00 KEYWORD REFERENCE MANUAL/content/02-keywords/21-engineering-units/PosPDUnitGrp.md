---
keyword: PosPDUnitGrp
summary: Read-only list of the pulse-and-direction position keywords that share the P/D position user-unit scaling and label.
availability:
  standalone: []
  central-i:
  - v5
can_code: 817
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 3
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1023
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# PosPDUnitGrp

Read-only list of the pulse-and-direction position keywords that share the P/D position user-unit scaling and label.

## Overview

When Global User Units is enabled for an axis ([UserUnitsEn](UserUnitsEn.md) = 1), each physical quantity is presented to the host with a per-quantity scale factor and a free-text unit label. `PosPDUnitGrp` is the membership list for the **pulse-and-direction (P/D) position** quantity: it tells the host which keywords are scaled together by [PosPDUnitFct](PosPDUnitFct.md) and labeled by [PosPDUnitUnt](PosPDUnitUnt.md).

It is the P/D counterpart of the main-feedback [PosUnitGrp](PosUnitGrp.md), and applies to the pulse-and-direction position counter [PDPos](../10-motion/06-motion-mode-pulse-and-direction-pd/PDPos.md) and the command that presets it.

`PosPDUnitGrp` is read-only and fixed: the controller populates it at startup, so you read it to discover the group, you do not edit it.

## How it works

The keyword is a non-axis array. Each populated element holds one member of the P/D position unit group. Arrays are 1-indexed; element [0] does not exist. The array has a reserved slot, so with `array_size` 3 the highest usable index is 2.

| Index | Member keyword |
|-------|----------------|
| [1]   | PDPos (pulse-and-direction position counter) |
| [2]   | SetPDPos (preset/re-zero the P/D position) |

Each element returns the internal command code of the member keyword (range 0–1023). A value of 0 means the slot is unused.

This grouping is consumed by the host display/units layer; it does not change the internal control computation. The scale factor and label for these keywords come from [PosPDUnitFct](PosPDUnitFct.md) and [PosPDUnitUnt](PosPDUnitUnt.md).

Global User Units and the embedded P/D scaling [PDUsrUnits](../10-motion/06-motion-mode-pulse-and-direction-pd/PDUsrUnits.md) are mutually exclusive on the same axis. If `UserUnitsEn` is on and `PDUsrUnits` is also set to a non-default scaling, accessing a member of this group reports a conflict.

This keyword is available from v5 (central-i) only.

## Examples

```text
APosPDUnitGrp[1]    ; read the first member command code of the P/D position group
APosPDUnitGrp[2]    ; read the second member command code
```

## See also

- [PosPDUnitFct](PosPDUnitFct.md) — scale factor for the P/D position quantity
- [PosPDUnitUnt](PosPDUnitUnt.md) — unit label for the P/D position quantity
- [PosUnitGrp](PosUnitGrp.md) — main-feedback position unit group
- [UserUnitsEn](UserUnitsEn.md) — enables the Global User Units feature per axis
- [PDPos](../10-motion/06-motion-mode-pulse-and-direction-pd/PDPos.md) — pulse-and-direction position counter
