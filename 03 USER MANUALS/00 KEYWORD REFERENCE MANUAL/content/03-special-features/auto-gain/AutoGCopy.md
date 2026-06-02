# AutoGCopy

**Definition:**

AutoGCopy is a command that applies the gains computed by the automatic gain tuning algorithm to the active servo controller parameters. The computed values are written into the gain set selected by AutoGNumSet, and only the individual gains enabled by AutoGMask (position gain, velocity gain, velocity integral gain, and acceleration feedforward gain) are copied. The copy is performed only when valid tuning results are present and only in the semi-automatic modes (AutoGMode 2 or 4), where gains are calculated on request but not applied automatically; in those modes AutoGCopy is the step that transfers them to the controller. It is an axis-related command and is not saved to flash.

**See also:**

[AutoGOn](AutoGOn.md), [AutoGStatus](AutoGStatus.md), [AutoGBW](AutoGBW.md)
