# CNCAFIFO/CNCBFIFO

**Definition:**

CNCAFIFO (and its CNCB equivalent) is a read-only array that holds the raw segment data currently queued in the CNC motion FIFO for queue A (or B). Reading it allows inspection of the pending motion segments before they are executed. It is a non-axis, read-only array that is not saved to flash.

**See also:**

[CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md), [CNCAClear/CNCBClear](CNCAClear-CNCBClear.md), [StopCNCA](StopCNCA.md)
