---
keyword: LockEventStat
summary: Reports legacy, valid, uncomputed or stale lock/event offset state.
availability:
  standalone: []
  central-i:
  - v5
can_code: 833
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
  - -2
  - 1
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-17'
doc_revision: '2026.10'
---
# LockEventStat

Reports the offset state used by [LockEventMode](LockEventMode.md). It is a read-only axis value.

| Value | Meaning |
| --- | --- |
| `0` | Legacy mode 0. Offset learning occurs on arming; this status is not a measurement certificate. |
| `1` | The applicable offset is valid. |
| `-1` | No offset has been computed. |
| `-2` | A previously computed offset is stale. |

In mode 1, run [LockEventInit](LockEventInit.md) with the source stationary after invalidation. In mode 2, firmware attempts recomputation while both features are off when tracked dependencies change or the remote reconnects. Check the resulting state before arming when the selected source requires an ancillary counter. A repeated assignment of mode 2 does not force a new measurement; `LockEventInit` does.

An applicable uncomputed offset refuses arming with error 335; a stale offset refuses it with error 404. A failed ancillary read leaves the offset invalid. The main absolute-encoder source does not need this offset and may leave the status unchanged.

Status 1 assumes a compatible remote FPGA. Historical v4.3.6 returns zero for unmapped ancillary reads and cannot certify this measurement; see [remote FPGA compatibility](LockEventInit.md#remote-fpga-compatibility).

See also: [LockEventInit](LockEventInit.md), [LockEventMode](LockEventMode.md), [LockEn](LockEn-AuxLockEn.md), [EventOn](../../18-event-generation/EventOn.md).
