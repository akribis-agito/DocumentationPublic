---
summary: On-the-fly scaling of CNC path speed and acceleration/deceleration.
---
# CNCAPercents/CNCBPercents

On-the-fly scaling of CNC path speed and acceleration/deceleration.

## Overview

`CNCAPercents` (and its `CNCBPercents` counterpart on the second CNC group) scales the CNC path speed **and** its acceleration/deceleration as a percentage. Because it scales the ramps as well as the cruise speed, it effectively rescales the **time** the whole CNC motion takes, while keeping the path geometry and the velocity-profile shape unchanged.

`CNCAPercents` can be modified at any time, including on-the-fly during CNC motion. Choose its value before starting a motion when a specific time scaling is wanted.

## How it works

Each control cycle the controller derives the active path-profile quantities from the programmed segment values and `CNCAPercents` (call its value `P`, in percent):

| Quantity | Scaling applied |
|----|----|
| Path speed ([CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md)) | × `P/100` (also × [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md)/100) |
| Segment-end speed ([CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md)) | × `P/100` |
| Acceleration ([CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md)) and deceleration ([CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md)) | × `(P/100)²` |
| Jerk ([CNCAJerk/CNCBJerk](CNCAJerk-CNCBJerk.md)) | × `(P/100)³` |

Scaling speed by `P/100` and the ramps by the square of `P/100` is exactly what makes the motion duration scale by `100/P` while the profile shape (and therefore the path) is preserved:

- `P = 100` (%) — the motion runs at the values defined in the segment queue.
- `P = 50` (%) — speed is halved and accel/decel are quartered, so the motion takes twice the nominal time.
- `P` greater than 100 (%) is allowed and speeds the motion up.

Because the factor is re-applied every cycle, changing `CNCAPercents` mid-path re-targets the speed and ramps on the next cycle. This is broader than [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md), which scales the speed only and leaves the ramps unchanged. The two multiply together for the net speed factor.

### CNCB note

`CNCBPercents` is the identical scaling for the independent second CNC group.

## Examples

```text
ACNCAPercents=100    ; run at nominal programmed speed and ramps
ACNCAPercents=50     ; half speed, quarter accel/decel — double the time
ACNCBPercents=200    ; group B runs in half the nominal time
```

## See also

- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — commanded path speed
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — speed-percentage override (speed only)
- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) / [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — active-segment ramps that this also scales
