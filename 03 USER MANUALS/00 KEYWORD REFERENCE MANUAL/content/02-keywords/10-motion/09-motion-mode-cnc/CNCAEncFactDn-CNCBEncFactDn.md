---
summary: Denominator of the CNC queue A (or B) encoder scaling ratio.
---
# CNCAEncFactDn/CNCBEncFactDn

Denominator of the CNC queue A (or B) encoder scaling ratio.

## Overview

`CNCAEncFactDn` (and its `CNCBEncFactDn` counterpart on the second CNC engine) is the denominator of the per-axis path-to-encoder scaling ratio applied to a CNC path. Together with [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) it defines the rational scale `CNCAEncFactNu / CNCAEncFactDn`, which maps CNC path units to the axis encoder counts so that member axes with different encoder resolutions can take part in the same coordinated path while the resultant geometry stays accurate. It is an axis-related parameter saved to flash, and cannot be changed while the axis is in motion. This is the numerator/denominator form that the CNC engine actually applies; the single-value [CNCAEncRatio/CNCBEncRatio](CNCAEncRatio-CNCBEncRatio.md) expresses the same idea but currently has no effect.

## How it works

Set the pair so that `CNCAEncFactNu / CNCAEncFactDn` equals the resolution ratio needed for the axis. When numerator and denominator are equal (the default `1` / `1`), the ratio is 1 and no scaling is applied. Both keywords accept whole numbers in the range `1`-`2000`, so a wide range of rational ratios can be expressed — for example `2` here with [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) = `3` gives a 3/2 (1.5:1) ratio.

When either value changes, the controller forms both the ratio and its reciprocal for the axis, ready for use during the path. The ratio is applied as the path runs: the engine uses it to convert each axis's position reference into the queued path units and uses the reciprocal to convert the queued segment coordinates back into per-axis position commands. Configure the pair on each member axis before starting the move, since it cannot be changed in motion.

## Examples

```text
ACNCAEncFactDn[1]=1     ; denominator = 1 (default)
ACNCAEncFactDn[1]=2     ; with CNCAEncFactNu = 3 gives a 3/2 (1.5:1) scaling ratio
ACNCAEncFactDn[1]       ; read the current denominator
```

## See also

- [CNCAEncFactNu/CNCBEncFactNu](CNCAEncFactNu-CNCBEncFactNu.md) — numerator of the scaling ratio
- [CNCAEncRatio/CNCBEncRatio](CNCAEncRatio-CNCBEncRatio.md) — single-value form (no current effect)
- [CNCAFIFO/CNCBFIFO](CNCAFIFO-CNCBFIFO.md) — queued segment data
