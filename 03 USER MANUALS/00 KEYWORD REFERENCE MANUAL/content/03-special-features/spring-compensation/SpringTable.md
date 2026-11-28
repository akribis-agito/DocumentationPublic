---
keyword: SpringTable
summary: A reserved, not-yet-implemented array keyword (size 41, with usable indices 1 through 40).
availability:
- controller
- ci-master
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
  - -16000
  - 16000
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    range:
    - -64000
    - 64000
  agc300-et:
    range:
    - -4000
    - 4000
  agc301-et:
    range:
    - -4000
    - 4000
  agc301-et-bioxtreme:
    range:
    - -4000
    - 4000
  agd200-et-2d01:
    range:
    - -4000
    - 4000
  agd200-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d01:
    range:
    - -4000
    - 4000
  agd301-et-2d02:
    range:
    - -8000
    - 8000
  agd301-et-2d09:
    range:
    - -25500
    - 25500
  agd155-af-2a06:
    range:
    - -25500
    - 25500
  agd155-af-2a10:
    range:
    - -28500
    - 28500
  agd155-ec:
    range:
    - -25500
    - 25500
  agd155-ec-var34:
    range:
    - -28500
    - 28500
  agd155-ec-var34-3:
    range:
    - -42500
    - 42500
  agd156-ec:
    range:
    - -12726
    - 12726
  agd101-ec-34a:
    range:
    - -28280
    - 28280
  agd101-ec-17a:
    range:
    - -14140
    - 14140
last_updated: '2026-05-29'
doc_revision: '2026.06'
---
# SpringTable

**Definition:**

SpringTable is a reserved, not-yet-implemented array keyword (size 41, with usable indices 1 through 40). It currently has no effect on spring compensation. The active compensation is the linear model defined by [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md), [SpringPosFFW](SpringPosFFW.md), and [SpringCurrFFW](SpringCurrFFW.md). When implemented, its entries would hold per-segment current corrections, 1-indexed. It is an axis-related array parameter saved to flash and can be changed at any time.

**See also:**

[SpringOn](SpringOn.md), [SpringTableGp](SpringTableGp.md), [SpringPLow](SpringPLow.md), [SpringPHigh](SpringPHigh.md)
