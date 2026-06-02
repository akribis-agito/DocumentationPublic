---
keyword: MotorLearnOn
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 444
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# MotorLearnOn

**Definition:**

MotorLearnOn enables the motor-learning routine, which drives the motor open-loop (advancing the commutation electrical angle in MotorLearnInc steps, per the mode selected by MotorLearnMod) to measure and report the motor pole pairs (MotorLearnPl) and the encoder resolution (MotorLearnRes); progress is reported by MotorLearnSta. The valid values are 0 (off) and 1 (on). Setting it to 1 automatically enables the motor and clears the last controller-fault and motor-off reasons. The routine produces results for rotary or linear brushless motors. In automatic mode the controller clears MotorLearnOn back to 0 and turns the motor off once the pass finishes (MotorLearnSta = 3) or fails (MotorLearnSta = 4); a rotary pass fails if more than 20 electrical cycles elapse without locating two consecutive index pulses. It cannot be changed while the axis is in motion; it can be changed with the motor on. It is an axis-related parameter and is not saved to flash.

**See also:**

[MotorLearnMod](MotorLearnMod.md), [MotorLearnSta](MotorLearnSta.md), [MotorLearnRes](MotorLearnRes.md), [MotorLearnInc](MotorLearnInc.md)
