---
summary: Reports the acceleration of the active CNC segment on group A (or B).
---
# CNCAAccel/CNCBAccel

Reports the acceleration of the active CNC segment on group A (or B).

## Overview

`CNCAAccel` (and its `CNCBAccel` counterpart) is a read-only parameter that reports the acceleration of the path-velocity profile for the currently active CNC segment on group A (or B), in user units per second squared. It reflects the acceleration encoded in the segment that was pushed to the queue. It is a non-axis, read-only parameter that is not saved to flash.

## How it works

CNC mode runs a single velocity profile along the path. While the path velocity [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) is below the commanded cruise speed [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md), the controller raises it by `CNCAAccel × (control-cycle time)` each cycle until it reaches cruise. `CNCAAccel` is the rate used for that rising ramp; it is applied to the **path** (resultant) velocity, not to any individual member axis — the geometry then distributes the resulting acceleration across the member axes.

The effective acceleration used each cycle is the reported segment value scaled by the square of the on-the-fly time-scaling factor [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md): effective accel = `CNCAAccel × (CNCAPercents/100)²`. Scaling the ramps by the square of the speed factor is what keeps the velocity-profile shape (and therefore the path) unchanged while [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) rescales the motion time. The speed-only override [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) does **not** scale acceleration.

It pairs with [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md), the braking rate. The underlying segment data is supplied through [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) and held in [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md).

### CNCB note

`CNCBAccel` reports the identical quantity for the independent second CNC group.

## Examples

```text
ACNCAAccel          ; read the active-segment acceleration on group A
ACNCBAccel          ; read it on group B
```

## See also

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — active-segment deceleration
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — cruise speed this ramps toward
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — scales acceleration by the square of its factor
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
