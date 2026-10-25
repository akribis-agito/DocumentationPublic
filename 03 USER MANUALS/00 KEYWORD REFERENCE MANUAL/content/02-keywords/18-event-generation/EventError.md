---
keyword: EventError
summary: Reads the first retained hardware-table failure and its original cause.
availability:
  standalone: []
  central-i:
  - v5
can_code: 974
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 13
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
# EventError

Reads the first retained hardware-table failure and its original cause.

Usable indices are **1–12**; index 0 is reserved. LONG32 words carry raw unsigned 32-bit patterns where applicable. Read this array inside the [EventStatus](EventStatus.md) sequence bracket; separate unbracketed reads can mix publications.

| Index | Meaning |
|---|---|
| 1 | Normalized error code |
| 2 | Failure phase |
| 3 | Original external table index; 0 when inapplicable |
| 4 | Command opcode |
| 5 | Original CiQStatus transport result |
| 6 | Command sequence |
| 7 | Session token low 32 bits |
| 8 | Session token high 32 bits |
| 9 | Occurrence time in ms |
| 10 | Raw remote RESULT/FAULT word |
| 11 | Central-i port (1-based) |
| 12 | Error occurrence number |

## Codes

0 none; 1 invalid count; 2 position/range/order; 3 settings/alignment; 4 busy/ownership; 5 unsupported; 6 timeout; 7 CRC; 8 malformed/identity reply; 9 remote rejected; 10 stored-table verification mismatch; 11 deliberate abort (normally latest result only); 12 port down; 13 reset; 14 source/configuration changed; 15 missed target; 16 output busy; 17 stale; 18 internal.

Phases: 0 none, 1 validate, 2 BEGIN, 3 APPEND, 4 VERIFY, 5 ARM, 6 run, 7 snapshot, 8 abort, 9 recovery, 10 acknowledge. Opcodes: 1 BEGIN, 2 APPEND, 3 VERIFY, 4 ARM, 5 ABORT, 6 ACK_ERROR, 7 SNAP. A locally refused command has command sequence 0 when no matching remote command was submitted. [5] is the original transport result, independently of the application result/fault in [10]; neither should be substituted for the other.

The first visible tuple is immutable until eligible [EventAckErr](EventAckErr.md) completion. Later Busy refusals or Abort requests do not erase it. EventStatus[21] independently reports the latest normalized operation result. A later failure hidden behind an admission error can become the next occurrence after that admission error is acknowledged. An unmappable or different-session remote row reports index 0 rather than pointing into the new selection.
