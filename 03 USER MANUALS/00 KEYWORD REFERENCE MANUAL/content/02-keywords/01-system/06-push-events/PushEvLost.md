---
keyword: PushEvLost
summary: Push events dropped since the last packet was sent.
availability:
  standalone: []
  central-i:
  - v5
can_code: 909
attributes:
  access: rw
  scope: non-axis
  flash: false
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 2147483647
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
last_updated: '2026-09-25'
doc_revision: '2026.09'
---
# PushEvLost

Push events dropped since the last packet was sent.

## Overview

`PushEvLost` counts the [push events](00-overview.md) the controller had to drop because the event queue was full, since the last packet was sent successfully. The same count is sent to the host in every packet header, as the `missed` field, so a host that reads the push socket learns about lost events without polling this keyword.

It is a non-axis counter, not saved to flash, and reads 0 after power-up.

## How it works

- When the 64-row queue is full, the **new** event is dropped and both `PushEvLost` and [PushEvTotLost](PushEvTotLost.md) are incremented. Events already in the queue are kept.
- When a packet is built, its `missed` field takes the current value of `PushEvLost`, capped at 65535. After the packet is sent successfully, exactly that amount is subtracted from `PushEvLost`. Events dropped while the packet was being built, and any count above 65535, are therefore reported in the next packet rather than lost.
- If a send fails, `PushEvLost` is not changed.
- A 0↔1 change of [PushEvEnable](PushEvEnable.md) clears it to 0.

The keyword is writable, so a host can also reset it by writing 0.

## Examples

```text
APushEvLost          ; events dropped since the last successful send
APushEvLost=0        ; clear the counter
```

## See also

- [PushEvTotLost](PushEvTotLost.md) — dropped events since power-on, never cleared automatically
- [PushEvStat](PushEvStat.md) — free rows in the queue
- [PushEvFlushMs](PushEvFlushMs.md) / [PushEvFillPct](PushEvFillPct.md) — when the queue is sent
