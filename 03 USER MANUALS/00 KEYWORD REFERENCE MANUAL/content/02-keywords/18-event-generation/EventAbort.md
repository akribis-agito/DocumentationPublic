---
keyword: EventAbort
summary: Requests disarm and bounded remote cleanup for the hardware table session.
availability:
  standalone: []
  central-i:
  - v5
can_code: 971
attributes:
  access: ro
  scope: axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: func
  range:
  - 0
  - 0
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventAbort

Requests disarm and bounded remote cleanup for the hardware table session.

With EventType=3, EventAbort and EventOn=0 request the same cleanup. EventOn clears immediately, pending enable publication is cancelled, and firmware requests remote inhibition/cleanup. Poll coherent [EventStatus](EventStatus.md) for confirmed Aborted and no pending cleanup. A command reply, local timeout or Fault alone is not confirmation that remote outputs are idle.

The latest operation result becomes 11 (deliberate abort). This does not create or replace the retained first [EventError](EventError.md); a cleanup failure can create an error if none was already retained. Remote uncertainty retains ownership and fences configuration until confirmed recovery. Repeating Abort requests recovery rather than replaying an ambiguous APPEND. After confirmed cleanup, acknowledge retained errors with [EventAckErr](EventAckErr.md), then [EventLoad](EventLoad.md) a new session.

After normal Complete, explicitly Abort and confirm Aborted before EventAckErr releases ownership to Empty, for pulse and toggle alike. A PC reconnection does not prove commands from its old connection have retired. If an old mutation may still arrive, the SDK must retain RecoveryRequired until command retirement is proven; a new live status read alone cannot authorize replacement recovery or arming.
