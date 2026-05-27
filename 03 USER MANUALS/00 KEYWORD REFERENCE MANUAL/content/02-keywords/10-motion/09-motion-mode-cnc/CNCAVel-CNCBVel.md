---
summary: Read-only array reporting the velocity components of the CNC queue A (or B) axes.
---
# CNCAVel/CNCBVel

Read-only array reporting the velocity components of the CNC queue A (or B) axes.

## Overview

`CNCAVel` (and its `CNCBVel` counterpart) is a read-only array that reports the current velocity components of the axes participating in CNC motion queue A (or B). It is a non-axis, read-only array that is not saved to flash.

The overall vector speed that drives these components is set by [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) and scaled by [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md).

## Examples

```text
CNCAVel[1]?         ; read the first axis velocity component (arrays are 1-indexed)
```

## See also

- [CNCASpeedPer/CNCBSpeedPer](CNCASpeedPer-CNCBSpeedPer.md) — speed percentage override
- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active segment acceleration
