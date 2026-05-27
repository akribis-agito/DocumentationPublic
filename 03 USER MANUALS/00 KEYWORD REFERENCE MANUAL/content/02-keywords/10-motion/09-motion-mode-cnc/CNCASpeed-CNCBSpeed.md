---
summary: Desired vector speed along the CNC path for the active segment.
---
# CNCASpeed/CNCBSpeed

Desired vector speed along the CNC path for the active segment.

## Overview

`CNCASpeed` (and its `CNCBSpeed` counterpart on the second CNC engine) represents the desired vector speed along the CNC path for the currently active segment. The actual vector speed is this value multiplied by a speed factor defined as part of the CNC FIFO segment definition, and by a second factor defined on-the-fly by the user via [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md).

## Examples

```text
CNCASpeed?          ; read the desired vector speed of the active segment
```

## See also

- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — on-the-fly speed/acc scaling
- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — speed percentage override
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — current velocity components
