---
keyword: GearMaster
summary: Complex CAN code selecting the master variable for gear motion.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 489
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
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# GearMaster

Complex CAN code selecting the master variable for gear motion.

## Overview

`GearMaster` is the [complex CAN code](../../../01-keyword-usage-and-syntax/complex-can-code.md) of the master variable used in gear motion ([MotionMode](../02-motion-configuration/MotionMode.md) `= 5` or `6`). The change in the selected master variable is scaled by [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) and accumulated into [MasterPos](MasterPos.md). If the master variable participates in a modulo operation, set [MasterModRev](MasterModRev.md) accordingly.

## Examples

```text
AGearMaster         ; read the complex CAN code of the master variable
```

## See also

- [MasterPos](MasterPos.md) — accumulated, scaled master position
- [MasterFact](MasterFact.md) / [MasterFactDen](MasterFactDen.md) — gear ratio numerator / denominator
- [MasterModRev](MasterModRev.md) — modulo divisor for the master variable
- [MotionMode](../02-motion-configuration/MotionMode.md) — selects gear motion (`= 5` or `6`)
