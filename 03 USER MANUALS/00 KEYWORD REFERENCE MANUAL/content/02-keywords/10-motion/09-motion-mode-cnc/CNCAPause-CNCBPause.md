---
summary: Pauses CNC motion (deceleration to zero vector velocity) when set to 1.
---
# CNCAPause/CNCBPause

Pauses CNC motion (deceleration to zero vector velocity) when set to 1.

## Overview

`CNCAPause` (and its `CNCBPause` counterpart on the second CNC engine) pauses and resumes CNC motion along the path without disturbing the queued segments.

- When set to `1`, the CNC motion decelerates to zero vector velocity.
- When set to `0`, the CNC motion is performed normally. If it was paused, it accelerates back to the desired vector speed of the active segment.

This differs from [StopCNCA](StopCNCA.md), which aborts the motion rather than pausing it.

## Examples

```text
CNCAPause=1         ; pause: decelerate to zero vector velocity
CNCAPause=0         ; resume normal CNC motion
```

## See also

- [StopCNCA](StopCNCA.md) — stop CNC motion on queue A
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — desired vector speed of the active segment
