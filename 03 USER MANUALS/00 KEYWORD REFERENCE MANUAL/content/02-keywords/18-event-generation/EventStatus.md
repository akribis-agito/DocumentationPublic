---
keyword: EventStatus
summary: Reads a coherent RAM publication of hardware-table capability, progress and state.
availability:
  standalone: []
  central-i:
  - v5
can_code: 973
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 25
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventStatus

Reads a coherent RAM publication of hardware-table capability, progress and state.

Usable indices are **1–24**; index 0 is reserved. Each element is LONG32. Treat bitfields, CRCs, tokens and sequences as unsigned 32-bit patterns, even when the transport displays a negative signed value. These reads use published RAM and do not issue a remote command per element.

## Coherent read

Read head [1], payload [2]..[23] and [EventError](EventError.md)[1]..[12], tail [24], then head [1] again. Accept only if all three sequence values are identical and even. Retry within a bounded client deadline; a partial reply, odd sequence, changed head or timeout is not a valid snapshot. Configuration invalidation can immediately mark the publication odd. In stable nonpending Empty, Ready, Complete, Aborted or Fault, otherwise unchanged telemetry (including command sequence and age) has a five-second minimum publication interval. Other owned activity coalesces at 100 ms; unowned idle telemetry at 1 s. State, freshness/ready-valid flags, session/configuration, errors and reconnect invalidation publish immediately. Reads never latch data or postpone publication.

A complete attempt uses exactly 37 live requests. If each attempt finishes within two seconds, retry a torn attempt immediately within a bounded total deadline: one periodic terminal telemetry publication cannot tear both attempts. Safety changes may still prevent success. Return unavailable rather than use cached Ready. Running may change too quickly for slow serial observation; observe terminal Complete afterward. The SDK must validate its actual transport latency; these intervals are not a baud-rate guarantee.

Age is conservative from the remote SNAP request start **to publication**, not to getter completion or current wall-clock time. A small retained age is not proof of ongoing freshness. Arm still obtains a new matching remote snapshot, and Complete originates from a fresh final inquiry.

| Index | Meaning |
|---|---|
| 1 | Publication sequence (head) |
| 2 | State |
| 3 | Flags |
| 4 | Supported capacity; 0 when unavailable |
| 5 | Requested entry count |
| 6 | Accepted entries |
| 7 | Committed entries |
| 8 | Retired targets |
| 9 | Remaining targets |
| 10 | Occupancy |
| 11 | Session token low 32 bits |
| 12 | Session token high 32 bits |
| 13 | Expected CRC |
| 14 | Stored-RAM CRC |
| 15 | Remote command sequence |
| 16 | Snapshot age in ms; 0xFFFFFFFF when absent |
| 17 | Remote clock in Hz; 0 when unsupported |
| 18 | Selected source |
| 19 | Configuration generation |
| 20 | Master-coordinate generation |
| 21 | Latest normalized operation result |
| 22 | Busy output mask |
| 23 | Raw remote CAPS |
| 24 | Publication sequence (tail) |

States: 0 Empty, 1 Loading, 2 Verifying, 3 Ready, 4 Armed, 5 Running, 6 Complete, 7 Aborted, 8 Fault. Flags: bit 0 supported, bit 1 fresh remote snapshot, bit 2 Ready-valid, bit 3 error retained, bit 4 operation pending. Supported and Ready-valid are different conditions. Require a fresh matching session before accepting Armed/Running or Complete. Complete requires all targets retired and the final pulse tail finished; Fault is not confirmed Abort. Error codes for [21] use the EventError normalization; 11 means an explicit abort request, not necessarily a new retained failure.

See [EventLoad](EventLoad.md) for the loading/arming workflow and [EventAbort](EventAbort.md) for recovery.
