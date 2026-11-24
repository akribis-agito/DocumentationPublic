---
keyword: BeginSkipProt
summary: Selects Orbit FR software position-limit handling for supported Begin moves.
last_updated: '2026-11-24'
doc_revision: '2026.11'
can_code: 917
availability:
- ci-master
products:
- agm800
attributes:
  access: rw
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
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# BeginSkipProt

This per-axis keyword exists only in the Orbit FR AGM800 firmware. Its default is 0. At 0 the normal software position-limit checks apply. At 1 the Orbit motion code skips the forward/reverse software position-limit target checks for supported point-to-point, repetitive and vector Begin moves and the corresponding point-to-point target clipping. Hardware-limit checks remain active. Other motion protections retain their own conditions.

The setting is volatile. Read `ABeginSkipProt` to inspect axis A. CAN code 917. [FwdPLim](FwdPLim.md)
