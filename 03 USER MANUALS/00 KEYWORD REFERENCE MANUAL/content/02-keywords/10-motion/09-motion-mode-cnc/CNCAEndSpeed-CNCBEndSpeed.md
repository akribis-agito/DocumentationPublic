---
summary: Reports the commanded speed at the end of the active CNC segment on queue A (or B).
---
# CNCAEndSpeed/CNCBEndSpeed

Reports the commanded speed at the end of the active CNC segment on queue A (or B).

## Overview

`CNCAEndSpeed` (and its `CNCBEndSpeed` counterpart) is a read-only parameter that reports the commanded speed at the end of the currently executing CNC motion segment on queue A (or B). It is a non-axis, read-only parameter that is not saved to flash.

The end-of-segment behaviour that determines how this speed is applied is selected by [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md). Note that when step mode is active ([CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md)) the end speed of each segment is forced to 0.

## Examples

```text
ACNCAEndSpeed       ; read the active segment end speed
```

## See also

- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — current velocity components
- [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) — end-of-segment behaviour
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
