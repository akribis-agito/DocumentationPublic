# OpenLoopCurr

**Condition:**

It is only used when OpenLoopOn = 1.

**Definition:**

OpenLoopCurr is the current reference, in milliamperes, applied onto the current loop if the axis is in current open-loop condition.

This value will bypass all the current references contributed by position, velocity or force control, except for cogging compensation ([UPMVelTable](../../../02-keywords/09-current-and-voltage/03-current-compensation/UPMVelTable.md)) and DC offset ([CurrRefOffset](../../../02-keywords/09-current-and-voltage/03-current-compensation/CurrRefOffset.md)). This value is applied per individual motor basis, which means decoupling matrix is not used (e.g. excitation not in gantry axis).
