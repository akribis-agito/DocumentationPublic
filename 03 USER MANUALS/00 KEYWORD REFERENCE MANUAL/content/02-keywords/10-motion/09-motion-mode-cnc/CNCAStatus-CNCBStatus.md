---
summary: Read-only array holding CNC engine status data for queue A (or B).
---
# CNCAStatus/CNCBStatus

Read-only array holding CNC engine status data for queue A (or B).

## Overview

`CNCAStatus` (and its `CNCBStatus` counterpart on the second CNC engine) is a read-only array parameter holding CNC status data for queue A (or B).

## How it works

Some of the statuses are not valid after reset or power-on, some others are not valid when the CNC FIFO is empty, and some others when there is no CNC FIFO motion, and so on. These statuses take the value `-1` when they are not valid (this value is never a valid value for any of these statuses when they are valid).

Please refer to the Motion Modes – CNC section for more detailed information.

## Examples

```text
CNCAStatus[1]?      ; read the first status element (arrays are 1-indexed)
```

## See also

- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAVel/CNCBVel](CNCAVel-CNCBVel.md) — current velocity components
