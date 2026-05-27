---
summary: Reports the acceleration of the active CNC segment on queue A (or B).
---
# CNCAAccel/CNCBAccel

Reports the acceleration of the active CNC segment on queue A (or B).

## Overview

`CNCAAccel` (and its `CNCBAccel` counterpart) is a read-only parameter that reports the current acceleration value of the active CNC motion segment being executed on queue A (or B). It reflects the acceleration encoded in the segment that was pushed to the CNC FIFO. It is a non-axis, read-only parameter that is not saved to flash.

It pairs with [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md), which reports the segment deceleration. The underlying segment data comes from [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) and is loaded via [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md).

## Examples

```text
ACNCAAccel          ; read the active segment acceleration
```

## See also

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — active segment deceleration
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
- [CNCAPushType/CNCBPushType](CNCAPushType-CNCBPushType.md) — push a segment to the FIFO
