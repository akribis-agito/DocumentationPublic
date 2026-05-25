# VecPause

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

A value of "1" pauses the vector motion by setting the speed to 0 (motion is decelerated till
stopping). A value of "0" continue the motion normally (if paused before, it will accelerate to the
VecSpeed again).

Not Saved to Flash. At power-up gets its default value: "0".
