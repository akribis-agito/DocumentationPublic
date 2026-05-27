---
keyword: RecStop
summary: Command that stops recording on the selected scope.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 250
attributes:
  access: ro
  scope: non-axis
  flash: false
  type: array
  array_size: 2
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
---
# RecStop

Command that stops recording on the selected scope.

## Overview

`RecStop` commands the selected scope to stop recording. It can be called at any stage of recording and is the first step when reconfiguring a scope. If recording is ongoing when `RecStop` is called, the [RecDataA/RecDataB](RecDataA-RecDataB.md) metadata is updated to report the actual length of the recording made. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

## How it works

What `RecStop` does depends on the scope's current [RecStat](RecStat.md):

- If the scope is still filling pre-trigger data or waiting for the trigger (status 1 or 2), recording ends with status 6 (stopped before trigger). No usable triggered data set exists, so [RecUpload](RecUpload.md) reports an error for that scope.
- If the trigger has already been detected and recording is in progress (status 3), recording ends with status 5 (stopped). The metadata length in [RecDataA/RecDataB](RecDataA-RecDataB.md) is rewritten to the number of points actually captured so the upload returns only the real data.
- If the scope is idle, already stopped, or already complete, `RecStop` does nothing and is not treated as an error.

## Examples

```text
ARecStop[1]          ; stop recording on the first scope
ARecStop[2]          ; stop recording on the second scope
```

## See also

- [RecStart](RecStart.md) — start recording
- [RecStat](RecStat.md) — recording status
- [RecDataA/RecDataB](RecDataA-RecDataB.md) — metadata updated on stop
