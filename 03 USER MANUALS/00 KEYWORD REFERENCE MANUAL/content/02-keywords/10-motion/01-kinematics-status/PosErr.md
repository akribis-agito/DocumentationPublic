# PosErr

**Definition:**

PosErr reports the error between position reference and feedback, only if the axis is enabled, in position operation mode, not in open-loop condition and the axis phasing is done. The unit is in terms of main user unit.

1.  Under individual (non-gantry) mode

$$
PosErr = PosRef - Pos
$$

2.  Under gantry mode

$$
PosErr = PosRef - GantryFdbk
$$

Otherwise, PosErr reports 0.

PosErr is generally used for position feedback control, motion protection, homing, operation mode switching, etc.
