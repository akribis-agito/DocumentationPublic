# CNCAStepMode/CNCBStepMode

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

The value of CNCAStepMode can be written at any time, even during motion.

When 0, the CNC motion will act normally (no step mode).

When 1, the CNC engine will halt at the end of each segment and will wait for CNCADoStep = 1
(see below) to perform the next segment (and halt again at the end of that segment).

The End Speed of each segment is forced to 0, even if a different value is defined as part of the
segment definition.

Any user command to stop the motion (StopCNCA, Stop, and Abort) will force CNCAStepMode
parameter to 0.

Note that CNCAStepMode can be modified while the controller is in motion. So, user can enter
the step mode at any time (the controller will halt at the end of the currently executed segment)
by setting this parameter to 1. On the other hand, user can leave the step mode and the
controller will continue to freely execute the NC segments by writing 0 to this parameter.
