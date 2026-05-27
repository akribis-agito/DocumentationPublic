---
summary: Running count of end-of-segment auto-corrections the CNC engine has applied to keep the path continuous.
---
# CNCAEndErrCnt/CNCBEndErrCnt

Counts how many end-of-segment auto-corrections the CNC engine has applied for queue A (or B).

## Overview

`CNCAEndErrCnt` (and its `CNCBEndErrCnt` counterpart on the second CNC engine) is a running count of the times the controller had to auto-correct a discontinuity between consecutive CNC segments on queue A (or B). It rises only when [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) is set to the auto-correct mode (value 1) and the engine forces the previous segment's end speed to 0 to keep the path continuous. It is a non-axis parameter, not saved to flash, and can be changed at any time.

Use it as a quality indicator: a non-zero value means the path the host streamed contained joins that did not match up at the requested speeds, so the controller silently inserted a stop at each of them. A clean, well-formed path leaves this count at 0.

## How it works

- The count starts at 0 and is reset to 0 by [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md).
- Each time a pushed segment breaks the continuous-motion rule **and** [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) = 1, the controller rewrites the previous segment's end speed to 0 and adds 1 to this count. (With `CNCAEndSegMod` = 0 the push is rejected instead and the count does not change.)
- It is therefore a cumulative tally over the life of the current queue, not a per-segment value and not a threshold. You may write it to seed or clear the tally, but normal use is to read it after streaming a path and check whether it is still 0.

## Examples

```text
ACNCAEndErrCnt       ; read how many end-of-segment corrections were applied
ACNCAEndErrCnt=0     ; reset the correction tally before streaming a new path
```

## See also

- [CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md) — selects reject vs. auto-correct (only mode 1 increments this count)
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — end-of-segment speed
- [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md) — resets this count to 0
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
