---
keyword: EventLoad
summary: Prepares the selected hardware event table without arming outputs.
availability:
  standalone: []
  central-i:
  - v5
can_code: 970
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
last_updated: '2026-10-28'
doc_revision: '2026.10'
---
# EventLoad

For AGM800 `EventType=3`, this argument-free command starts a bounded background preload of `EventTableBeg..EventTableEnd` (inclusive), containing 1–2048 rows. It does not arm outputs or start motion.

Configure positions, [EventTblMode](EventTblMode.md), widths, outputs and source first. For a corrected source, run [EventCorrect](EventCorrect.md) and inspect the resulting `EventTableCor` before loading. Establish the normal lock/event coordinate alignment at standstill before loading. The loader applies the existing table offset and hardware-coordinate conversion once.

Read [EventStatus](EventStatus.md): Loading is bit 0, Ready bit 1 and Fault bit 4. `EventOn=1` is admitted only after the complete load is Ready. Failed, interrupted or uncertain transfers cannot auto-arm.

`EventOn=0` cancels/stops and discards the prepared run. Every run requires a fresh preload of the selected range. Relevant edits invalidate a prepared load; active-run edits are refused. A disconnect discards the job rather than adopting or resuming it after reconnect. Ordinary command/communication errors report failures; no EventAbort/EventAckErr/EventError ceremony is required.

The converted effective pulse width must fit the original hardware's 13-bit field (0–8191 units after fine/coarse conversion); an unrepresentable width fails preparation before arm instead of being truncated.

If a selected output cannot finish its pulse and recovery before the next event, the run faults. Stop, correct the settings and explicitly load again; there is no delayed-event queue or automatic retry.

```text
AEventOn=0
AEventType=3
AEventTableBeg=5
AEventTableEnd=100
AEventTblMode=0
; Upload rows and configure source/settings before loading.
AEventLoad
AEventStatus        ; wait for Ready and check Fault
AEventOn=1          ; arm only after Ready
AEventOn=0          ; stop/discard; reload before another run
```
