---
keyword: ScopeStatus
summary: Reports the current state of the Central-i scope.
availability:
  standalone: []
  central-i:
  - v5
can_code: 745
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 6
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
# ScopeStatus

Reports the current state of the Central-i scope.

## Overview

`ScopeStatus` is a read-only array that reports the live state of the Central-i scope: its run state, how much buffer space is free, the current packet size, a running packet identifier, and a count of lost samples. It lets a host poll the scope started by [ScopeOn](ScopeOn.md) to decide when to call [ScopeUpload](ScopeUpload.md). It is a non-axis status variable and is not saved to flash.

## How it works

The array is 1-indexed. Each element reports one aspect of the scope:

| Index | Reports | Meaning |
|---|---|---|
| 1 | Packet size | Number of buffer slots one captured sample occupies (a time stamp plus one slot per configured signal). 0 or 1 means no signals are configured, so nothing is being captured. |
| 2 | Free space | Number of free slots remaining in the capture buffer. A full packet can be stored only while this is at least the packet size (index 1). |
| 3 | Run state | `0` not capturing; `1` capturing; `2` paused because the buffer is full. The scope resumes from the paused state automatically once [ScopeUpload](ScopeUpload.md) frees space. |
| 4 | Packet identifier | Counter that advances by one each time a sample is due, whether or not it could be stored — useful for detecting gaps. |
| 5 | Lost-samples counter | Number of due samples that could not be stored because the buffer was full. |

A host typically starts the scope with [ScopeOn](ScopeOn.md), then polls index 3 for the run state and index 2 for accumulated data, and calls [ScopeUpload](ScopeUpload.md) to retrieve completed packets. A non-zero, growing index 5 indicates the buffer is not being uploaded fast enough — lower the rate with [ScopeGap](ScopeGap.md) or upload more often.

## Examples

```text
AScopeStatus[3]      ; query the scope run state (0 idle, 1 capturing, 2 paused-full)
AScopeStatus[2]      ; query free buffer space
AScopeStatus[5]      ; query the lost-samples counter
```

## See also

- [ScopeOn](ScopeOn.md) — start/stop the scope
- [ScopeUpload](ScopeUpload.md) — retrieve captured data
- [ScopeAbout](ScopeAbout.md) — snapshot of the captured set
