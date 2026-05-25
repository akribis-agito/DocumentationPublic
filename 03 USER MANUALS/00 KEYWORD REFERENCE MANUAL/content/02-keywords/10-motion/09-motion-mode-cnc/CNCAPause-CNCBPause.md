# CNCAPause/CNCBPause

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

When set to "1", the CNC motion decelerate to zero vector velocity.
When set to "0", the CNC motion is performed normally. If it was paused, it accelerates back to
the desired vector speed of the active segment.
