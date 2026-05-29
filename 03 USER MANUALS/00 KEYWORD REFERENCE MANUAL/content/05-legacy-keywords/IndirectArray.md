# IndirectArray

**Definition:**

IndirectArray selects the target array to be accessed indirectly. The value is an array selector, not a CAN code; the only currently supported selection is 1 (GenData), and the valid range is 1..1 with a default of 1. Together with IndirectIndex and IndirectValue, it forms the three-register indirect access mechanism that allows dynamic array addressing. It is a non-axis parameter and is not saved to flash.

**See also:**

[IndirectIndex](IndirectIndex.md), [IndirectValue](IndirectValue.md), [IndirectDo](IndirectDo.md)
