# RecTrigPos

**Definition:**

RecTrigPos defines the percentage of data points out of RecLength to capture before the trigger condition(s) activate. It is normally used for debugging process to allow monitoring of pre-trigger data.

| Index | Descriptions                 |
|-------|------------------------------|
| 1     | First scope                  |
| 2     | Second scope (if applicable) |

**Example:**

If RecLength\[1\] = 16384 and RecTrigPos\[1\] = 10, the first scope will have 1638 pre-trigger data points and 14746 post-trigger data points.
