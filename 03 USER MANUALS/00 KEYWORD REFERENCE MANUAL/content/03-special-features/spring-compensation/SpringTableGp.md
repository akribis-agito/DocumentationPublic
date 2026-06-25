---
keyword: SpringTableGp
summary: A reserved, not-yet-implemented keyword, expressed in user units, that is associated with the (also not-yet-implemented) [SpringTable](SpringTable.md).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 598
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - 1
  - 10000000
  default: 100
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# SpringTableGp

**Definition:**

SpringTableGp is a reserved, not-yet-implemented keyword, expressed in user units, that is associated with the (also not-yet-implemented) [SpringTable](SpringTable.md). Its intended role is the position spacing (gap) between successive SpringTable entries; it accepts values from 1 to 10000000, with a default of 100. It currently has no effect on spring compensation; the active compensation is the linear model defined by [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md), [SpringPosFFW](SpringPosFFW.md), and [SpringCurrFFW](SpringCurrFFW.md). It is an axis-related parameter expressed in user units, saved to flash, and can be changed at any time.

**See also:**

[SpringTable](SpringTable.md), [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md)
