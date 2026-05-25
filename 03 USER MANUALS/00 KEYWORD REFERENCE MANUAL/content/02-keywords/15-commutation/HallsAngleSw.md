# HallsAngleSw

**Definition:**

HallsAngleSw sets the electrical angle at which the commutation switches from Hall-sensor-based to encoder-based feedback during startup. Below this angle threshold the controller uses the Hall sensors for commutation; above it, it transitions to encoder-based commutation. It is an axis-related parameter.

%%
Needs verification
HallsAngleSw was not found in the AG300_CTL01Params.c firmware parameter table. Confirm availability and parameter attributes before use.
%%

**See also:**

[HallsAngle](HallsAngle.md), [HallsValue](HallsValue.md), [HallOnlyFilt](HallOnlyFilt.md)
