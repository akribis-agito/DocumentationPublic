---
summary: Reports the jerk (smoothing) of the active CNC segment's path-velocity profile on group A (or B).
---
# CNCAJerk/CNCBJerk

Reports the jerk (smoothing) of the active CNC segment's path-velocity profile on group A (or B).

## Overview

`CNCAJerk` (and its `CNCBJerk` counterpart on the second CNC group) is a read-only parameter that reports the jerk (the rate of change of acceleration) of the path-velocity profile for the currently active CNC segment, in user units per second cubed. Jerk rounds the corners of the velocity ramps so the path follows a smoother S-curve instead of abrupt changes of acceleration. It reflects the jerk encoded in the segment that was pushed to the queue. It is a non-axis, read-only parameter that is not saved to flash.

## How it works

The CNC path-velocity profile is built from the commanded path speed [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md), the ramps [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) and [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md), and this jerk limit:

- When the active segment's jerk is **10 or greater**, the profiler applies a true jerk limit, producing S-curve acceleration and deceleration phases.
- When it is **0 to 9**, the segment runs in a backward-compatible mode with trapezoidal (linear) acceleration and deceleration ramps and no jerk smoothing.

The jerk is scaled on-the-fly by the cube of the time-scaling factor [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) (`CNCAJerk × (CNCAPercents/100)³`), consistent with how the commanded speed scales by the first power and the accel/decel ramps by the square — keeping the profile shape, and hence the path, unchanged as the motion time is rescaled.

### CNCB note

`CNCBJerk` reports the identical quantity for the independent second CNC group.

## Examples

```text
ACNCAJerk           ; read the active-segment jerk value on group A
ACNCBJerk           ; read it on group B
```

## See also

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active-segment acceleration
- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — active-segment deceleration
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — commanded path speed
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — on-the-fly time scaling (scales jerk by the cube of its factor)
