# CNCAClear/CNCBClear

**Definition:**

CNCAClear (and its CNCB equivalent) is a command that clears all pending segments from the CNC motion FIFO queue A (or B). It resets the queue so that new segments can be loaded from a clean state. It is a non-axis command function that can be issued at any time, including during motion.

**See also:**

[CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md), [StopCNCA](StopCNCA.md), [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md)
