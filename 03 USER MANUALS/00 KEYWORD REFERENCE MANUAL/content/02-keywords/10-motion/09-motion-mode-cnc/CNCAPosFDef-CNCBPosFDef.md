---
summary: Array defining the position filter configuration for CNC queue A (or B).
---
# CNCAPosFDef/CNCBPosFDef

Array defining the position filter configuration for CNC queue A (or B).

## Overview

`CNCAPosFDef` (and its `CNCBPosFDef` counterpart on the second CNC engine) is the array that defines the path-following position filter for a CNC path. It describes the filter that smooths the resultant CNC path reference before it is split among the member axes, reducing the jerk transmitted to the mechanics. The filter only takes effect when it is enabled by [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md). It applies to the whole CNC engine (not to an individual member axis), is saved to flash, and can be changed at any time, including during motion.

## How it works

The array uses the controller's standard customisable position-filter definition: element 1 selects the filter **type**, and elements 2-5 supply up to four **parameters** for that type. A type of `0` (the default) means no filter, so the path reference passes through unchanged. When a filter type is selected and [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) = 1, the controller derives the working coefficients from these parameters and applies a second-order (biquad-style) smoothing filter to the resultant path reference. The same definition convention is used elsewhere on the controller for customisable position filters.

The definition is checked when the path begins: an invalid combination of type and parameters causes the move to be rejected, so verify the values before enabling the filter with [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md). Because the array can be changed in motion, you can adjust the filter during a path; the controller recomputes the working coefficients in the background whenever the definition or the enable flag changes. A path program can also rewrite the filter type and parameters mid-path by queuing a dedicated parameter-change segment, so the smoothing can be tuned at specific points along the path without interrupting the queue.

## Examples

```text
ACNCAPosFDef[1]=0    ; element 1 = filter type (0 = no filter, the default)
ACNCAPosFDef[1]      ; read the filter-type element (arrays are 1-indexed)
ACNCAPosFDef[2]      ; read the first filter parameter
```

## See also

- [CNCAPosFOn/CNCBPosFOn](CNCAPosFOn-CNCBPosFOn.md) — enables/disables this position filter
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
