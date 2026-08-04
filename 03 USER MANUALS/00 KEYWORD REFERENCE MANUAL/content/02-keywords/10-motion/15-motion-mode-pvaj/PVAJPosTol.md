---
keyword: PVAJPosTol
summary: Position-continuity tolerance applied by PVAJValidate.
availability:
  standalone: []
  central-i:
  - v5
can_code: 884
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: counts
  default: 1.0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
---
# PVAJPosTol

The position tolerance [PVAJValidate](PVAJValidate.md) allows between what one [PVAJList](PVAJList.md) row states and what the quintic through the neighbouring rows implies at that point. Counts.

Raise it to accept a list generated at coarser precision than the controller's own arithmetic; lower it to insist on a tighter fit. A full validation that fails on position reports error `396`.

Default `1.0`. The tolerance is not applied when [PVAJValidate](PVAJValidate.md) is called with `2` (none) or `3` (partial), neither of which checks continuity.
