---
summary: Enables the position filter on the CNC queue A (or B) reference output.
---
# CNCAPosFOn/CNCBPosFOn

Enables the position filter on the CNC queue A (or B) reference output.

## Overview

`CNCAPosFOn` (and its `CNCBPosFOn` counterpart on the second CNC engine) enables the path-following position filter on a CNC path. When set to `1`, the filter defined by [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) is applied to smooth the resultant path position reference before it is split among the member axes; when `0` (the default), the reference passes through unfiltered. Smoothing the path reference reduces the jerk transmitted to the mechanics on every member axis at once. It applies to the whole CNC engine (not to an individual member axis), is saved to flash, and can be changed at any time, including during motion.

The keyword accepts only `0` (filter off) and `1` (filter on).

## How it works

The filter acts on the resultant CNC path reference, so enabling it smooths all member axes together and keeps the coordinated geometry consistent. The filter coefficients themselves come from [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md); this keyword only switches that filter into or out of the path.

When a CNC path begins, the controller validates the combination of `CNCAPosFOn` and [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md): if the filter is enabled, the definition must describe a valid filter or the move is rejected. Set up the definition first, then enable the filter. Because the parameter can be changed in motion, you can also turn the filter on or off during a path; the controller recomputes the working coefficients in the background when the enable flag or the definition changes. The filter only does any work while a CNC path is running. A path program can additionally switch the filter on or off mid-path by queuing a dedicated parameter-change segment, which updates the same enable flag and definition without interrupting the queue.

## Examples

```text
ACNCAPosFOn=0        ; position filter disabled (default)
ACNCAPosFOn=1        ; apply the CNCAPosFDef position filter to the CNC path reference
```

## See also

- [CNCAPosFDef/CNCBPosFDef](CNCAPosFDef-CNCBPosFDef.md) — filter definition applied when enabled
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
