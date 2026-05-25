# UsrUnits/AuxUsrUnits

<!-- Imported from the 2021 PDF reference. Verify against current firmware
     behavior and update with the latest semantics. -->

`UsrUnits` allows the user to read the position and its derivatives in units other than encoder counts. `UsrUnits` is the ratio between the desired unit and the encoder counts.

`AuxUsrUnits` is the auxiliary-encoder counterpart and operates the same way on the auxiliary feedback position and its derivatives.

**Example:**

If the user wants to see the position reading in mm, and every 5 encoder counts are equivalent to 1 mm, set `UsrUnits` to 5.

The position reading will now be received in mm, velocity in mm/s, and acceleration in mm/s².
