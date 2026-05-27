---
summary: Speed percentage override applied to CNC motion queue A (or B).
---
# CNCASpeedPer/CNCBSpeedPer

Speed percentage override applied to CNC motion queue A (or B).

## Overview

`CNCASpeedPer` (and its `CNCBSpeedPer` counterpart) sets the speed percentage override applied to CNC motion queue A (or B). Setting it to 100 uses the programmed segment speeds; lower values slow all segments proportionally without reprogramming the FIFO. It is a non-axis parameter, not saved to flash, and can be changed at any time.

It complements [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md), the other on-the-fly speed scaling factor.

## Examples

```text
ACNCASpeedPer=100    ; run at programmed segment speeds
ACNCASpeedPer=50     ; slow all segments to half speed
```

## See also

- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — desired vector speed of the active segment
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — on-the-fly speed/acc scaling
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — current velocity components
