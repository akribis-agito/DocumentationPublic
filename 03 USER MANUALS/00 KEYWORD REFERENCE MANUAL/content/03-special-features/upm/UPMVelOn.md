# UPMVelOn

**Definition:**

UPMVelOn enables the UPM anti-cogging compensation function, which applies an angle-indexed correction table (UPMVelTable) to the current reference to cancel cogging torque. The table is indexed by the commutation (electrical) angle in degrees, and the corresponding table entry is added to the current reference at each control cycle. This compensation applies only to brushless motors. UPMVelOn is a 0/1 enable. It is an axis-related parameter and is not saved to flash; it can be changed at any time.

**See also:**

[UPMDistOn](UPMDistOn.md), [UPMRptOn](UPMRptOn.md)
