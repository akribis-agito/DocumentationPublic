# RegenOff

**Definition:**

RegenOff sets the DC bus voltage threshold below which the regeneration circuit is deactivated. Once the bus voltage drops below this level the controller switches off the regen resistor. Setting RegenOff lower than RegenOn provides hysteresis to prevent rapid switching. It is a non-axis parameter saved to flash and can be changed at any time.

**See also:**

[RegenOn](RegenOn.md), [RegenCurr](RegenCurr.md), [RegenUsed](RegenUsed.md)
