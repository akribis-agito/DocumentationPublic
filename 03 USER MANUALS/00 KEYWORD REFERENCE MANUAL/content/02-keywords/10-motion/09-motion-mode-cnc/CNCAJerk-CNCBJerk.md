---
summary: Jerk (smoothing) for the CNC vector motion profile (future feature, no current effect).
---
# CNCAJerk/CNCBJerk

Jerk (smoothing) for the CNC path-velocity profile (future feature, no current effect).

## Overview

`CNCAJerk` (and its `CNCBJerk` counterpart on the second CNC group) is intended to set the jerk (the rate of change of acceleration) used to smooth the CNC path-velocity profile, in user units per second cubed. Lower jerk would round the corners of the velocity ramps for gentler S-curve motion.

> **Documentation pending:** This is a future feature. The controller accepts and stores the value, but it currently has no effect on the CNC path calculations: the path-velocity profile is generated with trapezoidal (linear) acceleration and deceleration ramps, without jerk smoothing.

## How it works

The CNC path-velocity profile is presently built from the commanded path speed [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) and the linear ramps [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) and [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md), with no jerk limit applied. When jerk smoothing becomes active in a future release, the value would be scaled on-the-fly by the cube of the time-scaling factor [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) (`CNCAJerk × (CNCAPercents/100)³`), consistent with how speed scales by the first power and the accel/decel ramps by the square — keeping the profile shape, and hence the path, unchanged as the motion time is rescaled.

### CNCB note

`CNCBJerk` is the identical (currently inactive) parameter for the independent second CNC group.

## Examples

```text
ACNCAJerk           ; read the configured jerk value on group A
ACNCBJerk           ; read it on group B
```

## See also

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active-segment acceleration
- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — active-segment deceleration
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — on-the-fly time scaling
