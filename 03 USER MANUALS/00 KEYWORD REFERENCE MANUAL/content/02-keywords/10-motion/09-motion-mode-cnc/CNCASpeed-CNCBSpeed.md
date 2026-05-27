---
summary: Desired vector speed along the CNC path for the active segment.
---
# CNCASpeed/CNCBSpeed

Desired vector speed along the CNC path for the active segment.

## Overview

`CNCASpeed` (and its `CNCBSpeed` counterpart on the second CNC group) is the desired (cruise) speed along the CNC path for the currently active segment, in user units per second. It is the ceiling that the path-velocity profile ramps toward, always treated as a positive magnitude — the travel direction comes from the path geometry, not from a sign.

The speed the controller actually targets is `CNCASpeed` multiplied by two on-the-fly scaling factors: a per-segment speed factor encoded in the segment definition, and the user override applied through [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) and [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md).

## How it works

CNC mode runs one velocity profile along the path. Each control cycle the controller computes the cruise target as:

```text
target path speed = CNCASpeed × (CNCAPercents/100) × (CNCASpeedPer/100) × (segment speed factor/100)
```

and ramps the path velocity [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) toward it:

- While the path velocity is below the target it is raised by the active acceleration ([CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md)) each cycle, clamped to the target.
- It cruises at the target.
- It is forced down by a deceleration-distance lookahead computed from the distance remaining to the segment length [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) and the active deceleration ([CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)), so the path velocity arrives at the segment-end speed [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) exactly at the segment endpoint.

If the segment is too short to reach the target, the profile is triangular and `CNCASpeed` is never attained. If a pause or a stop is requested, the target is forced to zero and the path decelerates.

The controller re-evaluates these factors every cycle, so changing `CNCAPercents` or `CNCASpeedPer` mid-path re-targets the path velocity on the next cycle. The resulting cruise speed is distributed to the member axes by the geometry, so no single member axis necessarily moves at the path speed — only the geometric resultant does (reported by [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) index 2).

### CNCB note

`CNCBSpeed` is the identical mechanism for the independent second CNC group.

## Examples

```text
ACNCASpeed          ; read the desired path speed of the active segment on group A
ACNCBSpeed          ; read it on group B
```

## See also

- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — on-the-fly speed and accel/decel scaling
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — speed-percentage override (speed only)
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — commanded path velocity ramping toward this speed
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — speed at the end of the segment
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — resulting resultant velocity
