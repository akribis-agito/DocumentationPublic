---
keyword: ScheduleGains
availability:
  standalone:
  - v4
  central-i:
  - v4
  - v5
can_code: 274
attributes:
  access: ro
  scope: axis
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
overrides:
  central-i.v5:
    array_size: 7
    data_type: float32
    range: null
---
# ScheduleGains

Read-only array reporting the tuning gains the control loops are using right now, after gain scheduling has selected the active set.

## Overview

`ScheduleGains` is the live readout of the scheduled gains in effect for the axis. Each array element holds one gain. When gain scheduling switches sets — or, in interpolated modes, blends between sets — these are the values that result and that the loops actually apply.

| Index | Gain |
|---|---|
| 1 | Position-loop proportional gain |
| 2 | Acceleration feedforward gain |
| 3 | Velocity-loop proportional gain |
| 4 | Velocity-loop integral gain |
| 5 | Velocity feedforward gain |
| 6 | Position-loop integral gain (central-i v5 only) |

Index 6 (the position-loop integral gain) exists only on central-i v5, where [PosKi](../03-position-control/PosKi.md) is available and schedulable. On v4 only indices 1–5 are reported.

## How it works

Each control cycle, the controller determines the active set number ([ScheduleSet](ScheduleSet.md)) from the rule chosen by [ScheduleMode](ScheduleMode.md), then loads `ScheduleGains` from that set:

- In the stepped modes, the six elements are copied from the corresponding gain arrays at the active set index — for example `ScheduleGains[2]` = [AccFFW](../05-feedforwards/AccFFW.md)`[set]`.
- In the interpolated modes (velocity or position range), each element is computed by linear interpolation between the two sets that bound the current measurement, so the reported values move continuously rather than in steps.
- When the axis is using gantry-paired scheduling, the gains are taken from the gantry tuning arrays instead of the standard ones (see [ScheduleGntry](ScheduleGntry.md)).

With no scheduling (`ScheduleMode = 0`), the active set is always 1, so each `ScheduleGains` element equals the first element of its corresponding gain keyword — for example `ScheduleGains[2]` = `AccFFW[1]`, `ScheduleGains[1]` = `PosGain[1]`.

## Examples

```text
AScheduleGains[3]      ; read the velocity-loop proportional gain currently applied
AScheduleGains[1]      ; read the position-loop proportional gain currently applied
```

### Worked example: confirming the active scheduling set

With velocity-band scheduling (`ScheduleMode = 4`) and `PosGain[1..3] = 400, 400, 250` configured, suppose the axis is stationary so [ScheduleSet](ScheduleSet.md) reads `1`. Then `ScheduleGains[1]` reads `400` (= `PosGain[1]`). After commanding a fast move that puts the speed into the third velocity band, `ScheduleSet` reads `3` and `ScheduleGains[1]` reads `250` (= `PosGain[3]`). The change in `ScheduleGains` confirms that the controller has actually switched the running gain, not merely the set number.

## See also

- [ScheduleSet](ScheduleSet.md) — active gain-set number that selects these values
- [ScheduleMode](ScheduleMode.md) — rule that drives the selection
- [PosGain](../03-position-control/PosGain.md) / [PosKi](../03-position-control/PosKi.md) / [VelGain](../04-velocity-control/VelGain.md) / [VelKi](../04-velocity-control/VelKi.md) / [VelFFW](../05-feedforwards/VelFFW.md) / [AccFFW](../05-feedforwards/AccFFW.md) — the source gain arrays
