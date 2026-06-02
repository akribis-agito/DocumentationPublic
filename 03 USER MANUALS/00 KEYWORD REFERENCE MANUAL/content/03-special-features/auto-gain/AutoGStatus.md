# AutoGStatus

**Definition:**

AutoGStatus is a read-only array (indexes 1 to 50) that reports the working values of the automatic gain tuning process for the axis. Its locations expose the latest results and intermediate quantities, including the estimated inertia ratio, the estimation-quality figure, the computed gains (position gain, velocity gain, velocity integral gain, and acceleration feedforward gain), the time of the most recent calculation, the time remaining until the next scheduled update (in minutes), a flag indicating that valid tuning results are present, and internal sample counters used by the algorithm. It is an axis-related status variable and is not saved to flash.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGMode](AutoGMode.md), [AutoGCopy](AutoGCopy.md)
