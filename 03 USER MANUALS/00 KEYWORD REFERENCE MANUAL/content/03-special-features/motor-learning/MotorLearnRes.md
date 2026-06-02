---
keyword: MotorLearnRes
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 446
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
  - 0
  - 10000000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# MotorLearnRes

**Definition:**

MotorLearnRes is a read-only result reported after a motor-learning pass completes: the encoder resolution measured during the pass. For a rotary motor it is the encoder counts between two consecutive index (marker) pulses, i.e. the counts per mechanical revolution; the value is reported only after an automatic-mode pass finishes (MotorLearnSta = 3). For a linear motor it is the estimated resolution derived from the distance traveled over one electrical cycle. It is an axis-related status variable and is not saved to flash.

**See also:**

[MotorLearnOn](MotorLearnOn.md), [MotorLearnSta](MotorLearnSta.md), [MotorLearnPl](MotorLearnPl.md)
