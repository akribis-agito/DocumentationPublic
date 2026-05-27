---
keyword: InTargetTime
summary: Minimum dwell time inside the settling window before target-reached is signalled.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 266
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
  default: null
  scaling: 1.0
  implemented: final
overrides: {}
---
# InTargetTime

Minimum dwell time inside the settling window before target-reached is signalled.

## Overview

`InTargetTime` is the minimum time that the absolute value of the monitored signal — [PosErr](../01-kinematics-status/PosErr.md) or [Vel](../01-kinematics-status/Vel.md) `[1]` — must remain within the settling window ([InTargetTol](InTargetTol.md) or [InTargetVelTh](InTargetVelTh.md)) before [InTargetStat](InTargetStat.md) signals that the target is reached (`InTargetStat = 4`).

## How it works

Internally `InTargetTime` is stored and compared in **controller cycles (samples)**, not milliseconds. The profiler keeps a dwell counter that increments for every consecutive in-window cycle and resets to 0 on any out-of-window cycle; when the counter reaches `glInTargetTime` the target-reached state latches (`AG300_CTL01Profiler.c:968`, current/force mode `:10358`).

When entered from a command the value is scaled by `SAMPLES_TO_MS_FACT = 16.384` (samples per ms at the 16384 Hz sampling rate), so the keyword is supplied in milliseconds:

$$
samples = InTargetTime_{ms} \times 16.384
$$

The raw range is `0`…`SAMPLES_PER_10SECOND = 163840` samples (0 to 10 s). The default `INTARGETTIME_DFLT` is `SAMPLES_PER_SECOND >> 8 = 16384 / 256 = 64` samples ≈ **3.9 ms**. A value of `0` makes the target-reached condition trigger on the first in-window cycle. It is saved to flash and may be changed while in motion.

## Examples

```text
AInTargetTime=100    ; hold the settling window for the configured duration (ms)
AInTargetTime       ; read current value
```

## See also

- [InTargetStat](InTargetStat.md) — settling state this time gates the transition to "reached"
- [InTargetTol](InTargetTol.md) — position settling window
- [InTargetVelTh](InTargetVelTh.md) — velocity settling window
- [MotionSamples](MotionSamples.md) — uses this dwell time in its `[3]` relation
