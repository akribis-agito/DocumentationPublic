# AutoGOn

**Definition:**

AutoGOn enables the automatic gain tuning process. When set to 1, the controller begins collecting motion data and computing optimal servo gains based on the configured AutoG parameters. When set back to 0 the process stops and its accumulated state and status are cleared; after re-enabling, the internal filter must re-stabilize over a number of calculation cycles before the reported results become valid again. It is an axis-related parameter and is not saved to flash.

**See also:**

[AutoGMode](AutoGMode.md), [AutoGStatus](AutoGStatus.md), [AutoGBW](AutoGBW.md), [AutoGCopy](AutoGCopy.md)
