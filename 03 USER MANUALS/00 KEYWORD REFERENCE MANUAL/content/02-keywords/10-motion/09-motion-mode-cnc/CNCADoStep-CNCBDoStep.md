---
summary: Advances CNC step mode to the next segment when set to 1.
---
# CNCADoStep/CNCBDoStep

Advances CNC step mode to the next segment when set to 1.

## Overview

`CNCADoStep` (and its `CNCBDoStep` counterpart on the second CNC engine) advances the motion to the next segment while running in step mode. It works together with [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md): if CNCA motion is active and the CNC is in step mode (`CNCAStepMode=1`), setting `CNCADoStep` to 1 instructs the controller to continue to the next step. The value of `CNCADoStep` has no effect outside of this conditional behaviour.

The value can be written at any time, even during motion.

## How it works

Once `CNCADoStep` is set to 1, and once the controller reacts to the request and moves to the next segment (only after reaching the end of the current segment), the controller clears `CNCADoStep` back to 0, to ensure it does not perform more than a single segment.

Upon beginning a CNCA motion (using the `Begin` message), the value of `CNCADoStep` is automatically set as follows:

- If `CNCAStepMode` is 0, `CNCADoStep` is cleared to 0 as well (so it is ready for activating step mode during the motion).
- If `CNCAStepMode` is 1, `CNCADoStep` is set to 1, to ensure the first segment is executed.

## Examples

```text
CNCADoStep=1        ; release the next segment while in step mode
```

## See also

- [CNCAStepMode/CNCBStepMode](CNCAStepMode-CNCBStepMode.md) — enables CNC step mode
- [StopCNCA](StopCNCA.md) — stop CNC motion (forces step mode off)
