---
summary: Maximum allowed position error count at the end of a CNC segment before a fault.
---
# CNCAEndErrCnt/CNCBEndErrCnt

Maximum allowed position error count at the end of a CNC segment before a fault.

## Overview

`CNCAEndErrCnt` (and its `CNCBEndErrCnt` counterpart) sets the maximum allowed position error count at the end of a CNC motion segment before a fault is generated. If the axis position error exceeds this threshold when a segment completes, the controller flags an end-of-segment error. It is a non-axis parameter, not saved to flash, and can be changed at any time.

It works with [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md), which selects the end-of-segment behaviour.

## Examples

```text
CNCAEndErrCnt=1000  ; max end-of-segment position error before fault
```

## See also

- [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) — end-of-segment behaviour
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
