# GantryDLoopOn

**Definition:**

GantryDLoopOn enables the dual-loop (position + yaw) control mode for the gantry axis. When set to a non-zero value, the controller adds a yaw correction current to the two gantry drive motors to maintain alignment. It is an axis-related parameter.

%%
Needs verification
GantryDLoopOn was not found in the AG300_CTL01Params.c firmware parameter table. Confirm availability and parameter attributes before use.
%%

**See also:**

[GantryOn](GantryOn.md), [GantryYawRef](GantryYawRef.md), [GantryPosGain](../03-gantry-tuning/GantryPosGain.md)
