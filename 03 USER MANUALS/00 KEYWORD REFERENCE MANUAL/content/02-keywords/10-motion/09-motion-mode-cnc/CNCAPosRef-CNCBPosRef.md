---
summary: Current desired position along the CNC path for the active segment.
---
# CNCAPosRef/CNCBPosRef

Current desired position along the CNC path for the active segment.

## Overview

`CNCAPosRef` (and its `CNCBPosRef` counterpart on the second CNC group) is the running position reference of the CNC motion along the path, in user units. It starts from zero at the beginning of the active segment and climbs to [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) at the end of that segment. Its per-cycle change (the path velocity) is reported by [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md).

`CNCAPosRef` is the single master coordinate that drives every member axis of the group, which is what keeps the axes exactly coordinated on the path.

## How it works

CNC mode runs **one** velocity profile along the path rather than a separate profile per axis. Each control cycle the controller advances a scalar path velocity (shaped by [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md), [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md), [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)) and accumulates it into `CNCAPosRef`. That one number climbs from 0 toward the active-segment length, and every member axis is then derived from it:

- **Linear segment** — for each member axis the controller multiplies `CNCAPosRef` by that axis's direction cosine (its share of the straight-line displacement: per-axis travel divided by the segment length) and adds the axis start position. All axes therefore trace the straight line together.
- **Arc segment** — `CNCAPosRef` divided by the radius gives the angle swept from the start angle (in the programmed direction); the two member-axis positions are the center coordinate plus radius times cosine / sine of that angle.

The accumulation is carried internally at higher precision than user units (a fixed-point value scaled by `2^14`) so that fractional path motion builds up without drift; `CNCAPosRef` is reported by scaling that accumulator back to user units. The 14-bit fraction is also used when splitting the path position across axes, so the axes stay sub-count accurate on the path. An optional path-position smoothing filter (see [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md)) can be applied to the reference before it is distributed to the axes.

When a segment finishes, any leftover fractional path distance is carried into the next segment so the path remains continuous through a blended corner; on the final segment (or when a stop is requested) the path is driven exactly to the endpoint and the member axes are snapped to their resolved end positions. While the group is active, [MotionStat](../05-motion-status/MotionStat.md) bit 11 (group A) or bit 14 (group B) is set on each member axis.

### CNCB note

`CNCBPosRef` is the identical mechanism on the independent second CNC group, with its own path accumulator and member axes.

## Examples

```text
ACNCAPosRef         ; read the current path position on group A
ACNCBPosRef         ; read the current path position on group B
```

## See also

- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — active-segment length (end value of `CNCAPosRef`)
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — per-cycle change of `CNCAPosRef` (path velocity)
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — actual resultant velocity measured from the member axes
- [MotionStat](../05-motion-status/MotionStat.md) — CNCA membership/active bits 10-12, CNCB bits 13-15
