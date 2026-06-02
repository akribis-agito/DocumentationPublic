# AutoGMask

**Definition:**

AutoGMask is an array that specifies which servo gain parameters the auto-gain algorithm is allowed to update. The array has four usable elements, addressed starting at index [1]: element [1] is the position gain, element [2] is the velocity gain, element [3] is the velocity integral gain, and element [4] is the acceleration feedforward gain. Each element is set to 1 to allow the corresponding gain to be written or to 0 to leave it unchanged. The mask is applied both when the gains are downloaded automatically in the full-auto modes and when AutoGCopy is used to apply the calculated gains in the semi-auto modes. The default value of each element is 1. It is an axis-related array parameter saved to flash and can be changed at any time.

**See also:**

[AutoGCopy](AutoGCopy.md), [AutoGOn](AutoGOn.md), [AutoGBW](AutoGBW.md)
