# GantryOffset

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

The GantryOffset is a read-only parameter.

AGantryOffset is calculated once when AGantryOn is switched by the user from 0 to 1.
AGantryOffset = APosRef ­ BPosRef.

The GantryOffset is later used for the calculation of the GantryFdbk readings, so that the initial
offset between the readings of the two encoders is ignored.

The actual calculation is:
AGantryFdbk is equal to (APos + BPos + AGantryOffset) / 2
BGantryFdbk is equal to (APos ­ BPos - AGantryOffset)

?GantryOffset with "?" not equal to "A" has no use and will always returns a value of 0.
