---
summary: On-the-fly scaling of CNC path speed and acceleration/deceleration.
---
# CNCAPercents/CNCBPercents

On-the-fly scaling of CNC path speed and acceleration/deceleration.

## Overview

`CNCAPercents` (and its `CNCBPercents` counterpart on the second CNC engine) is used to scale the CNC speed (and acceleration/deceleration) along the CNC path. By affecting the speed and acceleration/deceleration, `CNCAPercents` effectively scales the time needed to perform the CNC motion.

`CNCAPercents` can be modified at any time, including on-the-fly during the CNC motion. The user needs to consider what value to give to `CNCAPercents` before starting a CNC motion.

## How it works

- A value of `100` (%) means the motion runs according to the values defined in the CNC FIFO segments.
- A value of `50` (%), for example, means the CNC motion is performed in twice the time needed for the nominal CNC motion as defined in the CNC FIFO.
- `CNCAPercents` can take values higher than 100 (%).

## Examples

```text
CNCAPercents=100    ; run at nominal programmed speed
CNCAPercents=50     ; run at half speed (double the time)
```

## See also

- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — desired vector speed of the active segment
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — speed percentage override
