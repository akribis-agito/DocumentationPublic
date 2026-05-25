# CNCARemove/CNCBRemove

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

A function keyword to remove the last CNC FIFO A segment.

If the last pushed segment is closed, it will be popped out from the CNC FIFO (removed from the
CNC FIFO) and its ID will be also cancelled (so next pushed segment will get this ID).

If we are in the middle of pushing parameters to a segment, this segment will be cancelled, and
the controller will be ready to get a new segment (which will get the same ID as the deleted
segment, of course).

CNCARemove will return an error if the CNC FIFO A is empty.

CNCARemove will fail and return an error (without removing anything from the CNC FIFO) if the
controller is using this segment for motion at this time.
