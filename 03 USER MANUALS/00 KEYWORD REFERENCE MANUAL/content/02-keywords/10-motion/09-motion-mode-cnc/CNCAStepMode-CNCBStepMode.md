---
summary: Enables CNC step mode, halting at the end of each segment until released.
---
# CNCAStepMode/CNCBStepMode

Enables CNC step mode, halting at the end of each segment until released.

## Overview

`CNCAStepMode` (and its `CNCBStepMode` counterpart on the second CNC engine) enables step-by-step execution of a CNC path, in which the engine performs one queued segment at a time and stops, instead of running the whole path continuously. It is the main tool for dry-running or debugging a part program: you can walk through the path segment by segment, verifying each move before releasing the next one. It applies to the entire CNC engine (not to an individual member axis), is not saved to flash, and can be written at any time, including during motion.

This parameter accepts only two values:

| Value | Meaning |
|----|----|
| 0 (default) | Normal continuous execution — the engine runs segments back to back, blending across segment ends at the configured end speeds. |
| 1 | Step mode — the engine halts at the end of each segment and waits for [CNCADoStep/CNCBDoStep](CNCADoStep-CNCBDoStep.md) = 1 before performing the next one. |

While step mode is active the end speed of every segment is forced to `0`, even if the segment definition specifies a non-zero end speed. Each segment therefore decelerates cleanly to a full stop before the engine waits, so the path is traversed as a series of discrete point-to-point moves rather than a blended trajectory.

## How it works

The CNC engine checks `CNCAStepMode` each control cycle as it processes the queue. When it is `1` and a segment has just finished, the engine refuses to load the next segment until [CNCADoStep/CNCBDoStep](CNCADoStep-CNCBDoStep.md) is set to `1`; once a step is released, exactly one segment is loaded and performed, and the engine halts again at that segment's end. Stepping advances through *every* queued item one at a time — not only the motion segments (lines, arcs) but also the non-motion items in the queue such as dwell/delay segments, parameter-change segments, digital-output writes and array writes.

Because the value is read continuously, you can enter step mode mid-path: set it to `1` and the engine halts at the end of the segment currently being executed. Writing `0` again leaves step mode and lets the engine run the remaining segments freely from that point.

Any command that stops the motion — [StopCNCA](StopCNCA.md) (or `StopCNCB`), a general [Stop](../04-motion-command/Stop.md), or an `Abort` — automatically forces `CNCAStepMode` back to `0`. This guarantees the stop request is honoured immediately; otherwise an engine waiting in step mode would not respond to the request.

While a CNCA path is running, the axes report it through [MotionStat](../05-motion-status/MotionStat.md) (bit 11 / mask `0x800` for CNCA, bit 14 / mask `0x4000` for CNCB).

## Examples

```text
ACNCAStepMode=1      ; halt at the end of each segment (dry-run / debug)
ACNCAStepMode=0      ; resume free, continuous execution of segments
```

## See also

- [CNCADoStep/CNCBDoStep](CNCADoStep-CNCBDoStep.md) — release the next segment while in step mode
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — pause/resume along the path without single-stepping
- [StopCNCA](StopCNCA.md) — stop CNC motion (forces step mode off)
- [MotionStat](../05-motion-status/MotionStat.md) — reports active CNCA/CNCB motion (bits 11 and 14)
