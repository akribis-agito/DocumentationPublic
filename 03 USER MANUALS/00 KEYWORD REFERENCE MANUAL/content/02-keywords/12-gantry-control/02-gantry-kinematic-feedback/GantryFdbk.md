# GantryFdbk

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

The GantryFdbk parameter is a read-only parameter. It provides the MIMO gantry control
feedbacks.

AGantryFdbk is equal to (APos + BPos) / 2.
BGantryFdbk is equal to (APos ­ BPos).

Note that these parameters are calculated even when the Gantry mode is disabled.

Note that the above calculation considers also the GantryOffset, as explained below, although
not written in the above equations, for simplicity.

?GantryFdbk with "?" not equal to "A" or "B" has no use and will always returns a value of 0.
