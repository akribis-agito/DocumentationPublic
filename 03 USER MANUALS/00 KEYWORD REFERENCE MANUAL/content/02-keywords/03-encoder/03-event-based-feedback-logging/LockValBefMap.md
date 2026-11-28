---
summary: Reports the latest position-lock capture in the coordinate system before error mapping.
last_updated: '2026-11-23'
doc_revision: '2026.11'
keyword: LockValBefMap
can_code: 957
availability:
- controller
- ci-master
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: user
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides:
  ci-master:
    data_type: int64
    range:
    - -2251799813685248
    - 2251799813685247
---
# LockValBefMap

`LockValBefMap` (CAN 957) is a read-only, per-axis position. Read it when you need the latest lock capture in the same coordinates as `PosBeforeMap` or an `EventPos` target. The controller takes it from the same capture as `LockVal`. The value includes the capture’s coordinate offset and excludes the error-map table, `MapErrOffset` and both map ramps. [PosBeforeMap](../../04-error-mapping/PosBeforeMap.md)

For a main-encoder strobe the value uses the latched counter. A software capture uses the position sampled in the control cycle that handles the event. On a Central-i master, ancillary counter selections 0 and 1 in `EncSinCosHWEn` use the remote latch with the pre-map offset. Sources 2 and 3 use their virtual-encoder or auxiliary-encoder coordinates for both lock values. [LockSrc](LockSrc-AuxLockSrc.md)

Read `ALockValBefMap` for axis A. To compare it with `ALockVal`, read `ALockCntr` before and after the pair and retry if the count changes. Compare captures within the same logging session. Re-arming clears the counter and retains the last captured values until another capture arrives. On AGM800 and AGM800-EC, the pre-map position is 64-bit and `LockVal` is 32-bit. When working in encoder counts, the difference gives the applied correction modulo 2³². [LockVal](LockVal-AuxLockVal.md) · [LockCntr](LockCntr-AuxLockCntr.md)

A captured pre-map position can be reused directly as an event target when `EventTableSrc=0`. Source 1 expects a compensated target and performs its own inverse mapping. A two- or three-dimensional map, or a map indexed by another encoder, needs additional coordinates to reconstruct the compensated position at the capture. [EventTableSrc](../../18-event-generation/EventTableSrc.md)
