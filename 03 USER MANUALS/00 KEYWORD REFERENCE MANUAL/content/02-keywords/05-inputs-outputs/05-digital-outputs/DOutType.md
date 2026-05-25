# DOutType

**Definition:**

DOutType configures the digital outputs to operate in either sink or source mode, in 0-based indexing form.

| Bit’s value | Mode        |
|-------------|-------------|
| 0           | Sink mode   |
| 1           | Source mode |

**Example:**

If DOutType = 9 (binary 00000000 00000000 00000000 00001001), output 1 and 4 are in source mode, while all other outputs are in sink mode.

**Note:**

This keyword is applicable only for single ended digital outputs with configurable sink/source types. Please refer to individual product manual for more information.
