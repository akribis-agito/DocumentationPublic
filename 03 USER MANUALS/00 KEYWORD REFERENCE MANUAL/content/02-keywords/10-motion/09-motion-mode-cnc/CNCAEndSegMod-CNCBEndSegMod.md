---
summary: Selects the end-of-segment behaviour for CNC motion queue A (or B).
---
# CNCAEndSegMod/CNCBEndSegMod

Selects how the controller handles a discontinuity between consecutive CNC segments for queue A (or B).

## Overview

`CNCAEndSegMod` (and its `CNCBEndSegMod` counterpart on the second CNC engine) chooses what the controller does when a newly pushed segment would break the **continuous-motion** rule — that is, when the previous segment ends at a non-zero speed but the new segment cannot continue smoothly from it. It is a non-axis parameter, saved to flash, and can be changed at any time.

The related end-of-segment speed is reported by [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md), and the number of times this mode has had to apply a correction is counted by [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md).

## How it works

When a segment is pushed, the controller checks whether it can run continuously from the previous one. Continuity is broken when the previous segment's end speed is non-zero **and** either:

- the new segment is a non-motion / motion-blocking segment (such as a delay, an I/O write, or a wait), or
- the new segment is a motion segment whose involved axes differ from the previous segment's.

`CNCAEndSegMod` decides the response to such a discontinuity:

| Value | Behaviour on a discontinuity |
|----|----|
| 0 | **Reject.** The push is refused and an error is returned. The host must supply segments that already join up at the speeds it requested. |
| 1 | **Auto-correct.** The push is accepted; the controller rewrites the previous segment's end speed to 0 so the path comes cleanly to rest before the new segment, and increments the correction counter [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) by 1. |

When there is no discontinuity, `CNCAEndSegMod` has no effect — the segment is queued as pushed and the requested end speed is preserved.

## Examples

```text
ACNCAEndSegMod=0     ; reject any segment that breaks continuous motion
ACNCAEndSegMod=1     ; auto-correct: force the previous end speed to 0 and count it
```

## See also

- [CNCAEndErrCnt/CNCBEndErrCnt](CNCAEndErrCnt-CNCBEndErrCnt.md) — count of auto-corrections applied
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — end-of-segment speed
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment (where the check is made)
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
