# CNCAJerk/CNCBJerk

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

The parameter defines the Jerk (smoothing) to use when calculating the CNC vector motion
profile. This is a future feature (the controller supports this parameter, but it has no effect on the
CNC calculations).
Currently, the CNC vector motion profiler is calculated without smoothing.
