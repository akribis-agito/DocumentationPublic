---
summary: Reports the commanded speed at the end of the active CNC segment on group A (or B).
---
# CNCAEndSpeed/CNCBEndSpeed

Reports the commanded speed at the end of the active CNC segment on group A (or B).

## Overview

`CNCAEndSpeed` (and its `CNCBEndSpeed` counterpart) is a read-only parameter that reports the path speed the profile is commanded to reach at the **end of the currently active segment** on group A (or B), in user units per second. A non-zero end speed is the corner speed that lets two consecutive segments blend without stopping; a zero end speed brings the path to rest at the segment boundary. It is a non-axis, read-only parameter that is not saved to flash.

## How it works

CNC mode runs a single velocity profile along the path. As the path approaches a segment boundary, the deceleration lookahead (using the distance remaining to [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) and the active deceleration [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)) brakes the path velocity [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) so that it equals `CNCAEndSpeed` exactly at the boundary. This is the look-ahead/cornering mechanism: if the next segment can be entered at that speed, the path carries the velocity straight through the corner; any path fraction not consumed at the boundary is passed into the next segment so motion stays continuous.

The reported value is the segment's programmed end speed after the on-the-fly scaling factors are applied (the same speed factors that scale [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md): [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) and [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md)), so the corner speed tracks any feed-rate override.

The controller forces `CNCAEndSpeed` to **0** in cases where the path must come to rest at the segment end:

- on the last segment in the queue (so the path stops cleanly when the queue empties);
- when a stop of the group has been requested;
- when step mode ([CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md)) is active, so each stepped segment ends at zero speed.

The end-of-segment transition (blend versus stop) is selected by [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md).

![CNC segment chain showing two cornering blends and a final stop driven by CNCAEndSpeed](cnc-endspeed.svg)

### CNCB note

`CNCBEndSpeed` reports the identical quantity for the independent second CNC group.

## Examples

```text
ACNCAEndSpeed       ; read the active-segment end speed on group A
ACNCBEndSpeed       ; read it on group B
```

## See also

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — deceleration whose lookahead targets this end speed
- [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) — end-of-segment blend/stop behaviour
- [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) — step mode forces end speed to 0
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — path velocity ramped toward this end speed
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — resulting resultant velocity
