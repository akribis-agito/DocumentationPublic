# IndirectDo

**Definition:**

IndirectDo is a command that executes the indirect array write operation. When triggered, it stores the value held in IndirectValue into the element at the index specified by IndirectIndex of the array selected by IndirectArray. If IndirectArray names an array that is not supported, the write is rejected with error 115. If IndirectIndex is below 1 or above the size of the selected array, the write is rejected with error 116. When the target is the GenData array no value-range check is applied, since any value may be stored there. It is a non-axis command and is not saved to flash.

**See also:**

[IndirectArray](IndirectArray.md), [IndirectIndex](IndirectIndex.md), [IndirectValue](IndirectValue.md)
