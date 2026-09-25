---
keyword: PushEvTotLost
summary: Push events dropped since power-on.
availability:
  standalone: []
  central-i:
  - v5
can_code: 910
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
# PushEvTotLost

Push events dropped since power-on.

## Overview

`PushEvTotLost` counts every [push event](00-overview.md) the controller has dropped because the event queue was full, since power-on. It is incremented together with [PushEvLost](PushEvLost.md), but, unlike `PushEvLost`, it is **never cleared automatically**: a successful send and a change of [PushEvEnable](PushEvEnable.md) both leave it unchanged.

It is a non-axis counter, not saved to flash, and reads 0 after power-up. It is writable, so a host can reset it by writing 0.

Events are detected and queued whether or not a host is connected to the push socket. A rising `PushEvTotLost` therefore shows that events are occurring and not being collected, even to a user who only reads keywords.

## Examples

```text
APushEvTotLost       ; total events dropped since power-on
APushEvTotLost=0     ; reset the total
```

## See also

- [PushEvLost](PushEvLost.md) — dropped events since the last successful send
- [PushEvStat](PushEvStat.md) — free rows in the queue
- [Push Events overview](00-overview.md)
