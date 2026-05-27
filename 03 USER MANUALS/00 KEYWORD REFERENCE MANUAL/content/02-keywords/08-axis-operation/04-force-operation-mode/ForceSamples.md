---
keyword: ForceSamples
summary: Timings of the last completed ForceCmdVal application, in controller cycles.
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 736
attributes:
  access: ro
  scope: axis
  flash: false
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - -1
  - 2147483647
  default: -1
  scaling: 1.0
  implemented: final
overrides: {}
---
# ForceSamples

Timings of the last completed ForceCmdVal application, in controller cycles.

## Overview

`ForceSamples` reports the timings of the last completed [ForceCmdVal](ForceCmdVal.md) application, the force-mode counterpart of [MotionSamples](../../10-motion/05-motion-status/MotionSamples.md). It is applicable only when [ForceCmdSrc](ForceCmdSrc.md) = 1 or 2. The unit is the number of controller cycles, where one cycle is the sample period $T_{s} = \frac{1}{16384\ \text{Hz}} \approx 61.035\ \mu s$. The four timings are recorded together the moment [ForceInTStat](ForceInTStat.md) reaches 4 (settled), using an internal cycle counter and the dwell time [ForceInTTime](ForceInTTime.md).

Each element is initialized to `-1` when the motor is disabled, so `-1` means "no completed application yet". The array uses indices 1 to 4 (index 0 is unused).

## How it works

Each array element represents a different elapsed time, measured from the start of the new target-force application (when the index advanced to this entry):

| Index | Descriptions |
|----|----|
| 1 | Time for the raw force reference to reach the target value (ForceCmdVal) from its initial value — the ramp / "move" time. |
| 2 | Time until `ForceErr` **first enters** the ForceInTTol window (and stays long enough to ultimately settle) — "move and settle" time. |
| 3 | Time until `ForceErr` is **declared settled** (inside ForceInTTol for at least ForceInTTime) — "move, settle and in-target" time. |
| 4 | Time from the raw reference reaching the target until `ForceErr` first enters the ForceInTTol window — the "settle" time alone. |

In summary:

$$
ForceSamples\lbrack 2\rbrack = \ ForceSamples\lbrack 1\rbrack + \ ForceSamples\lbrack 4\rbrack
$$

$$
ForceSamples\lbrack 3\rbrack = \ ForceSamples\lbrack 2\rbrack + \ ForceInTTime
$$

(`ForceInTTime` is expressed in the same controller-cycle units as the samples.)

## Examples

```text
AForceSamples[1]    ; move time, in controller cycles
AForceSamples[3]    ; move + settle + in-target time
```

## See also

- [ForceInTStat](ForceInTStat.md) — in-target status (samples recorded when it reaches 4)
- [ForceInTTol](ForceInTTol.md) — settling window
- [ForceInTTime](ForceInTTime.md) — required dwell time within the window
- [MotionSamples](../../10-motion/05-motion-status/MotionSamples.md) — equivalent timings for position/velocity moves
