---
keyword: MotorLearnMod
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 449
attributes:
  access: rw
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: false
  ok_motor_on: true
  units: none
  range:
  - 0
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# MotorLearnMod

**Definition:**

MotorLearnMod selects the mode used by the motor-learning routine, which drives the motor open-loop to measure the number of pole pairs and the encoder resolution. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

| Value | Meaning |
|---|---|
| 0 | Automatic |
| 1 | Manual (manually find the number of pole pairs) |

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnInc](MotorLearnInc.md), [MotorLearnPl](MotorLearnPl.md)
