---
keyword: EventLoad
summary: Preloads and verifies a finite hardware position-event table before arming.
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
last_updated: '2026-10-25'
doc_revision: '2026.10'
---
# EventLoad

Preloads and verifies a finite hardware position-event table before arming.

## Availability

Central-i master firmware must advertise the verified-table API in [Identity](../01-system/01-status/Identity.md). The connected remote must independently advertise the compatible table engine; [EventStatus](EventStatus.md) reports its current capability. An API bit alone does not establish remote support or a qualified event rate.

## Prepare and load

1. Keep the selected position source stationary. Configure the source, [EventType](EventType.md) = 3, positions, widths and output selections. Set [LockEventMode](../03-encoder/03-event-based-feedback-logging/LockEventMode.md) = 1, run [LockEventInit](../03-encoder/03-event-based-feedback-logging/LockEventInit.md), and confirm LockEventStat = 1. EventLoad does not implicitly learn the source alignment.
2. Select inclusive EventTableBeg..EventTableEnd: **1–2048 entries**. EventTableSrc selects EventTable or EventTableCor. Positions must be strictly ordered in one direction, both in the original controller coordinates and after correction into the remote's signed 32-bit counter frame. Rollover and out-of-range targets are refused.
3. If EventTableSrc=1, run bare [EventCorrect](EventCorrect.md) after uploading the selected inputs and require successful completion; uploading EventTable does not regenerate EventTableCor. Software must fence generations before correction/readback, read back all three selected input columns and settings, and require only the correction command’s one source/table generation increment modulo32. Source0 readback permits no increment. Ready must match the final generations.
4. Run EventLoad. Acceptance starts asynchronous work; it does not mean Ready. The controller retains a private copy, loads every record, and asks the remote to verify a CRC over the stored RAM image. EventCntr and EventNextPos clear when a new load is accepted.
5. Poll coherent EventStatus until state Ready **and** the Ready-valid flag are present for the intended session. Then write [EventOn](EventOn.md) = 1 while the source remains before the first target in the selected direction. Equality or an already-passed first target is refused. EventOn reads 1 only after a fresh remote Armed/Running confirmation.

An immediate command rejection returns error 151; asynchronous failures are retained in [EventError](EventError.md). Correct configuration and acknowledge an eligible error before trying again. A load while another job owns the engine is refused without replacing that job.

## Execution and invalidation

This is a finite burst: no runtime refill, implicit repeat, or EventAlwaysOn streaming. Hardware consumes the verified table without per-event host writes. Completion requires all targets retired and the final pulse tail completed; toggle output levels may remain until explicit Abort. EventCntr is the retired-target count. EventNextPos uses the retained original controller coordinate of the next target, rather than a corrected remote coordinate.

Changing a captured table, source, origin or pulse configuration invalidates the session and inhibits further events; load and verify again. A controller/remote link reset requires a new load after recovery. Loss of the PC connection alone does not promise to stop an autonomous healthy remote sequence: explicitly request [EventAbort](EventAbort.md) and confirm its result.

The field acceptance target is 500 kHz–1 MHz target events on AGM800 + AGA101 with an incremental motor. This is a qualification requirement, not a measured rating. A 2048-entry table represents 4.096 ms at 500 kHz or 2.048 ms at 1 MHz in target periods; it is not an indefinite stream. One million toggle events per second forms a 500 kHz square wave.
