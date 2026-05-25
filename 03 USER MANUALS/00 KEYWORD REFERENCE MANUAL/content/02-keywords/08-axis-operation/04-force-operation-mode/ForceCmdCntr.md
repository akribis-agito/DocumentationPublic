# ForceCmdCntr

**Definition:**

ForceCmdCntr is the time elapsed, in milliseconds,

1.  (if ForceCmdSrc = 0) under force operation mode.

2.  (if ForceCmdSrc = 1 or 2) under the existing ForceCmdVal array entry. This value will reset to 0 upon switching to the next ForceCmdVal entry.

ForceCmdCntr will reset to 0 only

1.  upon receipt of GoToForceMode command,

2.  upon automatic condition switching, or

3.  upon digital input for switching to force operation mode.

This means if OperationMode is directly assigned, user can configure it to any initial value beforehand and begin the timer from such value.

**Note:**

User can overwrite ForceCmdCntr at any time under force operation mode.
