# ForceInTTime

**Condition:**

This keyword is only applicable when [ForceCmdSrc](../../../02-keywords/08-axis-operation/04-force-operation-mode/ForceCmdSrc.md) = 1 or 2.

**Definition:**

ForceInTTime defines the minimum time required (in milliseconds) for force error (ForceErr) to always stay within settling window (ForceInTTol) before the axis is considered settled in ForceInTStat.

The internal timer is active only while ForceInTStat = 3. It starts when ForceErr first enters the ForceInTTol window, and resets when ForceErr exits the window. Once ForceErr stays within the window for ForceInTTime, the axis is considered settled (ForceInTStat = 4) and the settling condition will no longer be checked.
