# DOutPortSBit/DOutPortCBit/DOutPortTBit

DOutPortSBit sets, DOutPortCBit clears, and DOutPortTBit toggles the individual bits of DOutPort.

Each index corresponds to an output (1-based index).

| Index | Changes DOutPort Bit \# | Corresponds to |
|-------|-------------------------|----------------|
| 1     | 0                       | Output 1       |
| 2     | 1                       | Output 2       |
| 3     | 2                       | Output 3       |
| …     | …                       | …              |

**Example:**

If DOutPort is initially 6 (0b0110) and

1.  DOutPortSBit\[4\] is called, then DOutPort will become 14 (0b1110) where bit 3 is set.

2.  DOutPortCBit\[2\] is called, then DOutPort will become 4 (0b0100) where bit 1 is cleared.

3.  DOutPortTBit\[3\] is called, then DOutPort will become 2 (0b0010) where bit 2 is toggled.

| Initial DOutPort value | Command sent | Operation | Final DOutPort value |
|---|---|---|---|
| 6 (0b0110) | DOutPortSBit[4] | Sets bit 3 | 14 (0b1110) |
| 6 (0b0110) | DOutPortCBit[2] | Clears bit 1 | 4 (0b0100) |
| 6 (0b0110) | DOutPortTBit[3] | Toggle bit 2 | 2 (0b0010) |
