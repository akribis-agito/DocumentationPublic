---
summary: Distance to move along the CNC path for the currently active segment.
---
# CNCAAbsTrgt/CNCBAbsTrgt

Distance to move along the CNC path for the currently active segment.

## Overview

`CNCAAbsTrgt` (and its `CNCBAbsTrgt` counterpart on the second CNC engine) is the distance to move, for the currently active segment, along the CNC path. The position reference [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) advances from zero at the start of the segment up to `CNCAAbsTrgt` at the end of the segment.

## Examples

```text
CNCAAbsTrgt?        ; query the target distance of the active segment
```

## See also

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — desired position along the CNC path
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — derivative of the position reference (vector velocity)
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
