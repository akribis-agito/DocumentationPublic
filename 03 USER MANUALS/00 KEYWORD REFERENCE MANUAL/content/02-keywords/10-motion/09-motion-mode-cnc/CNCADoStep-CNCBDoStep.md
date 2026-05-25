# CNCADoStep/CNCBDoStep

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

The value of CNCADoStep can be written at any time, even during motion.

    If CNCA motion is active, and if the CNC is in step mode (CNCAStepMode=1, see above), then
    setting CNCADoStep to 1 will instruct the controller to continue to the next step.

    The value of CNCADoStep has no effect beside the conditional effect as described above.

    Once CNCADoStep is set to 1, and once the controller reacts to this request and move to the next
    segment (only after reaching the end of the current segment), the controller clears CNCADoStep
    to 0, to ensure it will not perform more than a single segment.

    Upon beginning a CNCA motion (using the Begin message), the value of CNCADoStep is
    automatically set as follows:
 If CNCAStepMode is 0, CNCADoStep is cleared to 0 as well (to be ready for activating the step
    mode during the motion).
 If CNCAStepMode is 1, CNCADoStep is set to 1, to ensure the first segment is executed.
