---
summary: Selects the end-of-segment behaviour for CNC motion queue A (or B).
---
# CNCAEndSegMod/CNCBEndSegMod

Selects the end-of-segment behaviour for CNC motion queue A (or B).

## Overview

`CNCAEndSegMod` (and its `CNCBEndSegMod` counterpart) selects the end-of-segment behaviour for CNC motion queue A (or B), controlling how the controller handles the transition between consecutive CNC segments (for example, blending versus stopping). It is a non-axis parameter saved to flash and can be changed at any time.

The end-of-segment speed it governs is reported by [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md), and the allowed end position error is set by [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md).

## Examples

```text
ACNCAEndSegMod=0     ; select end-of-segment transition mode
```

## See also

- [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) — end-of-segment position error limit
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — end-of-segment speed
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
