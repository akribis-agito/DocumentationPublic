# DInPort/DInPortHigh

**Definition:**

DInPort/DInPortHigh reflects the state of the digital inputs after debouncing and logic inversion (if used).

| Bit’s value | State |
|-------------|-------|
| 0           | Off   |
| 1           | On    |

**Example:**

If DInPortHigh = 18 (binary 00000000 00000000 00000000 000<u>1</u>00<u>1</u>0), only digital inputs 34 and 37 are in on state. deweeredf

**Note:**

For bi-directional IO’s that are configured as an output, DInPort/DInPortHigh can be used to read back the state of the output.
