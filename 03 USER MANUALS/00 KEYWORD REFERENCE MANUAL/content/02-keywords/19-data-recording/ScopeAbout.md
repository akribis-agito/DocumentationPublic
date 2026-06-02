---
keyword: ScopeAbout
summary: Reports metadata about the current Central-i scope session.
availability:
  standalone: []
  central-i:
  - v5
can_code: 746
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 10
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
last_updated: '2026-06-02'
doc_revision: '2026.06'
---
# ScopeAbout

Reports metadata about the current Central-i scope session.

## Overview

`ScopeAbout` is a read-only array that reports metadata about the current scope session: session information plus a snapshot of the captured-signal list. It lets a host application interpret the data returned by [ScopeUpload](ScopeUpload.md) without separately re-querying the configuration. The snapshot is taken at the moment the scope is enabled by [ScopeOn](ScopeOn.md), so it reflects the configuration the captured data was actually recorded with, even if [ScopeParams](ScopeParams.md) is changed afterward. It is a non-axis status variable and is not saved to flash.

## How it works

The array is 1-indexed. Its leading elements carry session metadata (such as the session start time), and the remaining elements mirror the configured signal list from [ScopeParams](ScopeParams.md), so a host can pair each captured column in an upload with the signal it represents. The snapshot is refreshed each time the scope transitions from off to on through [ScopeOn](ScopeOn.md).

Because the sampling interval is taken live from [ScopeGap](ScopeGap.md) (it can be changed on the fly), it is not part of this snapshot; read it from [ScopeGap](ScopeGap.md) directly. This keyword is the Central-i-scope counterpart of [LoggerAbout](LoggerAbout.md).

## Examples

```text
AScopeAbout[1]      ; query the first session-metadata entry
AScopeAbout[4]      ; query a captured-signal entry from the session snapshot
```

## See also

- [ScopeOn](ScopeOn.md) — start/stop the scope
- [ScopeParams](ScopeParams.md) — signals the scope captures
- [ScopeUpload](ScopeUpload.md) — retrieve captured data
- [LoggerAbout](LoggerAbout.md) — equivalent metadata for the continuous logger
