# VecArcCenter

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

For ARC vector, defines the location of the arc center, so the controller can calculate the radius.
The VecArcCenter, like all other new keywords for the vector motion, is per axis. So, the
coordinate of the arc center are defined by the VecArcCenter of the two member axes.
Saved to Flash. Can't be modified while in motion.
