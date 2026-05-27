---
summary: Advances CNC step mode to the next segment when set to 1.
---
# CNCADoStep/CNCBDoStep

Advances CNC step mode to the next segment when set to 1.

## Overview

`CNCADoStep` (and its `CNCBDoStep` counterpart on the second CNC engine) releases the next segment while the CNC engine is running in step mode. It is the companion of [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md): when a CNCA path is active and step mode is on (`CNCAStepMode = 1`), the engine halts at the end of each segment, and setting `CNCADoStep = 1` tells it to perform exactly one more segment. It applies to the whole CNC engine (not to an individual member axis), is not saved to flash, and can be written at any time, including during motion.

Outside step mode the value has no effect — the engine runs continuously regardless of `CNCADoStep`. The keyword accepts only `0` and `1`.

## How it works

In step mode the engine consults `CNCADoStep` once it reaches the end of the current segment. If it is `1`, the engine performs the next segment; if it is `0`, the engine simply waits and does nothing further along the path. As soon as the engine acts on the request — which only happens after the current segment has finished — it clears `CNCADoStep` back to `0` automatically. This self-clearing is what makes each write release a *single* segment: the controller cannot run on past one segment because the flag is already back at `0` by the time the next segment end is reached.

When a CNCA path begins (the `Begin` command), `CNCADoStep` is preset according to the step-mode state so the first segment behaves consistently:

- If `CNCAStepMode` is `0`, `CNCADoStep` is cleared to `0`, leaving it ready in case step mode is switched on later during the motion.
- If `CNCAStepMode` is `1`, `CNCADoStep` is set to `1`, so the very first segment is executed before the engine halts and waits for the next release.

## Examples

```text
ACNCADoStep=1        ; release the next segment while in step mode
```

To single-step through a path: set `ACNCAStepMode=1`, start the motion, then write `ACNCADoStep=1` for each segment you want to advance.

## See also

- [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) — enables CNC step mode
- [CNCAPause/CNCBPause](CNCAPause-CNCBPause.md) — pause/resume along the path without single-stepping
- [StopCNCA](StopCNCA.md) — stop CNC motion (forces step mode off)
