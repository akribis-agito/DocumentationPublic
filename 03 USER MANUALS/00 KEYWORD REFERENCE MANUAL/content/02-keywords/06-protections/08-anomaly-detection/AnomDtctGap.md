---
keyword: AnomDtctGap
summary: "Number of control cycles each limit-table point spans before the detector advances, set per monitored motion."
availability:
  standalone: []
  central-i:
  - v5
can_code: 796
attributes:
  access: rw
  scope: axis
  flash: true
  type: array
  array_size: 5
  data_type: int32
  ok_in_motion: true
  ok_motor_on: true
  units: none
  range:
  - 1
  - 2147483647
  default: 1
  scaling: 1.0
  implemented: final
overrides: {}
---
# AnomDtctGap

Number of control cycles each limit-table point spans before the detector advances, set per monitored motion.

## Overview

`AnomDtctGap` controls how fast the detector walks through the [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) limit tables during a monitored motion. Each table point covers a fixed number of control cycles; `AnomDtctGap` is that number. A larger gap stretches the same number of table points over a longer motion, so it sets the time resolution of the expected-band profile.

There is one gap value per monitored motion, so a slow motion and a fast motion can use different resolutions.

This keyword is available from v5 (central-i).

## How it works

While a monitored motion is active the detector holds the current limit-table point for `AnomDtctGap` control cycles, then steps to the next point. The comparison of the filtered signal against the band is made once at the start of each gap window. Once the last point of the block is reached the detector holds on that final point until the motion ends.

The array is 1-indexed (index 0 is reserved). Each usable index corresponds to one monitored motion:

| Index | Monitored motion |
| --- | --- |
| 1 | motion 0 |
| 2 | motion 1 |
| 3 | motion 2 |
| 4 | motion 3 |

The minimum value is 1 (advance every control cycle) and the default is 1. With 256 points per motion, the gap multiplied by 256 sets roughly how many control cycles the profile spans; choose it so the table covers the duration of the motion you are monitoring.

## Examples

```text
AAnomDtctGap[1]=10      ; motion 0: hold each limit point for 10 control cycles
AAnomDtctGap[2]=4       ; motion 1: faster motion, finer time resolution
AAnomDtctGap[1]         ; read the gap for motion 0
```

## See also

- [AnomDtctUL](AnomDtctUL.md) / [AnomDtctLL](AnomDtctLL.md) — the limit tables this paces through
- [AnomDtctCnfg](AnomDtctCnfg.md) — monitored source and motion selection
- [AnomDtctSt](AnomDtctSt.md) — active motion and limits
