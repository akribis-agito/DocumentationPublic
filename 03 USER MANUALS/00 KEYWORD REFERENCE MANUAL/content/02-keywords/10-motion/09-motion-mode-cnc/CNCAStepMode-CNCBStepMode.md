---
summary: Enables CNC step mode, halting at the end of each segment until released.
---
# CNCAStepMode/CNCBStepMode

Enables CNC step mode, halting at the end of each segment until released.

## Overview

`CNCAStepMode` (and its `CNCBStepMode` counterpart on the second CNC engine) enables step-by-step execution of the CNC segments. The value can be written at any time, even during motion.

- When `0`, the CNC motion acts normally (no step mode).
- When `1`, the CNC engine halts at the end of each segment and waits for [CNCADoStep/CNCBDoStep](CNCADoStep-CNCBDoStep.md)`=1` to perform the next segment (and halts again at the end of that segment).

When step mode is active, the end speed of each segment is forced to 0, even if a different value is defined as part of the segment definition.

## How it works

Any user command to stop the motion (`StopCNCA`, `Stop`, and `Abort`) forces the `CNCAStepMode` parameter to 0.

`CNCAStepMode` can be modified while the controller is in motion, so the user can enter step mode at any time (the controller halts at the end of the currently executed segment) by setting this parameter to 1. Conversely, the user can leave step mode and let the controller freely execute the remaining segments by writing 0 to this parameter.

## Examples

```text
CNCAStepMode=1      ; halt at the end of each segment
CNCAStepMode=0      ; resume free execution of segments
```

## See also

- [CNCADoStep/CNCBDoStep](CNCADoStep-CNCBDoStep.md) — release the next segment in step mode
- [StopCNCA](StopCNCA.md) — stop CNC motion (forces step mode off)
