---
summary: Reports the deceleration of the active CNC segment on queue A (or B).
---
# CNCADecel/CNCBDecel

Reports the deceleration of the active CNC segment on queue A (or B).

## Overview

`CNCADecel` (and its `CNCBDecel` counterpart) is a read-only parameter that reports the current deceleration value of the active CNC motion segment being executed on queue A (or B). It reflects the deceleration encoded in the segment that was pushed to the CNC FIFO. It is a non-axis, read-only parameter that is not saved to flash.

It pairs with [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md), which reports the segment acceleration, and relates to [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md), the commanded speed at the end of the segment.

## Examples

```text
ACNCADecel          ; read the active segment deceleration
```

## See also

- [CNCAAccel/CNCBAccel](CNCAAccel-CNCBAccel.md) — active segment acceleration
- [CNCAEndSpeed/CNCBEndSpeed](CNCAEndSpeed-CNCBEndSpeed.md) — end-of-segment speed
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
