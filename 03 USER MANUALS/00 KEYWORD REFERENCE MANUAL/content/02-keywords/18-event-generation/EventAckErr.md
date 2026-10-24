---
keyword: EventAckErr
summary: Acknowledges an eligible retained hardware-table error without implicitly rearming.
availability:
  standalone: []
  central-i:
  - v5
can_code: 972
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
# EventAckErr

Acknowledges an eligible retained hardware-table error without implicitly rearming.

[EventError](EventError.md) keeps the first visible failure until an eligible acknowledgement completes. EventAckErr is asynchronous when remote acknowledgement/recovery is required. Poll coherent [EventStatus](EventStatus.md) and EventError; a command acceptance is not acknowledgement completion. EventAckErr never loads or arms a table.

After normal Complete, both pulse and toggle jobs retain ownership until explicit EventAbort → confirmed Aborted → EventAckErr → confirmed Empty. A deliberate Abort can produce Aborted without a retained first error; acknowledgement still releases that ownership. Complete itself is not acknowledgement-admissible.

A local admission error can be cleared when the engine is known disarmed, including a valid Ready session that has not begun arming. Such an acknowledgement preserves that Ready session. If a later core failure occurred behind the retained admission error, clearing the admission error publishes that core failure with a new occurrence number; it does not briefly publish healthy status. A second acknowledgement can then be necessary.

Pending acknowledgement, uncertain cleanup, an arm in progress or an active sequence can refuse acknowledgement (immediate error 151 with the retained diagnostic unchanged). Complete [EventAbort](EventAbort.md) recovery first when required. If acknowledgement fails, Abort can establish confirmed cleanup before another acknowledgement attempt. Inspect the error occurrence and pending flags rather than assuming a cleared error from a reply alone.
