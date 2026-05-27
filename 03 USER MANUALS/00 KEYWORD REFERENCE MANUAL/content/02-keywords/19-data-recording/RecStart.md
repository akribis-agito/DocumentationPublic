---
keyword: RecStart
summary: Command that starts recording on the selected scope.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
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

## How it works

`RecStart` validates the configuration, then takes a one-time snapshot of all settings into the recording's metadata so that later edits to the setup keywords do not affect the run in progress. As part of this it:

- Rejects the start if the scope is already recording, if [RecLength](RecLength.md) or [RecGap](RecGap.md) is not positive, if [RecTrigPos](RecTrigPos.md) is outside 0–100, or if a trigger type is invalid or has a zero mask.
- Walks [RecParamA/RecParamB](RecParamA-RecParamB.md) to count and resolve the channels, rejecting unknown codes, commands, and bad axis/index references, and rejecting the start if channels × `RecLength` exceeds the buffer.
- Records each channel's data type and user-unit scaling, converts the trigger thresholds into internal units, and seeds the previous/initial trigger-source values used to detect edges and changes.
- Computes how many points fall before the trigger (from `RecTrigPos`) and how many must follow it, then clears the buffer indices and counters.

It then arms the scope by setting [RecStat](RecStat.md) to 1 (filling pre-trigger). If no trigger is configured (the first trigger type is "none"), the scope skips straight to status 3 (trigger detected) and records the full requested length immediately.

## Examples

```text
ARecStart[1]         ; start recording on the first scope
ARecStart[2]         ; start recording on the second scope
```

## See also

- [RecStat](RecStat.md) — recording status
- [RecStop](RecStop.md) — stop recording
- [RecTrigForce](RecTrigForce.md) — force the trigger
- [RecParamA/RecParamB](RecParamA-RecParamB.md) — parameters to capture
