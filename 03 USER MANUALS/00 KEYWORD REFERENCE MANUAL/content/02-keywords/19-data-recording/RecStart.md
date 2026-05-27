---
keyword: RecStart
summary: Command that starts recording on the selected scope.
availability:
  standalone:
  - v4
  central-i:
  - v4
can_code: 248
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
# RecStart

Command that starts recording on the selected scope.

## Overview

`RecStart` commands the selected scope to start recording, according to the configured setup and trigger keywords. Once recording is started, changing the setup or trigger keywords ([RecParamA/RecParamB](RecParamA-RecParamB.md), [RecGap](RecGap.md), [RecLength](RecLength.md), and the trigger keywords) will not affect the recording in progress. Each array index selects a scope.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

After starting, monitor progress with [RecStat](RecStat.md) and, if needed, force the trigger with [RecTrigForce](RecTrigForce.md) or abort with [RecStop](RecStop.md).

## Examples

```text
RecStart[1]         ; start recording on the first scope
RecStart[2]         ; start recording on the second scope
```

## See also

- [RecStat](RecStat.md) — recording status
- [RecStop](RecStop.md) — stop recording
- [RecTrigForce](RecTrigForce.md) — force the trigger
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — parameters to capture
