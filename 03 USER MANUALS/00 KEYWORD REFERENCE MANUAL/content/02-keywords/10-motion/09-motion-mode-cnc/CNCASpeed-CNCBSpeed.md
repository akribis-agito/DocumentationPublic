# CNCASpeed/CNCBSpeed

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

CNCASpeed represent the desired vector speed along the CNC path, for the currently active
segment. However, the actual vector speed is this value multiplied by speed factor defined as
part of the CNC FIFO definition and by a second factor defined on-the-fly by the user
(CNCAPercents keyword).
