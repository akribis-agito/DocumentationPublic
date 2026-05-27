---
keyword: MasterModRev
summary: Modulo divisor that corrects MasterPos accumulation when the master variable wraps.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 519
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2000000000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  central-i.v5:
    data_type: int64
---
# MasterModRev

Modulo divisor that corrects MasterPos accumulation when the master variable wraps.

## Overview

`MasterModRev` is the modulo divisor used to ensure correct accumulation of [MasterPos](MasterPos.md) when the variable selected by [GearMaster](GearMaster.md) participates in a modulo operation. The master variable undergoes a modulo operation when:

1. the `ModRev` related to the master variable is non-zero, and
2. it is generally either [Pos](../01-kinematics-status/Pos.md), PDPos, [MasterPos](MasterPos.md), [PosRef](../01-kinematics-status/PosRef.md) or [AbsTrgt](../13-motion-mode-ptp/AbsTrgt.md).

You must set `MasterModRev` to match the `ModRev` of the master variable (manual assignment). If the master variable does not involve a modulo operation, `MasterModRev` must be `0`.

## How it works

The accumulated delta is corrected if its absolute value exceeds half of `MasterModRev`, in which case the master variable is assumed to have wrapped through its modulo boundary.

## Examples

```text
AMasterModRev=0      ; master variable has no modulo operation
AMasterModRev       ; read current value
```

## See also

- [MasterPos](MasterPos.md) — accumulated, scaled master position this divisor protects
- [GearMaster](GearMaster.md) — selects the master variable
