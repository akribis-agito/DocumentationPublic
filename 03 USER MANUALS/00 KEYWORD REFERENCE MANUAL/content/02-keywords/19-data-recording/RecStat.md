---
keyword: RecStat
summary: Reports the recording status of each scope.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 249
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 0
  - 5
  default: 0
  scaling: 1.0
  implemented: final
overrides: {}
---
# RecStat

Reports the recording status of each scope.

## Overview

`RecStat` reports the recording status of each scope, allowing a host to track progress from pre-trigger fill through completion before calling [RecUpload](RecUpload.md). It is the read-back counterpart to the [RecStart](RecStart.md) / [RecStop](RecStop.md) commands. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## How it works

The value returned from `RecStat` is defined as shown.

| Value | Status |
|----|----|
| 0 | Invalid recorded data (default condition upon power up) |
| 1 | Scope is filling pre-trigger data, as defined by RecTrigPos |
| 2 | Pre-trigger data are filled. Scope is buffering and waiting for the trigger. |
| 3 | Trigger is detected and recording is progressing. |
| 4 | Recording is completed without interruption. |
| 5 | Recording is stopped. |
| 6 | Recording is stopped before trigger is detected. |

For example, if RecStat\[1\] returns the value of 4, it indicates that recording of the first scope is successful, and the user can begin to stream the recorded data.

## Examples

```text
RecStat[1]?         ; query the recording status of the first scope
```

## See also

- [RecStart](RecStart.md) — start recording
- [RecStop](RecStop.md) — stop recording
- [RecTrigPos](RecTrigPos.md) — pre-trigger data (status 1)
- [RecUpload](RecUpload.md) — stream data once status is 4
