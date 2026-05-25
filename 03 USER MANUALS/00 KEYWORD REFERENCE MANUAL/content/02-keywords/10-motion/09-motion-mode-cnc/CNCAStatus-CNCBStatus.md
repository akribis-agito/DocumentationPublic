# CNCAStatus/CNCBStatus

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

A read only array parameter holding the following described status data.

Some of the statuses are not valid after reset or power on, some others are not valid when the
CNC FIFO is empty and some other when there is no CNC FIFO motion and so on. These statuses
get the value -1 when they are not valid (this value is not a valid value for any of these statuses
when they are valid).

Please refer to Motion Modes-CNC for more detailed information.
