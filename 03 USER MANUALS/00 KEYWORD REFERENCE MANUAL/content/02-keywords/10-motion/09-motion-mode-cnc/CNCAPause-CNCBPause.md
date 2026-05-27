---
summary: Pauses CNC motion (deceleration to zero vector velocity) when set to 1.
---
# CNCAPause/CNCBPause

Pauses CNC motion (deceleration to zero vector velocity) when set to 1.

## Overview

`CNCAPause` (and its `CNCBPause` counterpart on the second CNC engine) temporarily holds a CNC path without ending the motion or disturbing the queued segments. It is the CNC equivalent of pausing a part program: the tool slows to a stop along its programmed path and then resumes from exactly the same point. It applies to the whole CNC engine (not to an individual member axis), is not saved to flash, and can be written at any time, including during motion.

The keyword accepts only two values:

| Value | Meaning |
|----|----|
| 0 (default) | Run normally. If the path was paused, the engine accelerates back up to the desired vector speed of the active segment and continues along the path. |
| 1 | Pause — the commanded path (vector) speed is forced to zero, so the motion decelerates along its path to a standstill and waits. |

This differs from [StopCNCA](StopCNCA.md), which aborts the motion: a pause leaves the move and its queue intact so it can resume, whereas a stop ends it.

## How it works

The CNC engine reads `CNCAPause` each control cycle while it computes the path profile. While the flag is `1`, the commanded vector speed along the path is held at zero, so the engine ramps down using the active segment's deceleration and the group comes to rest on the path. Internally a pause produces the same zero-speed command as a pending stop request, but it is holdable: when `CNCAPause` returns to `0`, the commanded speed is restored to the desired vector speed of the active segment (after the configured speed factors — see [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) and [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md)) and the engine accelerates back up and carries on. Because the target and the queue are untouched, all member axes continue to their original endpoints when resumed.

Unlike step mode, a pause does not stop at segment boundaries — it halts wherever the path happens to be when the flag is set. The engine does not clear `CNCAPause` on its own: it stays at the value you last wrote, so remember to set it back to `0` to resume. While a CNCA path is active the axes report it through [MotionStat](../05-motion-status/MotionStat.md) (bit 11 / mask `0x800` for CNCA, bit 14 / mask `0x4000` for CNCB).

## Examples

```text
ACNCAPause=1         ; pause: decelerate along the path to zero vector velocity
ACNCAPause=0         ; resume: accelerate back to the active segment's vector speed
```

## See also

- [StopCNCA](StopCNCA.md) — terminate (rather than pause) CNC motion on queue A
- [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) — advance the path one segment at a time
- [CNCASpeed/CNCBSpeed](CNCASpeed-CNCBSpeed.md) — desired vector speed resumed to after a pause
- [CNCAPercents/CNCBPercents](CNCAPercents-CNCBPercents.md) — on-the-fly speed/acceleration scaling
- [MotionStat](../05-motion-status/MotionStat.md) — reports active CNCA/CNCB motion (bits 11 and 14)
