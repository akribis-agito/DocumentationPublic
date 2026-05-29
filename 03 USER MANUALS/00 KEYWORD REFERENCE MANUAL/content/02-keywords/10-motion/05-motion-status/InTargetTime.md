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
  scaling: 65.536
  implemented: final
overrides: {}
---
# InTargetTime

Minimum dwell time inside the settling window before target-reached is signalled.

## Overview

`InTargetTime` is the minimum time that the absolute value of the monitored signal — [PosErr](../01-kinematics-status/PosErr.md) or [Vel](../01-kinematics-status/Vel.md) `[1]` — must remain within the settling window ([InTargetTol](InTargetTol.md) or [InTargetVelTh](InTargetVelTh.md)) before [InTargetStat](InTargetStat.md) signals that the target is reached (`InTargetStat = 4`).

## How it works

Internally `InTargetTime` is stored and compared in **controller cycles (samples)**, not milliseconds. The controller keeps a dwell counter that increments for every consecutive in-window cycle and resets to 0 on any out-of-window cycle; when the counter reaches the configured time the target-reached state latches (in both position/velocity and current/force modes).

When entered from a command the value is scaled by `16.384` (samples per ms at the 16384 Hz sampling rate), so the keyword is supplied in milliseconds:

$$
\text{samples} = \text{InTargetTime}_{\text{ms}} \cdot 16.384
$$

The raw range is `0`…`163840` samples (0 to 10 s). The default is `16384 / 256 = 64` samples ≈ **3.9 ms**. A value of `0` makes the target-reached condition trigger on the first in-window cycle. It is saved to flash and may be changed while in motion.

## Examples

```text
AInTargetTime=100    ; hold the settling window for the configured duration (ms)
AInTargetTime       ; read current value
```

### Edge cases

- **Motor off:** value is held; the state machine is at `0` so it is not consulted.
- **Out-of-range write:** the parameter system clamps to the scaled `0`–`10 s` range; negative values are rejected.
- **Simulation mode (`MotorType` = 5):** unchanged; `PosErr` is zero so the dwell counter starts incrementing from the first cycle.
- **ModRev wrap:** unrelated.
- **Active fault:** axis disabled; the dwell counter is reset.
- **Other motion modes:** the dwell applies in any mode (the state machine runs regardless of motion mode).
- **`InTargetTime = 0`:** the target-reached state latches on the very first in-window cycle; useful for very fast point-to-point work where settling is not the bottleneck.
- **Live change in motion:** allowed; the new value takes effect for subsequent settling decisions but does not reset the in-progress counter.

## See also

- [InTargetStat](InTargetStat.md) — settling state this time gates the transition to "reached"
- [InTargetTol](InTargetTol.md) — position settling window
- [InTargetVelTh](InTargetVelTh.md) — velocity settling window
- [MotionSamples](MotionSamples.md) — uses this dwell time in its `[3]` relation
- [PosErr](../01-kinematics-status/PosErr.md) — the signal whose dwell inside the window is counted (position/velocity modes)
