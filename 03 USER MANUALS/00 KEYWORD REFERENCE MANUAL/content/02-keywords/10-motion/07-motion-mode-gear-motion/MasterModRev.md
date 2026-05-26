---
keyword: MasterModRev
availability:
  standalone:
  - v4
  central-i:
  - v4
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
overrides: {}
---
# MasterModRev

**Definition:**

MasterModRev is the modulo divisor used to ensure the correct accumulation of MasterPos, only if GearMaster points to the variable involved in modulo operation. Master variable undergoes modulo operation if

1.  ModRev related to the master variable is non-zero, and

2.  it is generally either [Pos](../../../02-keywords/10-motion/01-kinematics-status/Pos.md), PDPos, [MasterPos](../../../02-keywords/10-motion/07-motion-mode-gear-motion/MasterPos.md), [PosRef](../../../02-keywords/10-motion/01-kinematics-status/PosRef.md) or [AbsTrgt](../../../02-keywords/10-motion/03-kinematics-configuration/AbsTrgt.md)

User must set MasterModRev to match the ModRev related to the master variable (manual assignment). Conversely, if the master variable does not involve in modulo operation, MasterModRev must be 0.

The delta is corrected if its absolute value is more than half of MasterModRev, where master variable is assumed to have undergone modulo operation.
