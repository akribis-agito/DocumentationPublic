---
keyword: EventStatus
summary: Reports compact hardware-table loading and run flags.
availability:
  standalone: []
  central-i:
  - v5
can_code: 973
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
  - -2147483648
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-10-28'
doc_revision: '2026.10'
---
# EventStatus

Read-only scalar flags for the AGM800 original-engine preload (`EventType=3`). This is a compact status word, not the older verified-engine status array.

| Bit | Mask | Meaning |
|-----|------|---------|
| 0 | 1 | Loading: the firmware is preparing/transferring rows. |
| 1 | 2 | Ready: the complete selected table has passed the final admission check. |
| 2 | 4 | Enabled: the hardware-table run is enabled. |
| 3 | 8 | Complete: the run has completed. |
| 4 | 16 | Fault: the load or run failed; stop and explicitly reload. |

Loading is local firmware state. Ready/Fault and run state use the normal cyclic hardware status; automatic per-event offline counter/next-position reads are not needed. `EventCntr` is refreshed once after completion. Use an explicit inquiry if an intermediate count is needed.

Issue [EventLoad](EventLoad.md) after configuration, wait until Ready is set and Fault is clear, then arm with `EventOn=1`. `EventOn=0` stops/cancels and discards the job. Reconnect never resumes it. Relevant edits invalidate readiness and are refused during active operation. No error acknowledgement command is required.

In hardware-table mode `Vel[4]=0` because 1/T is unavailable. Other event types preserve their status meanings.

```text
AEventStatus
AEventCntr
```
