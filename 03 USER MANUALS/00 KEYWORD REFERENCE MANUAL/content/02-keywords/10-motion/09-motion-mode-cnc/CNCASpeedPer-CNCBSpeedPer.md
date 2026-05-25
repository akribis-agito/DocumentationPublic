# CNCASpeedPer/CNCBSpeedPer

**Definition:**

CNCASpeedPer (and its CNCB equivalent) sets the speed percentage override applied to CNC motion queue A (or B). Setting this to 100 uses the programmed segment speeds; lower values slow all segments proportionally without reprogramming the FIFO. It is a non-axis parameter, not saved to flash, and can be changed at any time.

**See also:**

[CNCAVel/CNCBVel](CNCAVel-CNCBVel.md), [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md)
