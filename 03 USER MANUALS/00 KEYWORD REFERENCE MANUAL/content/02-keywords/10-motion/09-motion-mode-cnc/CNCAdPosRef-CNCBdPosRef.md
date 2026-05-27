---
summary: Derivative of CNCAPosRef — the current vector velocity of the profiler.
---
# CNCAdPosRef/CNCBdPosRef

Derivative of CNCAPosRef — the current vector velocity of the profiler.

## Overview

`CNCAdPosRef` (and its `CNCBdPosRef` counterpart on the second CNC engine) is the derivative of [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md), meaning the current vector velocity of the profiler along the CNC path.

## Examples

```text
ACNCAdPosRef        ; read the current vector velocity of the profiler
```

## See also

- [CNCAPosRef/CNCBPosRef](CNCAPosRef-CNCBPosRef.md) — desired position along the CNC path
- [CNCAAbsTrgt/CNCBAbsTrgt](CNCAAbsTrgt-CNCBAbsTrgt.md) — segment target distance
