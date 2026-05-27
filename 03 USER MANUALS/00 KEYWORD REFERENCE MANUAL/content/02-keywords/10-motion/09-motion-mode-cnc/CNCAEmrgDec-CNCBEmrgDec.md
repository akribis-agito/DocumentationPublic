---
summary: CNC vector deceleration used for an emergency stop.
---
# CNCAEmrgDec/CNCBEmrgDec

CNC vector deceleration used for an emergency stop.

## Overview

`CNCAEmrgDec` (and its `CNCBEmrgDec` counterpart on the second CNC engine) is the CNC vector deceleration to use in case of an emergency stop. An emergency stop occurs when hitting the hardware Reverse/Forward limit switches, or when reaching the software position limits `RevPLim`/`FwdPLim`.

This is distinct from the normal per-segment deceleration reported by [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md).

## Examples

```text
ACNCAEmrgDec=2000000 ; vector deceleration used on emergency stop
```

## See also

- [CNCADecel/CNCBDecel](CNCADecel-CNCBDecel.md) — normal active-segment deceleration
- [StopCNCA](StopCNCA.md) — stop CNC motion on queue A
