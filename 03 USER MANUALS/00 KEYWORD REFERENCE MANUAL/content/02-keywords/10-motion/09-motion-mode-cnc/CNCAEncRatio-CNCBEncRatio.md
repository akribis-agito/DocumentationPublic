# CNCAEncRatio/CNCBEncRatio

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics.
     The CNCB counterpart operates the same way on the second CNC engine. -->

This parameter is axis related and it should be separately set for each member axis.

The parameter defines the ratio between the resolutions of an axis to the other axes, to allow
accurate CNC calculations for non-identical physical resolutions of the member axes.

This is a future feature (the controller supports this parameter, but it has no effect on the CNC
calculations).
Currently, the CNC motion calculations assume identical resolution for all member axes.
