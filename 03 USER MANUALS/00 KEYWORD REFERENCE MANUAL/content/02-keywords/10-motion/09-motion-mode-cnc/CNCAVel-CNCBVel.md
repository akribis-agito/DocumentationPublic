---
summary: Read-only array reporting the actual resultant path velocity of the CNC group A (or B) members.
---
# CNCAVel/CNCBVel

Read-only array reporting the resultant path velocity of the CNC group A (or B) members.

## Overview

`CNCAVel` (and its `CNCBVel` counterpart) is a read-only array that reports the **actual resultant velocity** of the axes participating in CNC motion on group A (or B), derived from the measured member-axis velocities. It is a non-axis, read-only array that is not saved to flash. Unlike [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — which is the *commanded* path velocity from the profiler — `CNCAVel` is computed from what the member axes are actually doing.

## How it works

Every control cycle the controller forms the resultant (Euclidean) speed of the group from the individual member-axis velocities: it sums the squares of the velocity of each axis that is currently a member of the group and takes the square root. This is the magnitude of the multi-axis velocity vector, i.e. the actual feed rate along the path.

The array reports:

| Index | Meaning |
|----|----|
| 1 | Not used. |
| 2 | Instantaneous resultant velocity — square root of the sum of the squares of the member-axis velocities. |
| 3 | A smoothed resultant velocity — a 32-cycle moving average of index 2. |

Arrays are 1-indexed, so the first valid reading is `CNCAVel[2]`. Use index 2 for the live resultant feed rate and index 3 when a less noisy reading is wanted (for example, for display). Only axes flagged as members of the group ([MotionStat](../05-motion-status/MotionStat.md) bit 10 for group A, bit 13 for group B) contribute to the sum.

The resultant that this array measures is the one driven by the commanded path speed [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) after the on-the-fly scaling factors [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) and [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) are applied.

### CNCB note

`CNCBVel` reports the identical resultant for the independent second CNC group.

## Examples

```text
ACNCAVel[2]         ; instantaneous resultant velocity (arrays are 1-indexed)
ACNCAVel[3]         ; 32-cycle moving-average resultant velocity
```

## See also

- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — commanded path velocity from the profiler
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — commanded path speed of the active segment
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — speed-percentage override
- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active-segment acceleration
