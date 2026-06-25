---
keyword: SpringTable
summary: A reserved, not-yet-implemented array keyword (size 41, with usable indices 1 through 40).
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 597
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 41
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -64000
  - 64000
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# SpringTable

**Definition:**

SpringTable is a reserved, not-yet-implemented array keyword (size 41, with usable indices 1 through 40). It currently has no effect on spring compensation. The active compensation is the linear model defined by [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md), [SpringPosFFW](SpringPosFFW.md), and [SpringCurrFFW](SpringCurrFFW.md). When implemented, its entries would hold per-segment current corrections, 1-indexed. It is an axis-related array parameter saved to flash and can be changed at any time.

**See also:**

[SpringOn](SpringOn.md), [SpringTableGp](SpringTableGp.md), [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md)
