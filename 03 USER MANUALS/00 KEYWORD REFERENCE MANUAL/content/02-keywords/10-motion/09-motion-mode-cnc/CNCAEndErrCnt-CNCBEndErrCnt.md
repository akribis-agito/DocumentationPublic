# CNCAEndErrCnt/CNCBEndErrCnt

**Definition:**

CNCAEndErrCnt (and its CNCB equivalent) sets the maximum allowed position error count at the end of a CNC motion segment before a fault is generated. If the axis position error exceeds this threshold when a segment completes, the controller flags an end-of-segment error. It is a non-axis parameter, not saved to flash, and can be changed at any time.

**See also:**

[CNCAEndSegMod/CNCBEndSegMod](CNCAEndSegMod-CNCBEndSegMod.md), [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md)
