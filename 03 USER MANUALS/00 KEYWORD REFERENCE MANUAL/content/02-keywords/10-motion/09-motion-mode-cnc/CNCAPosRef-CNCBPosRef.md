---
summary: Current desired position along the CNC path for the active segment.
---
# CNCAPosRef/CNCBPosRef

Current desired position along the CNC path for the active segment.

## Overview

`CNCAPosRef` (and its `CNCBPosRef` counterpart on the second CNC engine) is the current desired position along the CNC path. It starts from zero and reaches [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) at the end of the segment.

Its derivative, the current vector velocity of the profiler, is reported by [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md).

## Examples

```text
ACNCAPosRef         ; read the current desired position along the path
```

## See also

- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — segment target distance
- [CNCAdPosRef/CNCBdPosRef](CNCAdPosRef-CNCBdPosRef.md) — derivative (vector velocity)
