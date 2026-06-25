---
keyword: MotorLearnPl
summary: A read-only result reported after an automatic-mode motor-learning pass completes (MotorLearnSta = 3).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 447
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 50
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# MotorLearnPl

**Definition:**

MotorLearnPl is a read-only result reported after an automatic-mode motor-learning pass completes (MotorLearnSta = 3). For a rotary motor it is the learned number of pole pairs (the count of electrical cycles spanning one mechanical revolution, in the range 1 to 50); for a linear motor it is reported as 1. It is updated only by automatic-mode learning, not by manual-mode learning. It is an axis-related status variable and is not saved to flash.

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnSta](MotorLearnSta.md), [MotorLearnRes](MotorLearnRes.md)
