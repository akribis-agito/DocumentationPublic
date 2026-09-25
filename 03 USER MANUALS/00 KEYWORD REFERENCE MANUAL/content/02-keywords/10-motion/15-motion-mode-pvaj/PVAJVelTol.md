---
keyword: PVAJVelTol
summary: Velocity-continuity tolerance applied by PVAJValidate.
availability:
  standalone: []
  central-i:
  - v5
can_code: 885
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: float
  ok_in_motion: true
  ok_motor_on: true
  units: counts/second
  default: 100.0
  scaling: 1.0
  implemented: final
last_updated: '2026-08-04'
doc_revision: '2026.08'
---
# PVAJVelTol

The velocity tolerance [PVAJValidate](PVAJValidate.md) allows between what one [PVAJList](PVAJList.md) row states and what the quintic through the neighbouring rows implies at that point. Counts per second.

A full validation that fails on velocity reports error `397`.

Default `100.0` — looser than [PVAJPosTol](PVAJPosTol.md) in proportion, because a velocity column is usually the differentiated product of a trajectory generator and carries that differentiation's noise. The tolerance is not applied when [PVAJValidate](PVAJValidate.md) is called with `2` (none) or `3` (partial).
