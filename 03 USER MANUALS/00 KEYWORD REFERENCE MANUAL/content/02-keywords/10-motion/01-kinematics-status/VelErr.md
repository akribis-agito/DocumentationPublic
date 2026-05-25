# VelErr

**Definition:**

VelErr reports the error between velocity reference and feedback, only if the axis is enabled, in position/velocity operation mode, not in open-loop condition and the axis phasing is done. The unit is in terms of main user unit per second.

1.  Under individual (non-gantry) mode

$$
VelErr = VelRef - Vel\lbrack 1\rbrack
$$

2.  Under gantry mode

$$
VelErr = VelRef - GantryVel
$$

Otherwise, VelErr reports 0.

VelErr is generally used for velocity feedback control and motion protection.
