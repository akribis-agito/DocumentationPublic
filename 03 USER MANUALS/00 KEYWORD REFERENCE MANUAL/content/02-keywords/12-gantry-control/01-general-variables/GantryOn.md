# GantryOn

<!-- Imported from the 2021 PDF reference. Verify against current
     firmware behavior and update with the latest semantics. -->

AGantryOn control the operation of the gantry mode. With AGantryOn=0, the gantry mode is
disabled and each axis can be moved and controlled independently. With AGantryOn=1, the
gantry mode is enabled and the control scheme is automatically changed to gantry MIMO
control.

When Gantry is on, motions to the gantry stage is done by commanding motions to the A axis.

Note that ?GantryOn, with "?" not equal to "A" will result with an error. Gantry can be activated
only on A axis, and A and B axes are to be always used for the Gantry control.

Note that AGantryOn is automatically cleared to 0 when AMotorOn or BMotorOn are 0. The
Gantry mode is typically enabled by the user only after both A and B motors are enabled.
