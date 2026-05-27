---
keyword: PDEndTime
summary: Settling-check delay (ms) after PDPos and the position reference stop changing.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 414
attributes:
  access: rw
  scope: axis
  flash: true
  type: scalar
  array_size: 1
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: scaling
  range:
  - 0
  - 163840
  default: 16
  scaling: 1.0
  implemented: final
overrides: {}
---
# PDEndTime

Settling-check delay (ms) after PDPos and the position reference stop changing.

## Overview

`PDEndTime` is the waiting time, in milliseconds, that must elapse after the pulse-direction input and the generated position reference both stop changing, before the controller begins checking the settling status [InTargetStat](../05-motion-status/InTargetStat.md). Because both direct and indirect pulse-and-direction motion stay in the moving state as long as commands keep arriving, this delay prevents premature in-target reporting when a stream of pulses pauses briefly. It applies to both direct ([MotionMode](../02-motion-configuration/MotionMode.md) = 3) and indirect (`MotionMode` = 4) P/D motion.

## How it works

The settling check runs every control cycle during P/D motion:

- When both the P/D delta and the reference derivative are zero, an internal counter increments. Once it reaches `PDEndTime`, in-target checking begins (`InTargetStat` moves from "in motion" to "waiting target time", then evaluates [InTargetTol](../05-motion-status/InTargetTol.md)/`InTargetTime` as usual).
- If *either* the input or the reference moves again, the counter is reset to 0 and `InTargetStat` returns to "in motion".

`PDEndTime` is **stored internally in control samples** but exchanged with the host **in milliseconds**: the keyword has a samples-to-ms scaling (16.384 samples/ms), so reading or writing it uses ms while the comparison counter counts samples. The default internal value is 16 samples (≈ 1 ms); the maximum is 10 s.

## Examples

```text
APDEndTime=1         ; wait ~1 ms of no change before checking settling (default)
APDEndTime=50        ; wait 50 ms of no change
APDEndTime          ; read the current value (ms)
```

## See also

- [InTargetStat](../05-motion-status/InTargetStat.md) — settling status checked after this delay
- [PDPos](PDPos.md) — counter whose changes (via the P/D delta) reset the timer
- [MotionMode](../02-motion-configuration/MotionMode.md) — applies in direct (3) and indirect (4) P/D motion
