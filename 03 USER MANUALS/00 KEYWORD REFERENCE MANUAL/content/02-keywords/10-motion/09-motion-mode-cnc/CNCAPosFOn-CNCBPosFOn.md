---
summary: Enables the position filter on the CNC queue A (or B) reference output.
---
# CNCAPosFOn/CNCBPosFOn

Enables the position filter on the CNC queue A (or B) reference output.

## Overview

`CNCAPosFOn` (and its `CNCBPosFOn` counterpart) enables the position filter on the CNC motion queue A (or B) reference output. When active, the filter defined by [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) is applied to smooth the position reference before it is fed to the servo loop. It is a non-axis parameter saved to flash and can be changed at any time.

## Examples

```text
ACNCAPosFOn=1        ; enable the CNC position filter
```

## See also

- [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) — position filter configuration
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
