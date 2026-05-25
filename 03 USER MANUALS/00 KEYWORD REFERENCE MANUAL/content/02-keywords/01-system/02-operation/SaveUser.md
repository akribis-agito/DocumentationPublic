# SaveUser

**Definition:**

SaveUser is a command that saves the current parameter values to a dedicated user parameter area in flash memory, separate from the factory defaults. The saved values can later be restored with [LoadUser](LoadUser.md). The motor must be stopped before this command is issued.

Saving to flash is not allowed while motor is enabled.

**See also:**

[LoadUser](LoadUser.md), [Save](Save.md), [Load](Load.md)
