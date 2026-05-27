---
summary: Array defining the position filter configuration for CNC queue A (or B).
---
# CNCAPosFDef/CNCBPosFDef

Array defining the position filter configuration for CNC queue A (or B).

## Overview

`CNCAPosFDef` (and its `CNCBPosFDef` counterpart) is an array that defines the position filter configuration for CNC motion queue A (or B). Each element specifies filter parameters applied to the position reference of CNC segments. It is a non-axis array saved to flash and can be changed at any time.

The filter it defines is enabled by [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md).

## Examples

```text
ACNCAPosFDef[1]     ; read the first position-filter coefficient (arrays are 1-indexed)
```

## See also

- [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) — enables the position filter
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
